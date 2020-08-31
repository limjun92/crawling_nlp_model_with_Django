from django.shortcuts import render, redirect
from app_crawling.module.use_url import get_video, find_comment
from app_crawling.module.use_data import comment_save
from app_crawling.module.use_trainning_lsmt import train_model, use_model_with_key

import os
import pandas as pd

SESSION_SAVE_EVERY_REQUEST = True
# home으로 가기
def home(request):
    path = "./saved_model"
    file_list = os.listdir(path)
    file_list_py = [file for file in file_list]
    
    request.session['csv_list'] = []

    return render(request, 'home.html',{'save_model_list':file_list_py})

# 크롤링 페이지로 이동
def crawling(request):

    return render(request, 'crawling.html')

# 유튜브검색해서 상위부터 원하는 개수만큼 받아오기
def get_title(request):
    
    keyword = request.POST['keyword']
    videos = get_video(request.POST['keyword'], int(request.POST['num']))
    return render(request, 'title_list.html' ,{'videos':videos,'keyword':keyword})

# 해당 영상의 댓글을 가져오기
def comment(request, video_id, keyword):
    comments = find_comment(video_id)
    request.session.modified = True
    request.session['comments'] = comments
    return render(request, 'comment.html', {'comments':comments,'keyword':keyword})

# 해당 영상의 댓글을 csv로 저장하기
def save(request, keyword):

    comments = request.session.get('comments')
    comments = list(comments)
    name = keyword+'_'+str(len(comments))
    comment_save(name,comments) 

    path = "./saved_model"
    file_list = os.listdir(path)
    file_list_py = [file for file in file_list]

    return render(request, 'home.html',{'save_model_list':file_list_py})

def model(request):
    path = "./"
    file_list = os.listdir(path)
    file_list_py = [file for file in file_list if file.endswith(".csv")]

    return render(request, 'model.html', {'csv_list': file_list_py})

def get_csv(request,csv):
    
    path = "./"
    file_list = os.listdir(path)
    file_list_py = [file for file in file_list if file.endswith(".csv")]

    arr = request.session.get('csv_list')
    if csv not in arr:
        arr.append(csv)

    request.session['csv_list'] = arr

    print('===============',len(arr))

    num = 0
    for i in arr:
        num+=int(i.split('_')[-1].split('.')[0])

    print(num)

    return render(request, 'model.html', {'select_csv':arr,'csv_list': file_list_py,'num':num})

def create_model(request):

    arr = request.session.get('csv_list')

    data_list = []

    for csv in arr:
        data_list.append(pd.read_csv(csv, header = None, names = ['review','date','like']))

    name = request.POST['name']

    all_data = pd.concat(data_list)

    train_model(all_data,name)

    path = "./saved_model"
    file_list = os.listdir(path)
    file_list_py = [file for file in file_list]

    request.session['csv_list'] = []

    return render(request, 'home.html',{'save_model_list':file_list_py})

def use_model(request, name):
    return render(request, 'use_model.html',{'name':name})

def connect_model(request,name):

    keyword = request.POST['keyword']
    date = request.POST['date']

    result = use_model_with_key(keyword, date, name)

    return render(request, 'use_model.html',{'name':name,'result':result})

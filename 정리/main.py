from sele import search, search_comment
import csv
import pandas as pd
#keyword = input()

# 유튜에서 title, href, 조회수, 날짜전을 가져온다

youtube_list = search('코로나')

for i in range(len(youtube_list)):
    print(i+1,'/',len(youtube_list))
    youtube_list[i]+=search_comment(youtube_list[i][1])

with open('twice.csv', 'w',-1,'utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in youtube_list:
        writer.writerow(i)

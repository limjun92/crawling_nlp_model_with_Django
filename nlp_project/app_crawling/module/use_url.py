# -*- coding: utf-8 -*-
import requests
import json
import csv

headers = {
    'authority': 'www.youtube.com',
    'x-youtube-device': 'cbr=Chrome&cbrver=85.0.4183.83&ceng=WebKit&cengver=537.36&cos=Windows&cosver=10.0',
    'x-youtube-page-label': 'youtube.ytfe.desktop_20200828_2_RC1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'x-youtube-variants-checksum': 'f684c9514fe7520997487b07864e3848',
    'content-type': 'application/x-www-form-urlencoded',
    'x-youtube-page-cl': '329220766',
    'x-spf-referer': 'https://www.youtube.com/watch?v=nfMz11N43P4',
    'x-youtube-utc-offset': '540',
    'x-youtube-client-name': '1',
    'x-spf-previous': 'https://www.youtube.com/watch?v=nfMz11N43P4',
    'x-youtube-client-version': '2.20200829.02.01',
    'x-youtube-identity-token': 'QUFFLUhqbXRwWUVVZ2hpdGc1dmRNVUEwaHZVejJoTGRpQXw=',
    'x-youtube-time-zone': 'Asia/Seoul',
    'x-youtube-ad-signals': 'dt=1599010970588&flash=0&frm&u_tz=540&u_his=3&u_java&u_h=1080&u_w=1920&u_ah=1040&u_aw=1920&u_cd=24&u_nplug=3&u_nmime=4&bc=31&bih=843&biw=427&brdim=602%2C0%2C602%2C0%2C1920%2C0%2C1325%2C1047%2C443%2C843&vis=1&wgl=true&ca_type=image&bid=ANyPxKrkOkPgVMemvpBwoYZp5xDK26ZRZ92T8qSJMqAXvzJQoSphzHkNZP4RklSg0NiHOvbiRh0xoKmGKHDc_TBe3Aow7BU98A',
    'accept': '*/*',
    'origin': 'https://www.youtube.com',
    'x-client-data': 'CIa2yQEIo7bJAQjBtskBCKmdygEIlqzKAQiZtcoBCPbHygEI+MfKAQjnyMoBCOnIygEItMvKAQiV1soBCLzXygEY97/KAQ==',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.youtube.com/watch?v=nfMz11N43P4',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'VISITOR_INFO1_LIVE=kr8ukn4-Fsc; LOGIN_INFO=AFmmF2swRQIgMGpQO8CQl8XYfROj-WQeSt1ekkT10jQhapVMQPK21pgCIQC6H_wY6x5j4vdBmrt_eXkyonVIBa8SCjE3jaCTCfzPUg:QUQ3MjNmejNVSHE5ZUtyd2oxNGIxX1pfdV9xZ1A2Zmh6NWhNLUNLWnBBalNMZ0lxV3BTM3VfYnJBYVB5cTI5SWc0MDRWQkRTV0dXemthTXh6ZnE0RG1IZ19CQ0Y5WWxTUnJqdWJfNGlHb3Z4ZndJM2NNTXBoQjVFbGJSbGMzdzVxWU5wYVgzUUJtU2d6eVF2RWhXYnBkaU5JamFHRzRnS09FSWo4cEtNRmZzNXVMRnhVR2trRHFsb0dSZFdvSmd1QXFfeTNvX1UzdkNZ; PREF=f1=50000000&al=ko&HIDDEN_MASTHEAD_ID=TjytsrLrwJA&f4=4000000; SID=0wd_sYOw8Bils0iBx3lPOnFgI9O4Hfinb63varyiGrCiiTK2cCEQPIrX3cfECd-lesUQYw.; __Secure-3PSID=0wd_sYOw8Bils0iBx3lPOnFgI9O4Hfinb63varyiGrCiiTK2h3RoS7Iu1q1M2q3F_vTSQQ.; HSID=AqNGx7vnmzaiAIGDm; SSID=AbVM1DW3tGc4TKD4K; APISID=GKq7sTfqp3OARl1W/A9Axk92q67DM_AU5u; SAPISID=ZSnl7S2v6qO5EhhH/AQiS7NXuBNH6vgOta; __Secure-3PAPISID=ZSnl7S2v6qO5EhhH/AQiS7NXuBNH6vgOta; YSC=GQjbnL59Gd0; SIDCC=AJi4QfEYnDPPBKHCo75eCgFmVPPM-R0z7_mSx0lgWlB_aBUp9NNaGx8C8-4b7YOt3Tm-b1IB1eyb; __Secure-3PSIDCC=AJi4QfFlFgwxeNU0cjwFrB9DYvqjTZsp1ihHNqrBNSFKYGHw-dqKhOmYE_4T7GqXxgOWSLorZpQ',
}

data = {
  'session_token': 'QUFFLUhqa2dva29CeWItTEx4R2pyY3o4RTBHZlFENU1jZ3xBQ3Jtc0tsbkMzZ2lPZThyQlJWaU9LV1UzQVBuNGxWVFNTVFRWOXdCNF9UMDI3eDFRNUdvYjJTSmRYdUhscW1VODJ4NXlyRC1YbWlTbkRKMENTa1VvRWRnSFhDektIM2RyRnNCTE1RMGNvOVdVNWozcjQ4UllmS0owamRYVE5hbVVvdnUzSFA3Ny1YYzF3N1RjSkd0MHBTTWZJeWxSSF9rZ2c='
}

# 3. 댓글과 좋아요수 다음 댓글창 파라미터를 가져온다
def text_like_next(ctoken, next_p):

    params = (
        ('action_get_comments', '1'),
        ('pbj', '1'),
        ('ctoken', ctoken),
        ('continuation', ctoken),
        ('itct', next_p),
    )
    response = {}

    try:
        response = requests.post('https://www.youtube.com/comment_service_ajax', headers=headers, params=params, data=data).json()
    except:
        return
    
    contents_info = response['response']['continuationContents']['itemSectionContinuation']
    contents = contents_info['contents']

    for content in contents:
        t_l = []
        text_like_tmp = content['commentThreadRenderer']['comment']['commentRenderer']
        Str = ''
        for s in text_like_tmp['contentText']['runs']:
            Str += s['text']
        t_l.append(Str)
        t_l.append(text_like_tmp['publishedTimeText']['runs'][0]['text'])
        t_l.append(text_like_tmp['likeCount'])
        #print(text_like_tmp['contentText']['runs'][0]['text'])
        text_like.append(t_l)

        commentThreadRenderer = content['commentThreadRenderer']
        if 'replies' in commentThreadRenderer:
            side_param = commentThreadRenderer['replies']['commentRepliesRenderer']['continuations'][0]['nextContinuationData']['clickTrackingParams']
            side_ctoken = commentThreadRenderer['replies']['commentRepliesRenderer']['continuations'][0]['nextContinuationData']['continuation']
            side_text_like(side_ctoken,side_param)
    #print(text_like)
    if 'continuations' in contents_info:
        next_data = contents_info['continuations'][0]['nextContinuationData']
        next_pram = next_data['clickTrackingParams']
        next_ctoken = next_data['continuation']
        print(next_pram)
        text_like_next(next_ctoken,next_pram)

# 4. 대댓글을 가져온다
def side_text_like(ctoken, next_p):

    params = (
        ('action_get_comment_replies', '1'),
        ('pbj', '1'),
        ('ctoken', ctoken),
        ('continuation', ctoken),
        ('itct', next_p),
    )

    response = {}
    try:
        response = requests.post('https://www.youtube.com/comment_service_ajax', headers=headers, params=params, data=data).json()
    except:
        return

    if 'continuationContents' in response[1]['response']:
        contents_info = response[1]['response']['continuationContents']['commentRepliesContinuation']['contents']

        for content in contents_info:
            t_e = []
            Str = ''
            runs = content['commentRenderer']['contentText']['runs']
            for run in runs:
                Str += run['text']
            t_e.append(Str)
            t_e.append(content['commentRenderer']['publishedTimeText']['runs'][0]['text'])
            t_e.append(content['commentRenderer']['likeCount'])
            text_like.append(t_e)
        
        next_p_c = response[1]['response']['continuationContents']['commentRepliesContinuation']
        if 'continuations' in next_p_c:
            next_pc = next_p_c['continuations'][0]['nextContinuationData']
            next_p = next_pc['clickTrackingParams']
            next_c = next_pc['continuation']
            side_text_like(next_c, next_p)

# 2. 원하는 영상에 접근한다
def find_comment(id):
    params = (
        ('v', id),
        ('pbj', '1'),
    )
    try:
        response = requests.get('https://www.youtube.com/watch', headers=headers, params=params).json()
    except:
        return
    ContinuationData = response[3]['response']['contents']['twoColumnWatchNextResults']['results']['results']['contents'][2]['itemSectionRenderer']['continuations'][0]['nextContinuationData']
    next_p = ContinuationData['clickTrackingParams']
    ctoken = ContinuationData['continuation']
    text_like_next(ctoken, next_p)
    return text_like

# 1. 원하는 영상을 찾는다. 영상의 타이틀과 아이디를 가져온다 
def get_video(s_query,num):
    params = (
        ('search_query', s_query),
        ('pbj', '1'),
    )
    try:
        response = requests.get('https://www.youtube.com/results', headers=headers, params=params).json()
    except:
        return

    video_ids = response[1]['response']['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents']
    check = False
    for video_id in video_ids:
        if 'itemSectionRenderer' in video_id:
            for content in video_id['itemSectionRenderer']['contents']:
                if 'videoRenderer' in content:
                    video_ids = video_id['itemSectionRenderer']['contents']
                    check = True
                    break
        if check:
            break

    video = []
    index_count = 0
    for video_id in video_ids:
        if 'videoRenderer' in video_id:

            index_count+=1
            print(index_count)
            tmp = []
            video_text = video_id['videoRenderer']['title']['runs'][0]['text']
            video_id = video_id['videoRenderer']['videoId']
            tmp=[video_text,video_id]

            tmp+=get_new_video_info(video_id)
            video.append(tmp)

            if index_count == num:
                break

    return video

##################### 영상 정보 가져오기

# 영상의 날짜, 좋아요 싫어요수, 조회수 
def get_new_video_info(id):
    params = (
        ('v', id),
        ('pbj', '1'),
    )
    try:
        response = requests.get('https://www.youtube.com/watch', headers=headers, params=params).json()
    except:
        return
    video_info_list = []
    video_info = response[3]['response']['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']
    video_info_date = video_info['dateText']['simpleText']
    video_info_like_hate = ''
    
    if 'sentimentBar' in video_info:
        video_info_like_hate = video_info['sentimentBar']['sentimentBarRenderer']['tooltip']
    else:
        video_info_like_hate=None
    video_info_how_many_watch = video_info['viewCount']['videoViewCountRenderer']['viewCount']['simpleText']
    video_info_list = [video_info_date,video_info_like_hate,video_info_how_many_watch]
    
    ContinuationData = response[3]['response']['contents']['twoColumnWatchNextResults']['results']['results']['contents'][2]
    
    if 'itemSectionRenderer' in ContinuationData and 'continuations' in ContinuationData['itemSectionRenderer']: 
        ContinuationData=ContinuationData['itemSectionRenderer']['continuations'][0]['nextContinuationData']
        next_p = ContinuationData['clickTrackingParams']
        ctoken = ContinuationData['continuation']
        video_info_list.append(get_comment_count(ctoken,next_p))

    return video_info_list

def get_comment_count(ctoken,next_p):
    params = (
        ('action_get_comments', '1'),
        ('pbj', '1'),
        ('ctoken', ctoken),
        ('continuation', ctoken),
        ('itct', next_p),
    )
    response = {}
    try:
        response = requests.post('https://www.youtube.com/comment_service_ajax', headers=headers, params=params, data=data).json()
    except:
        return

    contents_info = response['response']['continuationContents']['itemSectionContinuation']['header']['commentsHeaderRenderer']['commentsCount']['simpleText']
    return contents_info

text_like = []

def find_viero(href):
    find_comment(href)
    return text_like
    
#get_new_video_info('MFiTZmUGi18')


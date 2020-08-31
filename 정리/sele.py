from selenium import webdriver as wd 
from selenium.webdriver.common.keys import Keys

def search(search):

    #search = '블랙핑크'

    driver = wd.Chrome(r"C:\Users\chromedriver.exe") 
    url = "https://www.youtube.com/results?search_query="+search#+"&sp=EgIIAw%253D%253D" 
    driver.get(url)

    import time
    SCROLL_PAUSE_TIME = 1
    # 한번 스크롤 하고 멈출 시간 설정

    body = driver.find_element_by_tag_name('body')
    # body태그를 선택하여 body에 넣음
    # 스코롤 횟수를 정해준다
    for i in range(1):
        last_height = driver.execute_script('return document.documentElement.scrollHeight')
        # 현재 화면의 길이를 리턴 받아 last_height에 넣음
        for i in range(2):
            body.send_keys(Keys.END)
            # body 본문에 END키를 입력(스크롤내림)
            time.sleep(SCROLL_PAUSE_TIME)

        new_height = driver.execute_script('return document.documentElement.scrollHeight')
        if new_height == last_height:
            break;

    from bs4 import BeautifulSoup

    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')

    all_videos = soup.find_all(id='dismissable')

    youtube_list = []
    for video in all_videos:
        title = video.find('a',id='video-title')
        metadata = video.find(id='metadata-line')
        if len(title.text.strip())>0:
            # 공백을 제거하고 글자수가 0보다 크면 append  
            day_before = None
            if len(metadata.text.strip().split('\n'))==2:
                views, day_before = metadata.text.strip().split('\n')
            else:
                day_before = None
            youtube_list.append([title.text,title['href'],day_before])

    return youtube_list

def search_comment(href):
    
    driver = wd.Chrome(r"C:\Users\chromedriver.exe") 
    url = "https://www.youtube.com/"+href
    driver.get(url)

    import time
    SCROLL_PAUSE_TIME = 0.5
    # 한번 스크롤 하고 멈출 시간 설정

    body = driver.find_element_by_tag_name('body')
    # body태그를 선택하여 body에 넣음

    for i in range(1):
        last_height = driver.execute_script('return document.documentElement.scrollHeight')
        # 현재 화면의 길이를 리턴 받아 last_height에 넣음
        for i in range(5):
            body.send_keys(Keys.END)
            # body 본문에 END키를 입력(스크롤내림)
            time.sleep(SCROLL_PAUSE_TIME)

        new_height = driver.execute_script('return document.documentElement.scrollHeight')
        if new_height == last_height:
            break;

    from bs4 import BeautifulSoup

    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')
    #print('=====================================')

    result = []

    view_count = soup.find(class_='view-count')

    if view_count:
        result.append(view_count.get_text())
    else:
        result.append(None)

    if soup.find('div',id='info') and soup.find('div',id='info').find(id='menu-container') and soup.find('div',id='info').find(id='menu-container').find(id='menu') and soup.find('div',id='info').find(id='menu-container').find(id='menu').find_all(id='text'):
        view_info = soup.find('div',id='info').find(id='menu-container').find(id='menu').find_all(id='text')
        for i in range(2):
            if view_info[i]:
                result.append(view_info[i].get_text())
            else :
                result.append(None)

    owner_sub_count = soup.find(id='owner-sub-count')

    if owner_sub_count:
        result.append(owner_sub_count.get_text())
    else :
        result.append(None)
    #result.append(owner_sub_count)

    count_text =soup.find(class_='count-text')

    if count_text:
        result.append(count_text.get_text())
    else:
        result.append(None)

    
    # all_main = soup.find_all(id='main')
    # for main in all_main:
    #     tmp = []
        # if main.find(class_='published-time-text'):
        #     print(main.find(class_='published-time-text').get_text())
        # if main.find(id='content-text'):
        #     print(main.find(id='content-text').get_text())
        # if main.find(id='vote-count-middle'):
        #     print(main.find(id='vote-count-middle').get_text())
    return result

def get_comment(href):
        
    driver = wd.Chrome(r"C:\Users\chromedriver.exe") 
    url = "https://www.youtube.com/"+href
    driver.get(url)

    import time
    SCROLL_PAUSE_TIME = 0.5
    # 한번 스크롤 하고 멈출 시간 설정

    body = driver.find_element_by_tag_name('body')
    # body태그를 선택하여 body에 넣음

    while True:
        last_height = driver.execute_script('return document.documentElement.scrollHeight')
        # 현재 화면의 길이를 리턴 받아 last_height에 넣음
        for i in range(10):
            body.send_keys(Keys.END)
            # body 본문에 END키를 입력(스크롤내림)
            time.sleep(SCROLL_PAUSE_TIME)

        new_height = driver.execute_script('return document.documentElement.scrollHeight')
        if new_height == last_height:
            break;

    from bs4 import BeautifulSoup

    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')
    #print('=====================================')

    text_list = []

    if soup.find(id='comments'):
        comments = soup.find(id='comments').find_all(id='comment')
        
        for comment in comments:
            tmp = []
            tmp.append(comment.find(id='content-text').get_text().strip())
            tmp.append(comment.find(id='vote-count-middle').get_text().strip())
            text_list.append(tmp)
    return text_list


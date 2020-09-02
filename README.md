# 내가 입력한 댓글 좋아요를 평균이상일까?

## 크롤링

키워드 입력
크롤링 수 입력

유튜브의 제목을 상위부터 크롤링 수만큼 키워드와 관련된 내용을 크롤링해서 보여준다

크롤링할때 유튜브 영상의 토큰값으로 접근하고 댓글 토큰값으로 한번더 접근해서 영상의 정보를 가져온다

영상 정보를 클릭하면 해당 영상 댓글의 문장과 날짜 좋아요수 다음 댓글 토큰을 재귀로 넘겨주면서 모두 가져온다

csv 파일로 저장을 원하면 저장을 한다

## 전처리

특수문자 영어문자 모두제거 사이드 공백제거
좋아요가 평균이상이면 1 미만이면 0을 대입

## 모델링

LSTM 모델을 사용
문장과 날짜는 X값 좋아요는 y값으로 지정해서 학습

학습이 완료된 모델을 저장한다


![crawling_search](/img/crawling_search.PNG) 

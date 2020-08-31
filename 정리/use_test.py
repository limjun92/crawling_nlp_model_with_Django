from use_url import get_video, find_viero
from use_data import save

############################# 입력
print("검색: " ,end='')
keyword = input()
keyword=keyword.replace(' ','+')
print("수: " ,end='')
num = int(input())

##############################
ids = get_video(keyword,num)

for i in range(len(ids)):
    print(i+1, ids[i])

num = int(input()) 

comments = find_viero(ids[num-1][1])

print(comments)
print(len(comments))
##############################

print(type(comments))

while True:
    print('저장하시겠습니까? y/n')
    re = input()
    if re == 'y':
        save(ids[num-1][-1]+'_'+keyword+'_'+ids[num-1][1],comments)
        break
    if re == 'n':
        break
    else:
        print('y or n을 입력해주세요')


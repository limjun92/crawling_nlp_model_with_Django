from sele import get_comment, search
import csv

youtube_list = search('사이코지만 괜찮아')

get_lists = []
for i in range(2, 15):
    get_lists += get_comment(youtube_list[i][1])

with open('gwana.csv', 'w',-1,'utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in get_lists:
        writer.writerow(i)
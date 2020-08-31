import csv

def save(name,comment_list):

    with open(name+'.csv', 'w',-1,'utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in comment_list:
            writer.writerow(i)

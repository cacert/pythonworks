'''
Created on May 5, 2015

@author: kasimsert
'''
import csv, json

database = []

def csvtojson():
    def search(name):
        for p in database:
            if p['hostName'] == name:
                return p
    
    with open('stat.csv', 'rb') as csvfile:
        csvfields = ('hostName','serviceName','callcount','successcount','rt')
        reader = csv.DictReader(csvfile, fieldnames=csvfields)
        group = None
        index = 0
        for row in reader:
            group = row['hostName']
            a = search(group)
            if( not a):
                a={}
                a['hostName']=row['hostName']
                index=index+1
                a['index']=index
                a['children']=[]
                database.append(a) 
            a['children'].append({ "rt": row['rt'].rstrip(),"successcount": row['successcount'].rstrip(),
                                    'callcount': row['callcount'].rstrip(), 'serviceName': row['serviceName'].rstrip()})   
         


def appendDate():
    with open('stat_son.csv', 'w') as outfile:
        with open('stat.csv', 'rb') as csvfile:
            for line in csvfile:
                outfile.write(line.rstrip()+',2015/05/21\n')
            
appendDate()

    

'''
Created on May 5, 2015

@author: kasimsert
'''
import csv, json
from web.db import database

database = []

def search(name):
    for p in database:
        if p['HOSTNAME'] == name:
            return p

def csvtojson():
    with open('/Users/kasimsert/Desktop/tez/data/data-01.csv', 'rb') as csvfile:
        csvfields = ('SERVICENAME','COUNT','AVGDURATION','HOSTOID','HOSTNAME')
        reader = csv.DictReader(csvfile, fieldnames=csvfields)
        group = None
        index = 0
        for row in reader:
            group = row['HOSTNAME']
            a = search(group)
            if( not a):
                a={}
                a['HOSTNAME']=row['HOSTNAME']
                index=index+1
                a['index']=index
                a['children']=[]
                database.append(a) 
            a['children'].append({ "AVGDURATION": row['AVGDURATION'].rstrip(),"COUNT": row['COUNT'].rstrip(),
                                    'COUNT': row['COUNT'].rstrip(), 'SERVICENAME': row['SERVICENAME'].rstrip()})   
         
    with open('/Users/kasimsert/Desktop/tez/data/out-01.json', 'w') as outfile:
        json.dump(database, outfile)

def appendDate(filename,columname, value):
    with open(filename+'son', 'w') as outfile:
        with open(filename, 'rb') as csvfile:
            i =0
            for line in csvfile:
                if(i==0):
                    outfile.write(line.rstrip()+',' +columname+'\n')
                else:
                    outfile.write(line.rstrip()+',' +value+'\n')
                i=i+1                
def mergeFiles(files):
    with open('stats.csv', 'w') as outfile:
        for file in files:
            i = 0
            with open(file+'son', 'rb') as infile:
                for line in infile:
                    if(i==0):
                        pass
                    else:
                        outfile.write(line.rstrip()+'\n')
                    i=i+1
                

# appendDate('/Users/kasimsert/Desktop/tez/data/data-01.csv','date','2015/05/13')
# appendDate('/Users/kasimsert/Desktop/tez/data/data-02.csv','date','2015/05/12')
# appendDate('/Users/kasimsert/Desktop/tez/data/data-03.csv','date','2015/05/11')
# csvtojson()
mergeFiles(['/Users/kasimsert/Desktop/tez/data/data-01.csv','/Users/kasimsert/Desktop/tez/data/data-02.csv','/Users/kasimsert/Desktop/tez/data/data-03.csv'])
    

import os
import sys
import csv
import json
alldata={}

def sum_ranking(dirpath, outputfile):
  for curdir,dirs,files in os.walk(dirpath):
    for file in files:
      print(os.path.join(curdir, file))
      with open(os.path.join(curdir, file), encoding='utf-8') as f:
        reader=csv.reader(f)
        for row in reader:
          keyword=row[0]
          occurrence=row[1]
          if keyword in alldata:
            alldata[keyword]+=1
          else:
            alldata[keyword]=1
  alldata={word: rank for word, rank in sorted(alldata.items(), key=lambda item: item[1], reverse=True)}
  with open(outputfile, 'w') as f:
    json.dump(alldata,f)
  print(json.dumps(alldata))

if __name__=='__main__':
  if len(sys.argv) < 3:
    print('Usage: python gen_ranking_file <dirpath> <outputfile>')
    exit()
  dirpath=sys.argv[1]
  outputfile=sys.argv[2]
  sum_ranking(dirpath, outputfile)
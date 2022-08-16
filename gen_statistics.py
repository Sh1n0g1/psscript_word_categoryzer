import os
import csv
import json
alldata={}
for curdir,dirs,files in os.walk("output"):
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
print(json.dumps(alldata))

import sys
import os
import re

MINIMUM_LENGTH=3
MAXIMUM_LENGTH=20
DEBUG = True

def main(inputfilename):
  contents=get_contents(inputfilename)
  contents=contents.lower()
  wordlist=extract_words(contents)
  wordlist=filter_words_by_length(wordlist)
  wordranking={}
  for word in wordlist:
    if word in wordranking:
      wordranking[word]+=1
    else:
      wordranking[word]=1
  wordranking={word: rank for word, rank in sorted(wordranking.items(), key=lambda item: item[1], reverse=True)}
  for word in wordranking:
    print("%s,%s" % (word,wordranking[word]))

def get_contents(inputfilename):
  if not os.path.exists(inputfilename) or not os.path.isfile(inputfilename):
    print("File not found")
    return []
  with open(inputfilename,'r') as f:
    contents=f.read()
  return contents

def lowercase(contents):
  return contents.lower()

def extract_words(contents):
  return re.findall("\w+", contents)

def filter_words_by_length(wordlist):
  return [word for word in wordlist if len(word) >= MINIMUM_LENGTH and len(word) < MAXIMUM_LENGTH]


if __name__ == '__main__':
  if(len(sys.argv) < 2):
    print("Usage: python gen_ranking_file.py <input textfile> <output textfile>")
    exit()
  inputfilename=sys.argv[1]
  main(inputfilename)
  
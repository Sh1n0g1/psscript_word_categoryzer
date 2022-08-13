# PSScript Word Categoryzer
A small script to calculate and categorize the word inside the powershell script. 
The result can be used to create a black list of word from a malicious script or to be proccessed for Bayesian network

## Install
```git clone https://github.com/Sh1n0g1/psscript_word_categoryzer.git```

## How to use
```python gen_ranking_file.py <inputtextfile> <outputtextfile>```
* inputtextfile -> The PowerShell Script you want to process
* outputtextfile -> The file with the wordlist and its ranking

## Ranking Sample
This is the partial result of all built-in commandlet.
```
get,416
set,214
remove,131
new,105
enable,74
disable,71
add,65
start,26
update,26
export,25
```

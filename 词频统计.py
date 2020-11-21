f = open('C:/Users/12579/Desktop/txt.txt','r',encoding='utf-8')
line = f.read()
import re
line =line.lower()
line =re.sub('[,.?!]',' ',line)
words =line.split()
word = set(words)
dic={i:words.count(i) for i in word}
res=sorted(dic.items(),key=lambda  x:x[1],reverse=True)
print(res)
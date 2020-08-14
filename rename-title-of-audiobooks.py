from tinytag import TinyTag
import os
fileinput=input('Enter folder name:')
filenames=os.listdir(fileinput)
print(filenames)
n=0
for each in filenames:
  tag=TinyTag.get(fileinput+'/%s' %(each,))
  temp_title=(tag.title+'.mp3')
  os.rename(fileinput+'/%s' %each, fileinput+'/%s' %temp_title)
  n=n+1
  print('namechanged'+str(n))
print(filenames)

import os
import random
import dircache
import sys

os.system("ffmpeg -y -i saga.mp3 -qscale:v 1 intermediate_all.mpg")

zeros = os.listdir(".\\0")
ones = os.listdir(".\\1")
indexz = 0
indexo = 0

random.shuffle(zeros)
random.shuffle(ones)

with open("input.txt") as f:
  while True:
    c = f.read(1)
    if not c:
      print "End of file"
      break
    if "0" in c:
      os.system("ffmpeg -y -i ./0/" + zeros[indexz] + " -qscale:v 1 intermediate1.mpg")
      indexz += 1
      if indexz >= len(zeros):
        random.shuffle(zeros)
        indexz = 0
      os.system("copy /b intermediate_all.mpg+intermediate1.mpg intermediate_all.mpg")
    elif "1" in c:
      os.system("ffmpeg -y -i ./1/" + ones[indexo] + " -qscale:v 1 intermediate1.mpg")
      indexo += 1
      if indexo >= len(ones):
        random.shuffle(ones)
        indexo = 0
      os.system("copy /b intermediate_all.mpg+intermediate1.mpg intermediate_all.mpg")
    elif c.isspace():
      os.system("ffmpeg -y -i space.mp3 -qscale:v 1 intermediate1.mpg")
      os.system("copy /b intermediate_all.mpg+intermediate1.mpg intermediate_all.mpg")
    elif "\n" in c:
      os.system("ffmpeg -y -i pause.mp3 -qscale:v 1 intermediate1.mpg")
      os.system("copy /b intermediate_all.mpg+intermediate1.mpg intermediate_all.mpg")
    #print "Read a character:", c

os.system("ffmpeg -y -i intermediate_all.mpg -qscale:v 2 saga.avi");

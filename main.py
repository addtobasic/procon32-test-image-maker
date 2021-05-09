import numpy as np
import cv2
import os
import random

img = cv2.imread("testImage/procon_logo.png")

if not os.path.exists("./outImage"):
  os.mkdir("./outImage")

wSplitNum = 3
hSplitNum = 2

# 分割後の横の長さのpx
w_split_size = img.shape[1] // wSplitNum
# 分割後の縦の長さのpx
h_split_size = img.shape[0] // hSplitNum

w_size = img.shape[1] // w_split_size * w_split_size
h_size = img.shape[0] // h_split_size * h_split_size

img = img[:h_size, :w_size]

split_img = []
split_rot_img = []
comb_img = []

def splitImage(img, wsplitNum, hSplitNum):
  [split_img.extend(np.hsplit(h_img, wSplitNum)) for h_img in np.vsplit(img, hSplitNum)]
  count = 0
  for outImage in split_img:
    cv2.imwrite("./outImage/img-"+str(count)+".jpg",split_img[count])

    split_img[count] = np.rot90(split_img[count],random.randint(0,3))
    cv2.imwrite("./outImage/img_rot"+str(count)+".jpg",split_img[count])
    count += 1

  #配列の中身をシャッフル
  random.shuffle(split_img)

def combinationImage(split_img,comb_img, wsplitNum, hSplitNum):
  num = 0
  for num in range(hSplitNum):
    comb_img.append(np.hstack(split_img[wSplitNum*num:wSplitNum*(num+1)]))

  comb_img = np.vstack(comb_img)
  cv2.imwrite("./outImage/test.jpg",comb_img)


splitImage(img, wSplitNum, hSplitNum)
combinationImage(split_img, comb_img, wSplitNum, hSplitNum)

print(str(wSplitNum)+" "+str(hSplitNum))
print(str(w_size)+" "+str(h_size))

import numpy as np
import cv2
import os
img = cv2.imread("testImage/procon_logo.png")

wSplitNum = 3
hSplitNum = 3

# 分割後の横の長さのpx
w_split_size = img.shape[0] // wSplitNum

# 分割後の縦の長さのpx
h_split_size = img.shape[1] // hSplitNum

w_size = img.shape[0] // w_split_size * w_split_size
h_size = img.shape[1] // h_split_size * h_split_size

img = img[:w_size, :h_size]

split_img = []
[split_img.extend(np.hsplit(h_img, wSplitNum)) for h_img in np.vsplit(img, hSplitNum)]

num = 0
comb_img = []

for num in range(hSplitNum):
  comb_img.append(np.hstack(split_img[wSplitNum*num:wSplitNum*(num+1)]))

comb_img = np.vstack(comb_img)

if not os.path.exists("./outImage"):
  os.mkdir("./outImage")

cv2.imwrite("./outImage/test.jpg",comb_img)

count = 0
for outImage in split_img:
  cv2.imwrite("./outImage/img-"+str(count)+".jpg",split_img[count])
  count += 1

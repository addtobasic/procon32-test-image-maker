import numpy as np
import cv2
import os

img = cv2.imread("testImage/procon_logo.png")

wSplitNum = 2
hSplitNum = 2

# 分割後の横の長さのpx
w_split_size = img.shape[0] // wSplitNum

# 分割後の縦の長さのpx
h_split_size = img.shape[1] // hSplitNum

v_size = img.shape[0] // w_split_size * w_split_size
h_size = img.shape[1] // h_split_size * h_split_size

img = img[:v_size, :h_size]

out_img = []
[out_img.extend(np.hsplit(h_img, wSplitNum))
  for h_img in np.vsplit(img, hSplitNum)]

# shuffle = np.random.permutation(range(len(img)))
# img = np.vstack((
#     # np.hstack(img[shuffle[0:5]]),
#     # np.hstack(img[shuffle[5:10]]),
#     # np.hstack(img[shuffle[10:15]]),
# ))

# cv2.imwrite("./outImage/test.jpg",img)

if not os.path.exists("./outImage"):
  os.mkdir("./outImage")

count = 0
for outImage in out_img:
  cv2.imwrite("./outImage/img-"+str(count)+".jpg",out_img[count])
  count += 1

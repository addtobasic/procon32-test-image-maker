import numpy as np
import cv2

img = cv2.imread("testImage/procon_logo.png")
size = 32


v_size = img.shape[0] // size * size
h_size = img.shape[1] // size * size
img = img[:v_size, :h_size]
v_split = img.shape[0] // size
h_split = img.shape[1] // size
out_img = []
[out_img.extend(np.hsplit(h_img, h_split))
  for h_img in np.vsplit(img, v_split)]

shuffle = np.random.permutation(range(len(img)))
img = np.vstack((
    # np.hstack(img[shuffle[0:5]]),
    # np.hstack(img[shuffle[5:10]]),
    # np.hstack(img[shuffle[10:15]]),
))

# cv2.imwrite("./outImage/test.jpg",img)


count = 0
for outImage in out_img:
  cv2.imwrite("./outImage/img-"+str(count)+".jpg",out_img[count])
  count += 1

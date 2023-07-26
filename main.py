import cv2

src = cv2.imread("johnny.jpg")

# cv2.imshow("Mr. Depp", src)

# percentage by which image is resized
scale_percent = 50

# calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)  # numpy
height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

output = cv2.resize(src, dsize)

cv2.imwrite('newImage.jpg',output)  # here we can specify name and extension of resized image
cv2.waitKey(0)

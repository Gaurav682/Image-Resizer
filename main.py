import cv2

src = cv2.imread("johnny.jpg")  # Specify Name/Address of image

#use to show your image with a title(in quotes)
# cv2.imshow('Mr. Depp', src) 

# percentage by which image is resized
scale_percent = 25

# calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100) 
height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

output = cv2.resize(src, dsize)

cv2.imwrite('newImage.jpg',output)  # here we can specify name and extension of resized image
cv2.waitKey(0)

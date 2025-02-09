
import cv2

img = cv2.imread(r'stand.jpg',0)
print(img)
status = cv2.imwrite('standing.jpg',img)
print("Image written to file system : ", status)

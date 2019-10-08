import cv2

img = cv2.imread('lines3.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(img.copy(), contours, -1, (0, 255, 0), 2)
cv2.imshow("contours", img)
cv2.waitKey()
cv2.destroyAllWindows()

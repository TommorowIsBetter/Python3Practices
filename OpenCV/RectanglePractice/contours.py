import cv2

img = cv2.imread('c.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
del_index = []
new_list = []
for i in range(len(contours)):
    if len(contours[i]) != 4:
        del_index.append(i)
for i in range(len(contours)):
    if i not in del_index:
        new_list.append(contours[i])
lines_list = new_list.copy()
del del_index[:]
del new_list[:]
print(lines_list)
for i, count in zip(lines_list, range(len(lines_list))):
    if cv2.contourArea(i) < 200 or cv2.contourArea(i) > 20000:
        del_index.append(count)
for i in range(len(lines_list)):
    if i not in del_index:
        new_list.append(lines_list[i])
lines_list = new_list
img = cv2.drawContours(img, lines_list, -1, (0, 255, 0), 2)
cv2.imshow("contours", img)
cv2.waitKey()
cv2.destroyAllWindows()

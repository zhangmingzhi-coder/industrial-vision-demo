import cv2

img = cv2.imread("test.jpg")

h, w = img.shape[:2]
print("这张图 宽:", w, "高:", h)

cv2.imshow("origin", img)
cv2.rectangle(img, (w//5, h//5), (w//5*4, h//5*4), (0, 255, 0), 5)
cv2.putText(img, "TARGET", (w//5, h//5 - 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
cv2.imshow("boxed", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
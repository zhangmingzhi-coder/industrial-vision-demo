import cv2
import numpy as np

# 画布：一张 400x600 的黑色图
img = np.zeros((400, 600, 3), dtype=np.uint8)

# 绿框（以后=框出零件）
cv2.rectangle(img, (50, 50), (250, 250), (0, 255, 0), 3)

# 红色实心圆（以后=标出缺陷）
cv2.circle(img, (450, 150), 80, (0, 0, 255), -1)

# 写字
cv2.putText(img, 'Hello CV Demo', (150, 350),
            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2)

cv2.imshow('my first CV window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
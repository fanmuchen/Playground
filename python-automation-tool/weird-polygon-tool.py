import cv2
import numpy as np

# 读取图像
img = cv2.imread('image.jpg')

# 设置鼠标事件回调函数
def draw_polygon(event, x, y, flags, param):
    global polygon
    if event == cv2.EVENT_LBUTTONDOWN:
        polygon.append([x, y])
    elif event == cv2.EVENT_RBUTTONDOWN:
        polygon = np.array(polygon, np.int32)
        cv2.fillPoly(img, [polygon], (255, 255, 255))
        cv2.imshow('image', img)
        # 计算变换矩阵
        src_points = np.float32(polygon)
        dst_points = np.float32([[100, 100], [300, 100], [300, 300], [100, 300]])
        transform_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
        # 变换多边形
        transformed_polygon = cv2.warpPerspective(img, transform_matrix, (img.shape[1], img.shape[0]))
        cv2.imshow('transformed polygon', transformed_polygon)


# 初始化变量
polygon = []

# 显示图像并等待用户选取多边形

cv2.imshow('image', img)
cv2.setMouseCallback('image', draw_polygon)

cv2.waitKey(0)
cv2.destroyAllWindows()

print(polygon)

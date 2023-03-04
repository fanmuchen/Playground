import cv2
import numpy as np

# 读取图像
img = cv2.imread('image.jpg')

# 设置鼠标事件回调函数
import cv2
import numpy as np

# 读取图像
img = cv2.imread('image.jpg')

# 设置鼠标事件回调函数
def draw_polygon(event, x, y, flags, param):
    global polygon
    if event == cv2.EVENT_LBUTTONDOWN:  # 如果用户左键点击鼠标，则将当前坐标添加到polygon列表中
        polygon.append([x, y])
    elif event == cv2.EVENT_RBUTTONDOWN:  # 如果用户右键点击鼠标，则进行多边形截取操作
        polygon = np.array(polygon, np.int32)  # 将polygon列表转换为NumPy数组
        mask = np.zeros_like(img)  # 创建一个和原图像大小一样的全黑图像
        cv2.fillPoly(mask, [polygon], (255, 255, 255))  # 在mask图像上填充选定多边形的区域，填充的颜色为白色
        masked_img = cv2.bitwise_and(img, mask)  # 将原图像和mask图像进行逐像素相与，从而得到选定多边形的部分
        x, y, w, h = cv2.boundingRect(polygon)  # 计算多边形的外接矩形
        cropped_polygon = masked_img[y:y+h, x:x+w]  # 截取选定多边形的部分
        cv2.imshow('cropped polygon', cropped_polygon)  # 在窗口中显示截取的多边形

# 初始化变量
polygon = []

# 显示图像并等待用户选取多边形
cv2.imshow('image', img)
cv2.setMouseCallback('image', draw_polygon)

cv2.waitKey(0)  # 等待用户按下键盘上的任意键
cv2.destroyAllWindows()  # 关闭所有窗口并退出程序



# 初始化变量
polygon = []

# 显示图像并等待用户选取多边形
cv2.imshow('image', img)
cv2.setMouseCallback('image', draw_polygon)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

# 加载原始图像和模板图像
img = cv2.imread('img.png')
template = cv2.imread('template.png')


# 获得模板图像的高度和宽度
h, w = template.shape[:-1]

# 搜索模板图像在原始图像中的匹配位置
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

# 设置缩放和误差阈值
scale = 1  # 缩放因子
threshold = 0.9  # 匹配误差阈值

# 在匹配结果中查找位置
while True:
    # 查找匹配程度最高的位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val >= threshold:
        # 找到了匹配位置
        # 计算模板图像的缩放后大小
        new_h, new_w = int(h*scale), int(w*scale)
        # 根据缩放后的大小创建模板图像
        template_resized = cv2.resize(template, (new_w, new_h))
        # 在原始图像中找到模板图像的位置
        top_left = max_loc
        bottom_right = (top_left[0] + new_w, top_left[1] + new_h)
        # 画出匹配矩形
        cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)
        # 设置下一次搜索的区域为已找到的区域
        res[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = -1
    else:
        # 没有找到更多的匹配位置
        break

# 显示结果图像
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

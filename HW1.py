import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import local_binary_pattern
from collections import deque

# 讀取圖片
image_path = r'D:\Microsoft VS Code\python\row.jpg'
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 設定道路顏色的 HSV 範圍
lower_gray = np.array([0, 0, 50])  # 下界
upper_gray = np.array([180, 50, 200])  # 上界
road_mask = cv2.inRange(hsv_image, lower_gray, upper_gray)

# 計算 LBP 只針對道路區域
def compute_lbp(image, mask, P=8, R=1):
    lbp = local_binary_pattern(image, P, R, method='uniform')
    lbp = lbp * (mask // 255)  # 只保留道路區域的 LBP 值
    return lbp

lbp_image = compute_lbp(gray_image, road_mask)

# BFS 區域分割
def bfs_segment(image, start, visited):
    queue = deque([start])
    component = []
    while queue:
        x, y = queue.popleft()
        if (x < 0 or x >= image.shape[0] or y < 0 or y >= image.shape[1] or
            visited[x, y] or image[x, y] == 0):  # 邊界和訪問檢查
            continue
        visited[x, y] = True
        component.append((x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 4-連通
            queue.append((x + dx, y + dy))
    return component

# 建立遮罩和訪問記錄
_, mask = cv2.threshold(lbp_image.astype(np.uint8), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
visited = np.zeros(mask.shape, dtype=bool)
segments = []

# 對未訪問過的道路像素執行 BFS
for i in range(mask.shape[0]):
    for j in range(mask.shape[1]):
        if road_mask[i, j] > 0 and mask[i, j] > 0 and not visited[i, j]:  # 只考慮道路部分
            component = bfs_segment(mask, (i, j), visited)
            segments.append(component)

# 將道路部分覆蓋綠色
overlay = image.copy()
alpha = 0.5
for segment in segments:
    color = [0, 0, 255]  # 紅色
    for x, y in segment:
        overlay[x, y] = color
cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

# 顯示原圖、LBP 圖片和最終處理結果
plt.figure(figsize=(15, 5))

# 原圖
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB))
plt.title('Original Image')

# LBP 圖像
plt.subplot(1, 3, 2)
plt.imshow(lbp_image, cmap='gray')
plt.title('LBP Image')

# 最終處理後的圖片
plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Final Image with Transparent Road Segments')

# 顯示三張圖片
plt.show()

# 保存結果
output_path = r'D:\Microsoft VS Code\python\row_corrected_segmented.jpg'
cv2.imwrite(output_path, image)

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 讀取圖片
image_path = r'D:\Microsoft VS Code\python\row.jpg'
image = cv2.imread(image_path)

# 將圖像轉換為 HSV 色彩空間 (用於篩選顏色)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 設定道路顏色的 HSV 範圍 (根據圖片中的道路顏色調整)
# 這裡假設道路是灰色，可以調整這些範圍來匹配圖片中的道路顏色
lower_gray = np.array([0, 0, 50])  # 下界
upper_gray = np.array([180, 50, 200])  # 上界

# 根據顏色範圍創建遮罩
mask = cv2.inRange(hsv_image, lower_gray, upper_gray)

# 顯示遮罩（僅顯示檢測出的道路部分）
plt.imshow(mask, cmap='gray')
plt.title('Detected Road Mask')
plt.show()

# 找到遮罩中的道路區域
road_area = np.where(mask == 255)

# 將道路部分塗成半透明
overlay = image.copy()
alpha = 0.5  # 透明度

# 設定道路區域為紅色 (或其他顏色)，並設置透明度
overlay[road_area] = [0, 0, 255]  # 紅色

# 將覆蓋層與原始圖像進行合併
cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

# 顯示結果
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Final Transparent Road Image')
plt.show()

# 保存處理後的圖片
output_path = r'D:\Microsoft VS Code\python\row_transparent_road_color.jpg'
cv2.imwrite(output_path, image)

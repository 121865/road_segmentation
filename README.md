# Embedded-Image-Processing
# 一、說明
input : 任一張直線道路+街景+天空的照片  
output : 區域塗上半透明
# 二、Breakdown
![image](https://github.com/user-attachments/assets/eddebc54-9633-41e5-abc7-1f797425bb6c)
# 三、流程圖
![image](https://github.com/user-attachments/assets/0d24253e-caf2-48a9-9230-1ce0b4458e6f)
# 四、程式說明
### 直方圖均衡化
```
equalized_gray = cv2.equalizeHist(gray_image)
```
### LBP
```
def compute_lbp(image, mask, P=8, R=2):
    lbp = local_binary_pattern(image, P, R, method='uniform')
    lbp = lbp * (mask // 255)  # 只保留道路區域的 LBP 值
    return lbp
```
P=16，R=2  
![road_final](https://github.com/user-attachments/assets/655dc894-a46e-4db6-af5b-13dfd43daaba)  
P=8，R=2  
![road_final_2](https://github.com/user-attachments/assets/5755dee6-030b-4ef9-a4e0-6af0ef0e8a16)  
### 找最大區域
在實作時發現圖片經HSV設定完馬路範圍與LBP處理後儘管不是只有馬路區域變成白色區域，但馬路範圍通常都是最大區域，所以取最大區域當作馬路。
```
# 尋找輪廓並保留最大區塊
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 找到最大輪廓
max_contour = max(contours, key=cv2.contourArea)
# 創建一個空白遮罩來保存最大區塊
filtered_mask = np.zeros_like(mask)
cv2.drawContours(filtered_mask, [max_contour], -1, 255, thickness=cv2.FILLED)
```
### 覆蓋顏色
```
overlay = image.copy()
alpha = 0.5
for x in range(filtered_mask.shape[0]):
    for y in range(filtered_mask.shape[1]):
        if filtered_mask[x, y] > 0:
            overlay[x, y] = [0, 0, 255]  # 紅色
output = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
```
# 五、成果
![image](https://github.com/user-attachments/assets/87b4c008-bce0-4ce8-b095-be56a900e204)
![image](https://github.com/user-attachments/assets/2f64efe3-308e-416f-9be5-e0467c668380)
![image](https://github.com/user-attachments/assets/98d5ef98-e6a3-4082-a721-205ea3885af5)
![image](https://github.com/user-attachments/assets/b4ffc7ab-0fc9-4851-b5cb-73b8af969bef)
# 六、參考資料
[二值化黑白影像](https://github.com/user-attachments/assets/f4601854-ad09-4cfd-8ac0-575a8ca5301b)
[二值化黑白影像](<https://github.com/user-attachments/assets/f4601854-ad09-4cfd-8ac0-575a8ca5301b>)
![image](https://github.com/user-attachments/assets/c9ae0dda-602c-40fe-833f-0024e3238ca4)






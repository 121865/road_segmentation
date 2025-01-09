# Embedded-Image-Processing
# 一、說明
input : 任一張直線道路+街景+天空的照片  
output : 區域塗上半透明
# 二、Breakdown
![image](https://github.com/user-attachments/assets/eddebc54-9633-41e5-abc7-1f797425bb6c)
# 三、流程圖
![image](https://github.com/user-attachments/assets/0d24253e-caf2-48a9-9230-1ce0b4458e6f)
# 四、API
![image](https://github.com/user-attachments/assets/8e6a9518-fb26-4617-b065-2f0c16a9717f)  
![image](https://github.com/user-attachments/assets/9421e76e-1a51-4fa0-a7fc-f5616c010ec1)  
![image](https://github.com/user-attachments/assets/e2985f54-a196-46b5-a22f-2aa3805b6297)  
![image](https://github.com/user-attachments/assets/7813e181-9b3a-4c1c-ad27-62509c93f2c4)

# 五、程式說明
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
# 六、成果
影片連結 : <https://youtu.be/3txH2h8slcw>  
![image](https://github.com/user-attachments/assets/87b4c008-bce0-4ce8-b095-be56a900e204)
![image](https://github.com/user-attachments/assets/2f64efe3-308e-416f-9be5-e0467c668380)
![image](https://github.com/user-attachments/assets/98d5ef98-e6a3-4082-a721-205ea3885af5)
![image](https://github.com/user-attachments/assets/b4ffc7ab-0fc9-4851-b5cb-73b8af969bef)
# 七、參考資料
<https://steam.oxxostudio.tw/category/python/ai/opencv-threshold.html>  
<https://ithelp.ithome.com.tw/articles/10269771?sc=rss.iron>  
<https://vocus.cc/article/66feaaeafd897800013da017>  
<https://ithelp.ithome.com.tw/articles/10323537?sc=rss.iron>  
<https://ithelp.ithome.com.tw/m/articles/10323301>





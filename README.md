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
原本設定P=16，R=2，但部分圖像顯示結果並不理想，所以更改為P=8，R=2  
![road_final](https://github.com/user-attachments/assets/655dc894-a46e-4db6-af5b-13dfd43daaba)
![road_final_2](https://github.com/user-attachments/assets/5755dee6-030b-4ef9-a4e0-6af0ef0e8a16)




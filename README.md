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



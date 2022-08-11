# SBG-N-detection-Cascade-Classifier


在本練習中，我們參考[1]，先利用攝像鏡頭捕捉 SBG-N GNSS&IMU 模組的positive image，建立positive 圖庫後，我們將SBG-N 移除目標環境，將目標環境也做拍攝捕捉negative image (background image)，之後透過Cascade Trainger GUI 來訓練Cascade Classifier，最後將訓練好的 Cascade Classifier來判斷桌面上的SBG-N 模組是否存在與位置。 

![image](https://user-images.githubusercontent.com/108604868/183280674-99897efd-db08-4811-b028-4dffa6693bb4.png)





Cascade Trainger GUI 


Negative Image Count 173

Number of Stages 15

Sample Width 36

# Reference
[1] https://www.youtube.com/watch?v=dZ4itBvIjVY

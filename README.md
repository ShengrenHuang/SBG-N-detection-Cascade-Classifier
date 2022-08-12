# SBG-N-detection-Cascade-Classifier

Inspired by [1], we aim to create a cascade classifier to detect something different in this practice. We select a GNSS and IMU integrated module, SBG-N, as our detection object. Using the webcam, we capture the different angles of the SBG-N to gather positive images. Meanwhile, we collect some frames without SBG-N to be our negative images. Then we employ Cascade Trainer GUI based on Opencv [2] to train our cascade classifier with the following parameters:
1. Number of Stages 15
2. Sample Width 36.  

The result shows that the performance of the classifier is pretty well. 




![image](https://user-images.githubusercontent.com/108604868/183280674-99897efd-db08-4811-b028-4dffa6693bb4.png)




https://user-images.githubusercontent.com/108604868/184277194-84e23704-0432-48d6-8f3f-8fb7335d14af.mp4





# Reference
[1] https://www.youtube.com/watch?v=dZ4itBvIjVY
[2] https://amin-ahmadi.com/cascade-trainer-gui/

### 🐶🐱Cats vs. Dogs Classification Project
---

![alt text](/demo/miscellaneous/Cats-Dogs-Classification-deep-learning.gif)

### 📄Description
---
* In this project, we are going to classify cats and dogs using deep learning models.
* The project is done using two models.
* One model is a `Convolutional Neural Network(CNN)` that is written from scratch.
* Another model is a pre-trained model based on `MobileNetV2` architecture.
* Project implementations can be accessed in `scripts` folder.
* Models can be accessed in `models` folder.

### 📕Model's Output
---
In this section you can see the outputs of both models:
#### CNN's Output
---
![alt text](/demo/results/cnn/result-01.png)
![alt text](/demo/results/cnn/result-03.png)

#### MobileNetV2's Output
---
![alt text](/demo/results/mobilenetv2/result-01.png)
![alt text](/demo/results/mobilenetv2/result-03.png)

### 📈📉📊Model Performance
---
* This two models has a reasonably good performance.
* The CNN model has reached above `90%` accuracy.
* The pre-trained model based on `MoobileNetV2` architecture has reached above `97%` accuracy.
* If you are interested in further details you can access them by `demo/performance` directory.

### 🎫 Dataset
---
You can access the dataset via this [link](https://www.kaggle.com/c/dogs-vs-cats).The data is zipped, and you have to unzip it.After unzipping, you have to serialize the image data into `pickle` format.For pickling files you have to run `creating_data.py` that is placed in `preprocessing` folder.The pickle file contains `100x100` grayscale images and it is used for `CNN` model.

For pre-trained model we randomly picked `1000` samples of each class and then convert them into `227x227` images and preprocessed them to feed them into the pre-trained model.

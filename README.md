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

### 📕Output
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
You can access the dataset via this [link](https://www.kaggle.com/c/dogs-vs-cats).The data is zipped, and you have to unzip it.After unzipping, you can see that the main folder is now contains two subfolers, `Cat` and `Dog`. Each folder is a representative of each class for our data and each of them contains `~12000` samples.
In the next step, you have to serialize the data into `pickle` format. For pickling files you have to run `creating_data.py` that is placed in `preprocessing` folder. The pickle file is now contains `100x100` grayscale images and it is used for `CNN` model.

For pre-trained model we randomly picked `1000` samples of each class and then convert them into `227x227` images and preprocessed them to feed them into the pre-trained model.

### 💻🖥Installation
---
## 🛠Requirements
| Module/Framework        | Version           |
| ----------------------- |:-----------------:|
| tensorflow              | 2.4.1             |
| keras                   | 2.5.0             |
| sci-kit learn           | 0.22.2.post1      |
| seaborn                 | 0.11.1            |
| pandas                  | 1.1.5             |
| numpy                   | 1.19.5            |
| cv2                     | 4.1.2             |
| PIL                     | 7.1.2             |
| matplotlib              | 3.2.2             |
| imutils                 | 0.5.4             |

### ⚙Setup
---
Tensorflow:
```
$ pip install tensorflow==2.4.1
```
keras:
```
$ pip install keras==2.5.0
```
Scikit-learn:
```
$ pip install scikit-learn==0.22.2.post1
```
Seaborn:
```
$ pip install seaborn==0.11.1
```
Pandas:
```
$ pip install pandas==1.1.5 
```
Numpy:
```
$ pip install numpy==1.19.5
```
CV2:
```
$ pip install cv2==4.1.2 
```
PIL:
```
$ pip install PIL==7.1.2
```
Matplotlib:
```
$ pip install matplotlib==3.2.2 
```
Imutils:
```
$ pip install imutils==0.5.4
```
### 👥Contributers
---
Kasra1377

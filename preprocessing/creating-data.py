import os
import cv2
import numpy as np
import pickle
from sklearn.utils import shuffle
img_size = 100

categories = ["Cat" , "Dog"]
dataDir = r"E:/Datasets/PetImages"
training_data = []

def create_data():
  for i in categories:
    path = os.path.join(dataDir , i)
    class_num = categories.index(i)
    for img in os.listdir(path):
      try:
        img_array = cv2.imread(os.path.join(path , img) , cv2.IMREAD_GRAYSCALE)
        new_array = cv2.resize(img_array , (img_size , img_size))
        training_data.append([new_array , class_num])
      except Exception as e:
        pass

create_data()

print("The length of training data is : " , len(training_data))
shuffle(training_data)

X = []
y = []

for features , label in training_data:
  X.append(features)
  y.append(label)

X = np.array(X).reshape(-1 , img_size , img_size , 1)
y = np.array(y)

pickle_out = open(r"E:/Datasets/PetImages/X.pickle" , "wb")
pickle.dump(X , pickle_out)
pickle_out.close()

pickle_out = open(r"E:/Datasets/PetImages/y.pickle" , "wb")
pickle.dump(y , pickle_out)
pickle_out.close()

print("The shape of X is : " , X.shape)
print("The shape of y is : " , y.shape)


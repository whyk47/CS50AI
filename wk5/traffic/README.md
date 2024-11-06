# Traffic Sign Classification 

[video demo](https://youtu.be/5NJEkPIYT2U)

### Overview
This project involves building an AI model to classify traffic signs from images using deep learning. The AI uses a Convolutional Neural Network (CNN) to predict which traffic sign appears in a photograph. The project will involve training multiple neural networks using TensorFlow and evaluating their performance on a testing dataset.

### Usage
1. Download and unzip the [GTSRB dataset](https://cdn.cs50.net/ai/2020/x/projects/5/gtsrb.zip), placing it in the traffic directory.
2. Install the project dependencies.
```bash
$ pip install -r requirements.txt
```
3. Run the script with the following command:
```bash
python traffic.py gtsrb
```
4. Optionally, specify a filename to save the trained model:
```bash
python traffic.py gtsrb model.h5
```

### Experimentation and Model Tuning
- Convolutional Layers: Experiment with different numbers and sizes of filters.
- Pooling Layers: Try different pooling strategies like max pooling and average pooling.
- Fully Connected Layers: Add one or more hidden layers and experiment with their size.
- Dropout: Introduce dropout layers to avoid overfitting.
- Learning Rate: Experiment with different learning rates and optimizers.

### Overview of results: 
- Models with 1 hidden, 2 convolutional and pooling layers seem to give the highest accuracy on the test set. 
- Number of layers has the biggest impact on accuracy of around 0.03. 
- Optimal Pool size seems to have little impact on the model accuracy. 
- Optimal kernel sizes -- one (4, 4) and one (3, 3) -- seem to improve accuracy slightly by around 0.01. 
- Optimal dropout (0.5) improves accuracy by around 0.01

### Models tried:
```python
Conv2D(filters=32, kernel_size=(3,3))
MaxPool2D(pool_size=(2, 2))
Conv2D(filters=64, kernel_size=(3,3))
MaxPool2D(pool_size=(2, 2))
Flatten()
Dense(units=128)
Dropout(0.5)
# loss: 0.1239 - accuracy: 0.9589
# loss: 0.0476 - accuracy: 0.9890


Conv2D(filters=32, kernel_size=(3,3))
MaxPool2D(pool_size=(2, 2))
Flatten()
Dense(units=128)
# loss: 0.4335 - accuracy: 0.8580
# loss: 0.1708 - accuracy: 0.9566


Conv2D(filters=32, kernel_size=(3,3))
MaxPool2D(pool_size=(2, 2))
Flatten()
Dense(units=128)
Dropout(0.5),
# loss: 0.0418 - accuracy: 0.9904
# loss: 0.1715 - accuracy: 0.9585


Conv2D(filters=32, kernel_size=(3,3))
MaxPool2D(pool_size=(2, 2))
Conv2D(filters=64, kernel_size=(3,3))
MaxPool2D(pool_size=(2, 2))
Flatten()
Dense(units=128)
Dropout(0.5)
Dense(units=128)
Dropout(0.5)
# loss: 0.7328 - accuracy: 0.7575
# loss: 0.2902 - accuracy: 0.9455 


Conv2D(filters=32, kernel_size=(3,3))
MaxPool2D(pool_size=(2, 2))
Conv2D(filters=64, kernel_size=(3,3))
MaxPool2D(pool_size=(2, 2))
Flatten()
Dense(units=64)
Dropout(0.5)
# loss: 0.9825 - accuracy: 0.6529
# loss: 0.3013 - accuracy: 0.9438


Conv2D(filters=32, kernel_size=(4,4))
MaxPool2D(pool_size=(2, 2))
Conv2D(filters=64, kernel_size=(3,3))
MaxPool2D(pool_size=(2, 2))
Flatten()
Dense(units=128)
Dropout(0.5)
# loss: 0.1125 - accuracy: 0.9644
# loss: 0.0381 - accuracy: 0.9916


Conv2D(filters=32, kernel_size=(3,3))
MaxPool2D(pool_size=(3, 3))
Conv2D(filters=64, kernel_size=(3,3))
MaxPool2D(pool_size=(2, 2))
Flatten()
Dense(units=128)
Dropout(0.5)
# loss: 0.1516 - accuracy: 0.9513
# loss: 0.0451 - accuracy: 0.9904 


Conv2D(filters=32, kernel_size=(4,4))
MaxPool2D(pool_size=(2, 2))
Conv2D(filters=64, kernel_size=(3,3))
MaxPool2D(pool_size=(2, 2))
Flatten()
Dense(units=128)
Dropout(0.3)
# loss: 0.1129 - accuracy: 0.9622
# loss: 0.0490 - accuracy: 0.9882

Conv2D(filters=32, kernel_size=(4,4))
MaxPool2D(pool_size=(2, 2))
Conv2D(filters=64, kernel_size=(3,3))
MaxPool2D(pool_size=(2, 2))
Flatten()
Dense(units=256)
Dropout(0.5)
# loss: 0.0801 - accuracy: 0.9762
# loss: 0.0669 - accuracy: 0.9858

Conv2D(filters=32, kernel_size=(4,4))
MaxPool2D(pool_size=(2, 2))
Conv2D(filters=64, kernel_size=(4 ,4))
MaxPool2D(pool_size=(2, 2))
Flatten()
Dense(units=128)
Dropout(0.5)
# loss: 0.1062 - accuracy: 0.9663
# loss: 0.0632 - accuracy: 0.9857

Conv2D(filters=32, kernel_size=(4,4))
MaxPool2D(pool_size=(2, 2))
Conv2D(filters=64, kernel_size=(3,3))
MaxPool2D(pool_size=(2, 2))
Conv2D(filters=64, kernel_size=(3,3))
MaxPool2D(pool_size=(2, 2))
Flatten()
Dense(units=128)
Dropout(0.5)
# loss: 0.0811 - accuracy: 0.9735
# loss: 0.0578 - accuracy: 0.9855
```
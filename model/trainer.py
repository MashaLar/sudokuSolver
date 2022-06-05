# trainer.py file
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.datasets import mnist
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report
from builder import Model
import argparse

INITIAL_LEARNING_RATE = 1e-3
EPOCHS = 10
BATCH_SIZE = 128
WH = 28 # width, height

def data_lables():
    ((dataSet, labelsSet), (data, labels)) = mnist.load_data()
    
    (dataSet, data) = data_train_test(dataSet, data)
    
    binarizer = LabelBinarizer()
    (labelsSet, labels) = labels_train_test(labelsSet, labels, binarizer)
    
    return (dataSet, labelsSet, data, labels, binarizer)

def model_setup():
    print("[INFO] CREATING MODEL...")
    optimizer = Adam(learning_rate=INITIAL_LEARNING_RATE)
    model = Model.build(width=WH, height=WH, depth=1, classes=10)
    model.compile(loss="categorical_crossentropy", optimizer=optimizer, metrics=["accuracy"])
    return (model)
   
def data_train_test(dataSet, data):
    dataSet = dataSet.reshape((dataSet.shape[0], WH, WH, 1))
    data = data.reshape((data.shape[0], WH, WH, 1))
    dataSet = dataSet.astype("float32") / 255.0
    data = data.astype("float32") / 255.0
    return (dataSet, data)
   
def labels_train_test(labelsSet, data, labelBinarizer):
    labelsSet = labelBinarizer.fit_transform(labelsSet)
    data = labelBinarizer.transform(data)
    return (labelsSet, data)

(dataSet, labelsSet, data, labels, binarizer) = data_lables()
model = model_setup()

print("[INFO] LEARN ON MNIST DATASET...")
H = model.fit(dataSet, labelsSet, validation_data=(data, labels), batch_size=BATCH_SIZE, epochs=EPOCHS, verbose=1)
    
print("[INFO] CHECK LEARNING...")
predictions = model.predict(data)
print(classification_report(
	labels.argmax(axis=1),
	predictions.argmax(axis=1),
	target_names=[str(n) for n in binarizer.classes_]))
    
print("[INFO] LOAD INTO FILE...")
model.save("./model/output/MODEL.h5", save_format="h5")
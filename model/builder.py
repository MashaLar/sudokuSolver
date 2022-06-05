# builder.py file
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout

class Model:
    @staticmethod
    def set_relu(model):
        model.add(Dense(64))
        model.add(Activation("relu"))
        model.add(Dropout(0.5))
    
    @staticmethod     
    def set_pool(model):
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))
    
    @staticmethod
    def build(width, height, depth, classes):
        model = Sequential()
        
        model.add(Conv2D(32, (5, 5), padding="same", input_shape=(height, width, depth)))
        Model.set_pool(model)
        model.add(Conv2D(32, (3, 3), padding="same"))
        Model.set_pool(model)
        
        model.add(Flatten())
        Model.set_relu(model)
        Model.set_relu(model)
        
        model.add(Dense(classes))
        model.add(Activation("softmax"))
        
        return model
        
   
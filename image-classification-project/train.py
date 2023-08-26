import tensorflow as tf
from model import create_model
from dataset import load_dataset

#load and preprocess the dataset
(train_images, train_labels), (test_images, test_labels) = load_dataset()

model = create_model()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#Train model
model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

model.save_weights('model_weights.h5')
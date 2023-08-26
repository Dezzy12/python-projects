import tensorflow as tf

def load_dataset():
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.cifar10.load_data()
    train_images = train_images / 255.0
    test_images = test_images / 255.0
    
    return (train_images, train_labels), (test_images, test_labels)



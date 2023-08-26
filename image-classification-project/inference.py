import numpy as np
from dataset import load_dataset
from model import create_model
import cv2 as cv

#load and preprocess the dataset
(_, _), (test_images, test_labels) = load_dataset()

test_image_index = 0
test_image = test_images[test_image_index]
test_label = test_labels[test_image_index]

#Reshape and preprocess the test image
test_image = np.expand_dims(test_image, axis=0)
test_image = test_image / 255.0

model = create_model()
model.load_weights('model_weights.h5')

#Initialize video capture
capture = cv.VideoCapture(0)

classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

while True:
    ret, frame = capture.read()

    resized_frame = cv.resize(frame, (32, 32))
    normalized_frame = resized_frame / 255.0
    test_image = np.expand_dims(normalized_frame, axis=0)

    #Prediction
    predictions = model.predict(test_image)
    predicted_label = np.argmax(predictions[0])

    print("True Label:", test_label)
    print("Predicted Label:", predicted_label)

    predicted_label = classes[predicted_label]

    # Display the predicted label on the frame
    predicted_label_str = str(predicted_label)
    cv.putText(frame, predicted_label_str, (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv.imshow('Object Recognition', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv.destroyAllWindows()
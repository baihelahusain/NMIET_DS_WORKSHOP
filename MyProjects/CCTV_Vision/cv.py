import cv2
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('vandalism_detection_model.h5')

# Connect to phone camera
cap = cv2.VideoCapture('http://<your-phone-ip>:8080/video')  # Replace with your IP

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Preprocess frame
    resized_frame = cv2.resize(frame, (224, 224))
    normalized_frame = resized_frame / 255.0
    input_frame = np.expand_dims(normalized_frame, axis=0)
    
    # Predict
    prediction = model.predict(input_frame)
    class_idx = np.argmax(prediction)
    confidence = np.max(prediction)
    
    # Trigger alarm if confidence > 90%
    if class_idx == 0 and confidence > 0.9:  # Class 0 = "vandalism"
        print("ALARM: Vandalism detected!")
        # Add alarm sound or notification here
    
    # Display frame
    cv2.imshow('CCTV Feed', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

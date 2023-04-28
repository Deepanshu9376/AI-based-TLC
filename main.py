import cv2
import time

# Load pre-trained vehicle detection classifier
car_cascade = cv2.CascadeClassifier('cars.xml')

for i in range(2):
    cap=cv2.VideoCapture(0)

    if not cap.isOpened():
        raise IOError("Unable to open web camera")

    ret,frame = cap.read()
    cap.release()
    cv2.imwrite("capturedimage.jpg",frame)
    print("Image Captured Successfully")

    # Read image
    img = cv2.imread('capturedimage.jpg')
        
    # Convert image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        # Detect vehicles in the image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

        # Draw bounding boxes around detected vehicles
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Count the number of detected vehicles
    count = len(cars)

        # Display the image with bounding boxes
    cv2.imshow('image', img)
    cv2.destroyAllWindows()
    cv2.waitKey(0)

        # Print the number of detected vehicles
    print("Number of vehicles detected:",count)
    if count > 1:
        timer = 3
        while timer >= 0:
            print(f"Stop {timer} seconds...")
            time.sleep(1)
            timer -= 1
            
#************************************************************************************************************************************************#

    cap=cv2.VideoCapture(0)

    if not cap.isOpened():
        raise IOError("Unable to open web camera")

    ret,frame1 = cap.read()
    cap.release()
    cv2.imwrite("capturedimage2.jpg",frame1)
    print("Image 2 Captured Successfully")

    # Read image
    img1 = cv2.imread('capturedimage2.jpg')
        
    # Convert image to grayscale
    gray = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

        # Detect vehicles in the image
    cars1 = car_cascade.detectMultiScale(gray, 1.1, 1)

        # Draw bounding boxes around detected vehicles
    for (x, y, w, h) in cars1:
        cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Count the number of detected vehicles
    count1 = len(cars1)

        # Display the image with bounding boxes
    cv2.imshow('image', img1)
    cv2.destroyAllWindows()
    cv2.waitKey(0)

        # Print the number of detected vehicles
    print("Number of vehicles detected:",count1)
    if count1 > 1:
        timer1 = 3
        while timer1 >= 0:
            print(f"Stop {timer1} seconds...")
            time.sleep(1)
            timer1 -= 1
##cv2.imwrite('randimg2.jpg', img)
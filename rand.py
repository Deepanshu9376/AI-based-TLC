import cv2
import time

# Load pre-trained vehicle detection classifier
car_cascade = cv2.CascadeClassifier('cars.xml')

for i in range(0,5):

# Read image
    img = cv2.imread('1.jpg')
    
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
    cv2.waitKey(1)

    # Print the number of detected vehicles
    print("Number of vehicles detected:",count)
    if count > 1:
        timer = 5
        while timer >= 0:
            print(f"Stop in {timer} seconds...")
            time.sleep(1)
            timer -= 1

    
#################################################################################################2

    img = cv2.imread('2.jpg')

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
    cv2.waitKey(1)

    

    # Print the number of detected vehicles
    print("Number of vehicles detected:",count)

    if count > 1:
        timer = 3
        while timer >= 0:
            print(f"Stop {timer} seconds...")
            time.sleep(1)
            timer -= 1

    
#################################################################################################3

#     img = cv2.imread('random.jpg')

#     # Convert image to grayscale
#     gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#     # Detect vehicles in the image
#     cars = car_cascade.detectMultiScale(gray, 1.1, 1)

#     # Draw bounding boxes around detected vehicles
#     for (x, y, w, h) in cars:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

#     # Count the number of detected vehicles
#     count = len(cars)

#     # Display the image with bounding boxes
#     cv2.imshow('image', img)
#     cv2.destroyAllWindows()
#     cv2.waitKey(1)

    

#     # Print the number of detected vehicles
#     print("Number of vehicles detected:",count)

#     if count > 1:
#         timer = 3
#         while timer >= 0:
#             print(f"Stop {timer} seconds...")
#             time.sleep(1)
#             timer -= 1
            
#     cv2.imwrite('5.jpg', img)

# #######################################################################################4

#     img = cv2.imread('5.jpg')

#     # Convert image to grayscale
#     gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#     # Detect vehicles in the image
#     cars = car_cascade.detectMultiScale(gray, 1.1, 1)

#     # Draw bounding boxes around detected vehicles
#     for (x, y, w, h) in cars:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

#     # Count the number of detected vehicles
#     count = len(cars)

#     # Display the image with bounding boxes
#     cv2.imshow('image', img)
#     cv2.destroyAllWindows()
#     cv2.waitKey(1)

    

#     # Print the number of detected vehicles
#     print("Number of vehicles detected:",count)

#     if count > 1:
#         timer = 3
#         while timer >= 0:
#             print(f"Stop {timer} seconds...")
#             time.sleep(1)
#             timer -= 1
            
#     cv2.imwrite('randimg.jpg', img)


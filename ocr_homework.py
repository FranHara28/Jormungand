import cv2
import pytesseract


# Function to add border boxes around each letter and print it
def add_boxes_using_image_to_boxes(image_path):

    image = cv2.imread(image_path)
    h, w, _ = image.shape   # get the shape of the image

    custom_config = r'--oem 3 --psm 6'  # add custom config for pytesseract

    boxes = pytesseract.image_to_boxes(image)   # get bounding boxes

    for b in boxes.splitlines():
        b = b.split(' ')
        x, y, x2, y2 = int(b[1]), int(b[2]), int(b[3]), int(b[4])   # get the box coordinates

        cv2.rectangle(image, (x, h - y), (x2, h - y2), (0, 255, 0), 2)  # draw a rectangle around each letter
        letter = b[0]   # extract the letter
        cv2.putText(image, letter, (x, h - y - 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)  # print the letter above the border box

    # Print the writing in the image to string
    print(pytesseract.image_to_string(image, config=custom_config))

    # Display the resulting image
    cv2.imshow('Result', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


add_boxes_using_image_to_boxes('umbc_address.png')  # call the function
# Made by: Fran Haraminčić

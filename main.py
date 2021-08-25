print('This is a opencv project created by Abhishek raj ')
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # To avoid the warning and log message
from utlis import *
import sudukoSolver


pathImage = "Resources/1.jpeg" # path of image
heightImg = 450
widthImg = 450
model = intializePredectionModel()  # LOAD THE CNN MODEL


#### 1. Preprocessing of the image
img = cv2.imread(pathImage) # imread method is used to read the input image
img = cv2.resize(img, (widthImg, heightImg))  # Resize yhe image and make it as square because sudoku is 9*9 matrix
imgBlank = np.zeros((heightImg, widthImg, 3), np.uint8)  # create a blank image for testing and debugging of image
imgThreshold = preProcess(img) # preprocessing the image where u have to convert it into grayscale so that we can find countour easily

# 2. Find All the Countour i.e contours are a useful tool for shape analysis and object detection
imgContours = img.copy() # we are going to copy that image for displaying image
imgBigContour = img.copy() # we are going to copy that image for displaying image
contours, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # find all the contours
cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 3) # actually it will draw all the contours

# 3.find the biggest contours which u can consider as sudoku
biggest, maxArea = biggestContour(contours) # Find the biggest contours
print(biggest)
if biggest.size != 0:
    biggest = reorder(biggest) # when we are checking for differnt image their width and height order changes
    print(biggest)
    cv2.drawContours(imgBigContour, biggest, -1, (0, 0, 255), 25) # Draw the biggest contours
    pts1 = np.float32(biggest) #prepare the point for warp perspective
    pts2 = np.float32([[0, 0],[widthImg, 0], [0, heightImg],[widthImg, heightImg]]) # prepare the poin for wrap
    matrix = cv2.getPerspectiveTransform(pts1, pts2) # GER
    imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
    imgDetectedDigits = imgBlank.copy() # take the image of black image
    imgWarpColored = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY) # It will convert into greyscale

    # 4. Split the image and find each digit available
    imgSolvedDigits = imgBlank.copy() # It will take blank image
    boxes = splitBoxes(imgWarpColored)
    print(len(boxes))
    numbers = getPredection(boxes, model)
    print(numbers)
    imgDetectedDigits = displayNumbers(imgDetectedDigits, numbers, color=(255, 0, 255))
    numbers = np.asarray(numbers)
    posArray = np.where(numbers > 0, 0, 1)
    print(posArray)


    # 5. Find the solution of board
    board = np.array_split(numbers,9)
    print(board)
    try:
        sudukoSolver.solve(board)
    except:
        pass
    print(board)
    flatList = []
    for sublist in board:
        for item in sublist:
            flatList.append(item)
    solvedNumbers =flatList*posArray
    imgSolvedDigits= displayNumbers(imgSolvedDigits,solvedNumbers)

    # 6. Solution
    pts2 = np.float32(biggest) # PREPARE POINTS FOR WARP
    pts1 =  np.float32([[0, 0],[widthImg, 0], [0, heightImg],[widthImg, heightImg]]) # PREPARE POINTS FOR WARP
    matrix = cv2.getPerspectiveTransform(pts1, pts2)  # GER
    imgInvWarpColored = img.copy()
    imgInvWarpColored = cv2.warpPerspective(imgSolvedDigits, matrix, (widthImg, heightImg))
    inv_perspective = cv2.addWeighted(imgInvWarpColored, 1, img, 0.5, 1)
    imgDetectedDigits = drawGrid(imgDetectedDigits)
    imgSolvedDigits = drawGrid(imgSolvedDigits)

    imageArray = ([img,imgThreshold,imgContours, imgBigContour],
                  [imgDetectedDigits, imgSolvedDigits,imgInvWarpColored,inv_perspective])
    stackedImage = stackImages(imageArray, 1)
    cv2.imshow('Final Stacked Image created by Abhishek Raj', stackedImage)

else:
    print("No Sudoku Found")

cv2.waitKey(0)

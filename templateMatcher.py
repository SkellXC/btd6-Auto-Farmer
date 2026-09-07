import cv2
import numpy as np
import pyautogui

def getRoundNumber():
    collectedNumbers = []
    numberImages = [r"images/zero.png",r"images/one.png",r"images/two.png",
                    r"images/three.png",r"images/four.png",r"images/five.png",
                    r"images/six.png",r"images/seven.png",r"images/eight.png",
                    r"images/nine.png"
                    ]

    # Take screenshot and crop to round number area
    screenshot = pyautogui.screenshot()
    round = 0
    toprx = 1434   
    topry = 30   
    width = 128
    height = 42
    screenshot = screenshot.crop((
        toprx,
        topry,
        toprx+width,
        topry+height
    ))

    # Convert screenshot to grayscale
    values = np.array(screenshot)
    img_gray = cv2.cvtColor(values, cv2.COLOR_RGB2GRAY)

    for n in range(0,10):
        x_coord = None
        template = cv2.imread(numberImages[n], cv2.IMREAD_GRAYSCALE)
        print(numberImages[n])
        h, w = template.shape[:2]
        # Convert template to grayscale

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        # Run template match

        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            x_coord = int(pt[0])
            # Gets the x-coordinate to get the numbers position

            # cv2.rectangle(values, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
            # Draws a rectangle on each found number and displays it

        if x_coord:
            foundNumber = (n,x_coord)
            collectedNumbers.append(foundNumber)

    """
        cv2.imshow('Detected',values)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()
    """

    collectedNumbers = sorted(
        collectedNumbers,
        key = lambda x: x[1]
    )

    result = [n[0] for n in collectedNumbers]
    result = int("".join(str(num) for num in result))
    # print(result)
    return result

print(getRoundNumber())
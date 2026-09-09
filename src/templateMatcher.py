import cv2
import numpy as np
import pyautogui

def getRoundNumber(totalRounds) -> int:
    collectedNumbers = []
    numberImages = [r"images/zero.png",r"images/one.png",r"images/two.png",
                    r"images/three.png",r"images/four.png",r"images/five.png",
                    r"images/six.png",r"images/seven.png",r"images/eight.png",
                    r"images/nine.png"
                    ]

    # Take screenshot and crop to round number area
    screenshot = pyautogui.screenshot()
    round = 0
    toprx = 1430   
    topry = 30   
    width = 130
    height = 42
    screenshot = screenshot.crop((
        toprx,
        topry,
        toprx+width,
        topry+height
    ))
    #screenshot.show()

    # Convert screenshot to grayscale
    values = np.array(screenshot)
    img_gray = cv2.cvtColor(values, cv2.COLOR_RGB2GRAY)
    #_, img_gray_bw = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)

    for n in range(0,10):
        x_coord = None
        template = cv2.imread(numberImages[n], cv2.IMREAD_GRAYSCALE)
        #_, template_bw = cv2.threshold(template, 200, 255, cv2.THRESH_BINARY)
        # print(numberImages[n])
        h, w = template.shape[:2]
        # Convert template to grayscale

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        # Run template match

        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            x_coord = int(pt[0])
            
            # 5-pixel proximity filter
            is_duplicate = False
            for existing_match in collectedNumbers:
                if abs(existing_match[1] - x_coord) < 5:
                    is_duplicate = True
                    break
            
            if not is_duplicate:
                foundNumber = (n, x_coord)
                collectedNumbers.append(foundNumber)
                cv2.rectangle(values, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        

        """cv2.imshow('Detected',values)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()"""
    

    collectedNumbers = sorted(
        collectedNumbers,
        key = lambda x: x[1]
    )

    result = [n[0] for n in collectedNumbers]
    
    result = ("".join(str(num) for num in result))
    if totalRounds < 100:
        result = result[:-2]
    else:
        result = result[:-3]

    try:
        result = int(result)
        return result
    except:
        print("Error! Unable to read a round number")
        return -1
    



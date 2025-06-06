import cv2
import numpy as np
from PIL import ImageGrab

import Constants.constantsScreenshot as constants

def locateTemplateOnScreen(region, targetImage):
    '''
    Takes a partial screenshot of the current screen and checks if the target image is present.
    If the target image is found, it returns the center coordinates of the target image.
    If the target image is not found, it returns None.
    '''

    screenshot = ImageGrab.grab(bbox=region)
    screenshotGray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY) # Convert to grayscale for better matching

    bestMatch = None
    bestMatchValue = -1
    bestScale = 1.0
    
    # Scale the target images to find the match with the most confidence, preventing false positives
    for scale in np.arange(constants.scaleRange[0], constants.scaleRange[1], constants.scaleStep):
        targetImageScaled = cv2.resize(targetImage, None, fx=scale, fy=scale)

        result = cv2.matchTemplate(screenshotGray, targetImageScaled, cv2.TM_CCOEFF_NORMED) # TM_CCOEFF_NORMED is the most commonly used equation for template matching
        maxVal, _, maxLoc = cv2.minMaxLoc(result)[1:] # maxVal is the maximum confidence of the result for any pixel, and maxLoc is the coordinates of said pixel

        if maxVal >= constants.threshold and maxVal > bestMatchValue:
            bestMatch = maxLoc
            bestMatchValue = maxVal
            bestScale = scale
    
    if bestMatch is not None:
        # Center coords to point the mouse to a more accurate position
        centerX = int(bestMatch[0] + targetImage.shape[1] * bestScale / 2)
        centerY = int(bestMatch[1] + targetImage.shape[0] * bestScale / 2)
        return (centerX + region[0], centerY + region[1])  # Adjust for the region offset
    else:
        return None
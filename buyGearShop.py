# For debugging purposes, you can uncomment the following import statements:
import numpy as np
from datetime import datetime
from PIL import ImageGrab

import autoit
import cv2
from time import sleep # To make sure each action is registered properly

import Constants.constantsPositions as constants
import Constants.constantsFilepaths as filepaths
from buy import buy
from locateTemplateOnScreen import locateTemplateOnScreen

def buyGearShop():
    '''
    Automatically buys most items from the gear shop in the game.
    By default, it will buy the following items:
    - Recall Wrenches
    - All Sprinklers(Basic, Advanced, Godly, Master)
    - Lightning Rods

    This can be modifed in the Constants/constantsFilepaths.py file.
    '''

    gearToBuy = list(filepaths.gearShopItemTemplatePaths)

    # If you plan to be in the gear shop for a long time, you can uncomment the line below to not use the recall wrench
    if(moveToGearShop()):  # Ensure player is in the gear shop before buying items
        buy(gearToBuy)  # Buy the items from the gear shop
        closeGearShop()  # Close the gear shop after buying items
    
    else:
        print("Failed to open the gear shop. Please check your settings and try again.")

def moveToGearShop():
    '''
    Moves the player to the gear shop by holding the recall wrench.
    This function is used to teleport the player to the gear shop.
    '''

    autoit.send(constants.recallWrenchKeybind)  # Player holds the recall wrench in their hand
    autoit.mouse_click("left")  # Player uses the recall wrench to teleport to the gear shop
    sleep(0.1)  # Wait for the teleport animation to finish
    # Scroll to a far enough level so that the dialogue option appears
    autoit.mouse_wheel("up", 20)
    sleep(0.1)  # Wait for the scroll animation to finish
    autoit.mouse_wheel("down", 10)
    sleep(0.1) # Wait for scroll animation to finish
    autoit.send("e") # Player interacts with the gear shop to open it
    sleep(2) # Wait for gear shop vendor to give the options

    
    region = (constants.gearShopOptionsPosX1, constants.gearShopOptionsY1, constants.gearShopOptionsPosX2, constants.gearShopOptionsY2)
    for showGearShopImage in filepaths.showGearShopImagePaths:
        targetImage = cv2.imread(showGearShopImage, cv2.IMREAD_GRAYSCALE)  # Read the image in grayscale for better matching
        showGearShopCoords = locateTemplateOnScreen(region, targetImage)

        if showGearShopCoords is not None:
            autoit.mouse_move(showGearShopCoords[0], showGearShopCoords[1])
            autoit.mouse_click("left")
            autoit.mouse_move(constants.middleX, constants.middleY)  # Move mouse to the center of the screen to focus on the shop window
            sleep(2)  # Wait for the gear shop to open
            return True
    
    # If the gear shop options were not found, take a screenshot for debugging purposes
    screenshot = ImageGrab.grab(bbox=region)
    screenshotGray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    cv2.imwrite(f"debugScreenshot{timestamp}.png", screenshotGray)
    return False  # If the gear shop options were not found, return False

def closeGearShop():
    '''
    Closes the gear shop by clicking the X button.
    This function is used to close the gear shop after buying items.
    '''

    region = (constants.shopWindowPosX1, constants.shopWindowY1, constants.shopWindowPosX2, constants.shopWindowY2)
    XImage = cv2.imread(filepaths.XButtonImagePath, cv2.IMREAD_GRAYSCALE)
    XButtonCoords = locateTemplateOnScreen(region, XImage)

    if XButtonCoords is not None:
        autoit.mouse_move(XButtonCoords[0], XButtonCoords[1])
        autoit.mouse_click("left")  # Click the X button to close the gear shop
    
    else:
        print("Failed to close the gear shop. The X button was not found.")
        # Take a screenshot for debugging purposes
        screenshot = ImageGrab.grab(bbox=region)
        screenshotGray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        cv2.imwrite(f"debugScreenshot{timestamp}.png", screenshotGray)
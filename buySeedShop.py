import autoit
import cv2
from time import sleep

import Constants.constantsPositions as constants
import Constants.constantsFilepaths as filepaths
from buy import buy
from locateTemplateOnScreen import locateTemplateOnScreen

def buySeedShop():
    '''
    Automatically buys the desired items from the gear shop in the game.
    This can be modifed in the Constants/constantsFilepaths.py file.
    '''

    seedsToBuy = list(filepaths.seedShopItemTemplatePaths)

    if(moveToSeedShop()):  # Ensure player is in the seed shop before buying items
        buy(seedsToBuy)  # Buy the items from the seed shop
        closeSeedShop()  # Close the seed shop after buying items
    
    else:
        print("Failed to open the seed shop. Please check your settings and try again.")

def moveToSeedShop():
    '''
    Moves the player to the seed shop.
    This function should be called before buying seeds.
    '''

    autoit.mouse_move(constants.seedsButtonPosX, constants.seedsButtonPosY)
    autoit.mouse_click("left")  # Click the seeds button to open the seed shop
    sleep(0.3)  # Wait for the teleport animation to finish
    autoit.send("e") # Player interacts with the gear shop to open it
    autoit.mouse_move(constants.middleX, constants.middleY)  # Move mouse to the center of the screen to focus on the shop window
    sleep(2) # Wait for seed shop vendor to open seed shop

    # Check if any rarity image is present in the seed shop window, meaning that the seed shop is opened
    region = (constants.shopWindowPosX1, constants.shopWindowY1, constants.shopWindowPosX2, constants.shopWindowY2)
    shopOpenImage = cv2.imread(filepaths.shopOpenPath, cv2.IMREAD_GRAYSCALE)

    if locateTemplateOnScreen(region, shopOpenImage, filepaths.shopOpenPath) is not None:
        return True
    
    print("Failed to open the seed shop. The seed shop was not found.")
    return False

def closeSeedShop():
    '''
    Closes the seed shop by clicking the X button.
    This function is used to close the seed shop after buying items.
    '''

    region = (constants.shopWindowPosX1, constants.shopWindowY1, constants.shopWindowPosX2, constants.shopWindowY2)
    XImage = cv2.imread(filepaths.XButtonImagePath, cv2.IMREAD_GRAYSCALE)
    XButtonCoords = locateTemplateOnScreen(region, XImage, filepaths.XButtonImagePath)

    if XButtonCoords is not None:
        autoit.mouse_move(XButtonCoords[0], XButtonCoords[1])
        autoit.mouse_click("left")  # Click the X button to close the gear shop
    
    else:
        print("Failed to close the gear shop. The X button was not found.")
        autoit.mouse_move(constants.XButtonPosX, constants.XButtonPosY)
        autoit.mouse_click("left")
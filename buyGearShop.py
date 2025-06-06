import autoit
import cv2
from time import sleep # To make sure each action is registered properly

import Constants.constantsPositions as constants
import Constants.constantsFilepaths as filepaths
from locateTemplateOnScreen import locateTemplateOnScreen

def buyGearShop():
    '''
    Automatically buys most items from the gear shop in the game.
    By default, it will buy the following items:
    - Recall Wrenches
    - All Sprinklers(Basic, Advanced, Godly, Master)
    - Lightning Rods

    This can be modifed in the Constants/constantsPositions.py file.
    '''

    gearToBuy = list(filepaths.gearShopItemTemplatePaths)

    autoit.mouse_move(constants.middleX, constants.middleY)
    autoit.mouse_click("left")  # Click to focus the game window
    autoit.mouse_wheel("up", 100)  # Scroll up to the top of the shop

    while(len(gearToBuy) > 0):
        updatedGearToBuy = list(gearToBuy) # To prevent modifying the list while iterating over it
        foundGear = False #  Flag to determine if we need to scroll down to find more items

        for imagePath in gearToBuy:
            targetImage = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE) # Read the image in grayscale for better matching
            
            # Defines the region of the shop window
            region = (constants.shopWindowPosX1, constants.shopWindowY1, constants.shopWindowPosX2, constants.shopWindowY2)
            coords = locateTemplateOnScreen(region, targetImage)

            if coords is not None: # Found item in the shop
                updatedGearToBuy.remove(imagePath)  # Remove the item from the list after buying it so we don't look for it again
                foundGear = True

                autoit.mouse_move(coords[0], coords[1])
                autoit.mouse_click("left")
                sleep(0.5) # Wait for the animation to finish

                moneySymbolImage = cv2.imread(filepaths.moneySymbolImagePath, cv2.IMREAD_GRAYSCALE)
                moneySymbolCoords = locateTemplateOnScreen(region, moneySymbolImage)

                if moneySymbolCoords is not None: # Found the money symbol indicating that we can buy the item
                    autoit.mouse_move(moneySymbolCoords[0], moneySymbolCoords[1])
                    # TODO: Modify this so it's not hardcoded to click 25 times
                    # Some of those clicks won't register because we click so fast
                    for _ in range(25):
                        autoit.mouse_click("left")
            
        if(not foundGear):
            autoit.mouse_wheel("down", 1)  # Scroll down by one click to look at the next item in the shop
            sleep(0.5)  # Wait for the scroll animation to finish
        
        gearToBuy = list(updatedGearToBuy)

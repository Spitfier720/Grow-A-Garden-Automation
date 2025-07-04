import autoit
import importlib
from datetime import datetime

import Constants.constantsPositions as constants
import Constants.constantsFilepaths as filepaths
from buyGearShop import buyGearShop
from buySeedShop import buySeedShop

def isFiveMinMark():
    curTime = datetime.now()
    return curTime.minute % 5 == 0 and curTime.second == 0

def focusGameWindow():
    '''
    Focuses the game window to ensure that the mouse clicks are registered correctly.
    '''
    
    autoit.mouse_move(constants.middleX, constants.middleY)
    autoit.mouse_click("left")  # Click to focus the game window

def returnToGarden():
    '''
    Returns the player to the garden by clicking the garden button, resetting the cycle.
    '''
    
    autoit.mouse_move(constants.gardenButtonPosX, constants.gardenButtonPosY)
    autoit.mouse_click("left")  # Click the garden button to return to the garden
    autoit.mouse_move(constants.middleX, constants.middleY)  # Move mouse to the center of the screen to finish off nicely

def main():
    while(True):
        # Uncomment the if true statement to instantly buy shop items for testing purposes
        # if True:
        if(isFiveMinMark()):
            print("Shops have reset. Time is " + datetime.now().strftime("%H:%M"))
            importlib.reload(filepaths) # Allows you to change the constantsFilepaths file without restarting the script
            focusGameWindow()
            print("Buying gear shop items...")
            buyGearShop()
            print("Gear shop items bought successfully.")
            print("Buying seed shop items...")
            buySeedShop()
            print("Seed shop items bought successfully.")
            returnToGarden()
            print("Returned to garden. Cycle complete.")

if __name__ == "__main__":
    main()
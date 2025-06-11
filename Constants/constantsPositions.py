import pyautogui

'''
Feel free to modify the relative positions of the buttons based on your screen resolution, if you like.
The hope is that with relative positions, the code will work on any screen resolution.
'''

screenWidth, screenHeight = pyautogui.size()

# Relative positions for buttons that do not change position
seedsButtonRelativeX = 680 / screenWidth
seedsButtonRelativeY = 135 / screenHeight
seedsButtonPosX, seedsButtonPosY = int(screenWidth * seedsButtonRelativeX), int(screenHeight * seedsButtonRelativeY)

gardenButtonRelativeX = 960 / screenWidth
gardenButtonRelativeY = 137 / screenHeight
gardenButtonPosX, gardenButtonPosY = int(screenWidth * gardenButtonRelativeX), int(screenHeight * gardenButtonRelativeY)

# sellButtonRelativeX = 1240 / screenWidth
# sellButtonRelativeY = 135 / screenHeight
# sellButtonPosX, sellButtonPosY = int(screenWidth * sellButtonRelativeX), int(screenHeight * sellButtonRelativeY)

# Center of the screen, which is used to interact with the store
middleX, middleY = screenWidth // 2, screenHeight // 2

# Number of scrolls to perform to reach the bottom of the shops
# These values may need to be adjusted based on how far your scroll wheel scrolls
numScrollsGearShop = 15
numScrollsSeedsShop = 7

# Dimensions of the shop window, which will be used to take a screenshot and detect items
# Top left corner of the shop window
shopWindowX1 = 555 / screenWidth
shopWindowY1 = 225 / screenHeight
# Bottom right corner of the shop window
shopWindowX2 = 1360 / screenWidth
shopWindowY2 = 980 / screenHeight
# Convert to relative positions
shopWindowPosX1, shopWindowY1 = int(screenWidth * shopWindowX1), int(screenHeight * shopWindowY1)
shopWindowPosX2, shopWindowY2 = int(screenWidth * shopWindowX2), int(screenHeight * shopWindowY2)

# The keybind to hold the recall wrench, which teleports the player to the gear shop
recallWrenchKeybind = "3"  # Change this to the keybind you use for the recall wrench

# Dimensions of the gear shop options menu, which will be used to detect the option that opens the gear shop
# Top left corner of the gear shop options menu
gearShopOptionsX1 = 960 / screenWidth
gearShopOptionsY1 = 515 / screenHeight
# Bottom right corner of the gear shop options menu
gearShopOptionsX2 = 1700 / screenWidth
gearShopOptionsY2 = 700 / screenHeight
# Convert to relative positions
gearShopOptionsPosX1, gearShopOptionsY1 = int(screenWidth * gearShopOptionsX1), int(screenHeight * gearShopOptionsY1)
gearShopOptionsPosX2, gearShopOptionsY2 = int(screenWidth * gearShopOptionsX2), int(screenHeight * gearShopOptionsY2)
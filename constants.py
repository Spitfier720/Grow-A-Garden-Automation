import pyautogui

screenWidth, screenHeight = pyautogui.size()

seedsButtonRelativeX = 680 / 1920
seedsButtonRelativeY = 135 / 1080
seedsButtonPosX, seedsButtonPosY = int(screenWidth * seedsButtonRelativeX), int(screenHeight * seedsButtonRelativeY)

gardenButtonRelativeX = 960 / 1920
gardenButtonRelativeY = 137 / 1080
gardenButtonPosX, gardenButtonPosY = int(screenWidth * gardenButtonRelativeX), int(screenHeight * gardenButtonRelativeY)

sellButtonRelativeX = 1240 / 1920
sellButtonRelativeY = 135 / 1080
sellButtonPosX, sellButtonPosY = int(screenWidth * sellButtonRelativeX), int(screenHeight * sellButtonRelativeY)

XButtonRelativeX = 1290 / 1920
XButtonRelativeY = 265 / 1080
XButtonPosX, XButtonPosY = int(screenWidth * XButtonRelativeX), int(screenHeight * XButtonRelativeY)

BuyButtonRelativeX = 770 / 1920
BuyButtonRelativeY = 632 / 1080
BuyButtonPosX, BuyButtonPosY = int(screenWidth * BuyButtonRelativeX), int(screenHeight * BuyButtonRelativeY)
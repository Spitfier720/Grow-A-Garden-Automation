import autoit
import constants
from time import sleep

def main():
    autoit.mouse_move(constants.seedsButtonPosX, constants.seedsButtonPosY, speed = 10)
    sleep(0.5)
    autoit.mouse_move(constants.gardenButtonPosX, constants.gardenButtonPosY, speed = 10)
    sleep(0.5)
    autoit.mouse_move(constants.sellButtonPosX, constants.sellButtonPosY, speed = 10)
    sleep(0.5)
    autoit.mouse_move(constants.XButtonPosX, constants.XButtonPosY, speed = 10)
    sleep(0.5)
    autoit.mouse_move(constants.BuyButtonPosX, constants.BuyButtonPosY, speed = 10)
    sleep(0.5)

if __name__ == "__main__":
    main()
from datetime import datetime
from time import sleep

from buyGearShop import buyGearShop

def isFiveMinMark():
    return datetime.now().minute % 5 == 0

def main():
    while(True):
        # Uncomment these lines to instantly buy gear shop items for testing purposes
        # if(True):
        #     buyGearShop()

        if(isFiveMinMark()):
            print("Buying gear shop items...")
            buyGearShop()
            print("Gear shop items bought successfully.")
        
        else:
            print("Waiting for the next 5-minute mark...")
        
        sleep(60)

if __name__ == "__main__":
    main()
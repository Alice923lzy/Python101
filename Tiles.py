#This is a program to calculate tile number needed
import math

def numTiles(wRoom,lRoom,sTile):

    """
    numTiles that will take the size of one tile, and the width and length of a room  as parameters and will return the number of tiles it will take to cover that room. The number of tiles should be rounded up to the nearest whole number.

    """
    sizeRoom = wRoom * lRoom
    return math.ceil(sizeRoom/(sTile*sTile))
    


def main():
    """
    This function will collects the input for the program and show the output to user
    """

    #for validity check
    errStr = "Please enter a valid number."


    #number of room
    numRoom = int(input("Enter the number of rooms in the job: "))
    while (numRoom < 0 or numRoom > 4): 
                print(errStr,"valid only between 0-4")
                numRoom = int(input("Enter the number of rooms in the job: "))

    #tile size
    sizeTile= int(input("Enter the size of each tile in cm: "))
    while (sizeTile <= 0): 
            print(errStr)
            sizeTile= int(input("Enter the size of each tile in cm: "))

    #declare sum var
    sumTile = 0

    #loop through room
    for x in range(numRoom):
        room = str(x + 1)


        #width
        widthRoom = int(input("Enter room "+room+" width (cm): "))
        while (widthRoom <= 0): 
            print(errStr)
            widthRoom = int(input("Enter room "+room+" width (cm): "))


        #length
        lenRoom = int(input("Enter room "+room+" length (cm): "))
        while (lenRoom <= 0): 
            print(errStr)
            lenRoom = int(input("Enter room "+room+" length (cm): "))

        #calculate
        tileReq = numTiles(widthRoom,lenRoom,sizeTile)
        print("Room",room,"requires:",tileReq)
        sumTile = sumTile + tileReq


    #outputs
    print("The ",numRoom," rooms in this job will require ",sumTile," tiles.")
    numBoxs = math.ceil(sumTile / 20)
    print("The number of boxes of tiles needed is ",numBoxs,".")
    leftOver = numBoxs*20 - sumTile
    print("There will be ",leftOver," extra tiles left over.")
    print("Thanks for using.")







main()

    




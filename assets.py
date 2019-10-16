import config
import main, board, game

import sys
import time
import random
import tkinter as tk
from tkinter import *
import tkinter

global shipPlaceChooser

class DisplayShip():

    def __init__(self, position, ship, rotation):

        #define variables
        self.position = position
        self.ship = ship
        self.rotation = rotation

        self.ships = config.ships

        #gets the row and column of the button pressed
        buttonInfo = config.PcoordinateButtons[position].grid_info()
        self.buttonColumn = buttonInfo['column']
        self.buttonRow = buttonInfo['row']

        #creates variables according to the ship type - self.length is the amount of tiles it takes up and self.shipCode is used to identify the type of ship
        if self.ship == "carrier":
            self.shipCode = 0
            self.length = 5

        if self.ship == "battleship":
            self.shipCode = 1
            self.length = 4

        if self.ship == "cruiser":
            self.shipCode = 2
            self.length = 3

        if self.ship == "destroyer":
            self.shipCode = 3
            self.length = 2

        if self.ship == "submarine":
            self.shipCode = 4
            self.length = 2

        self.renderShips()


    def shipPlacementChecker(self):

        #creates list for the positions the ship will be rendered it
        selectedPositions = []

        #adds position to 'selectedPosition' 
        for i in range(self.length):
            if self.rotation == "right":
                selectedPositions.append(self.position+i)
            if self.rotation == "down":
                selectedPositions.append(self.position+(i*11))
            if self.rotation == "left":
                selectedPositions.append(self.position-i)
            if self.rotation == "up":
                selectedPositions.append(self.position-(i*11))

        #compares 'selectedPosition' to each list in 'shipsPositions' and sees if there are any matches
        #if it finds a match it returns 'False' if not 'True' is returned
        for i in range(5):
            check = any(item in selectedPositions for item in config.shipsPositions[i])
            if check == True:
                return False

        return True
            

    def renderShips(self):

        #this if statement checks if any of the positions for the ship that's wanted to be renderedis occupied by another ship
        if self.shipPlacementChecker() == True:

            if self.rotation == "up":
                #only allows you to place the ship in the playing grid
                if self.buttonRow > (self.length - 1) and self.buttonColumn != 0 and self.buttonRow !=0:
            
                    #displays the ship tiles and adds the positions to 'shipsPositions'
                    for i in range(self.length):
                        config.PcoordinateButtons[self.position-(i*11)].config(image="")
                        config.PcoordinateButtons[self.position-(i*11)].config(image=self.ships[self.shipCode][3][i])
                        config.shipsPositions[self.shipCode].append(self.position-(i*11))
                        self.correctPlacement = True
                else:
                    self.correctPlacement = False
                

            if self.rotation == "right":
                #only allows you to place the ship in the playing grid
                if self.buttonColumn < (12 - self.length) and self.buttonColumn != 0 and self.buttonRow != 0:

                    #displays the ship tiles and adds the positions to 'shipsPositions'
                    for i in range(self.length):
                        config.PcoordinateButtons[self.position+(i)].config(image="")
                        config.PcoordinateButtons[self.position+(i)].config(image=self.ships[self.shipCode][0][i])
                        config.shipsPositions[self.shipCode].append(self.position+i)
                        self.correctPlacement = True
                else:
                    self.correctPlacement = False
                
            if self.rotation == "down":
                #only allows you to place the ship in the playing grid
                if self.buttonRow < (12 - self.length) and self.buttonRow != 0 and self.buttonColumn != 0:

                    #displays the ship tiles and adds the positions to 'shipsPositions'
                    for i in range(self.length):
                        config.PcoordinateButtons[self.position+(i*11)].config(image="")
                        config.PcoordinateButtons[self.position+(i*11)].config(image=self.ships[self.shipCode][1][i])
                        config.shipsPositions[self.shipCode].append(self.position+(i*11))
                        self.correctPlacement = True
                else:
                    self.correctPlacement = False

            if self.rotation == "left":
                #only allows you to place the ship in the playing grid
                if self.buttonColumn > (self.length - 1) and self.buttonColumn != 0 and self.buttonRow != 0:

                    #displays the ship tiles and adds the positions to 'shipsPositions'
                    for i in range(self.length):
                        config.PcoordinateButtons[self.position-(i)].config(image="")
                        config.PcoordinateButtons[self.position-(i)].config(image=self.ships[self.shipCode][2][i])
                        config.shipsPositions[self.shipCode].append(self.position-i)
                        self.correctPlacement = True
                else:
                    self.correctPlacement = False



        else:
            self.correctPlacement = False




def assetsInitialisation():
    #Loads in all necessary assets

    config.arrowRight = PhotoImage(file="./assets/arrow/arrow0.gif")
    config.arrowDown = PhotoImage(file="./assets/arrow/arrow1.gif")
    config.arrowLeft = PhotoImage(file="./assets/arrow/arrow2.gif")
    config.arrowUp = PhotoImage(file="./assets/arrow/arrow3.gif")
    
    
    def filePathFormater(ship, number):
        #creates variables for use in the filepath
        for i in range(4):
            if i == 0:
                r = "right"
            if i == 1:
                r = "down"
            if i == 2:
                r = "left"
            if i == 3:
                r = "up"

            #fetches and stores all ship tile photos with their 4 orientations in the 'ships' list 
            if ship == 0:
                filePath = ("./assets/submarine/" + r + "/submarine" + str(number) + ".gif")
                image = PhotoImage(file=filePath)
                config.ships[4][i].append(image)
            if ship == 1:
                filePath = ("./assets/destroyer/" + r + "/destroyer" + str(number) + ".gif")
                image = PhotoImage(file=filePath)
                config.ships[3][i].append(image)
            if ship == 2:
                filePath = ("./assets/cruiser/" + r + "/cruiser" + str(number) + ".gif")
                image = PhotoImage(file=filePath)
                config.ships[2][i].append(image)
            if ship == 3:
                filePath = ("./assets/battleship/" + r + "/battleship" + str(number) + ".gif")
                image = PhotoImage(file=filePath)
                config.ships[1][i].append(image)
            if ship == 4:
                filePath = ("./assets/aircraftCarrier/" + r + "/aircraftCarrier" + str(number) + ".gif")
                image = PhotoImage(file=filePath)
                config.ships[0][i].append(image)
    

    #ships = ["carrier", "battleship", "cruiser", "destroyer", "submarine"]
    #Where the images of the ships are stored
    config.ships = [[[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]]

    #Where the position of the ships are stored
    config.shipsPositions = [[], [], [], [], []]

    
    #i-1 = ship number
    #b = image number

    #This loop runs through each image number b times(the amount of images it has/ the number of squares it takes up)
    #and forwards the numbers to the filePathFormater function
    
    for i in range(6):
        for b in range(i):
            #As the submarine is the first ship but has two image files it has to re-loop and increment the ship number
            if i == 1:
                for x in range(2):
                    b = b+x
                    filePathFormater(i-1, b)
            else:
                filePathFormater(i-1, b)

    placeShips()


def placeShips():
    global shipPlaceChooser
    #variable initiated so program can know which ship was rendered last so therefore the ship that needs to be rendered next
    config.numOfShipsPlaced = 0

    #initiates list where labels that prompt the user to place the ships are stored
    config.shipPlacePrompt = []

    #labels are created to prompt user
    carrierPrompt = Label(config.commandWin, text="ADMIRAL, PLACE YOUR\nAIRCRAFT CARRIER\n5 LONG", bg="grey", fg="white", height=5, width=30, font=("Courier"))
    battleshipPrompt = Label(config.commandWin, text="ADMIRAL, PLACE YOUR\nBATTLESHIP\n4 LONG", bg="grey", fg="white", height=5, width=30, font=("Courier"))
    cruiserPrompt = Label(config.commandWin, text="ADMIRAL, PLACE YOUR\nCRUISER\n3 LONG", bg="grey", fg="white", height=5, width=30, font=("Courier"))
    destroyerPrompt = Label(config.commandWin, text="ADMIRAL, PLACE YOUR\nDESTROYER\n2 LONG", bg="grey", fg="white", height=5, width=30, font=("Courier"))
    submarinePrompt = Label(config.commandWin, text="ADMIRAL, PLACE YOUR\nSUBMARINE\n2 LONG", bg="grey", fg="white", height=5, width=30, font=("Courier"))


    #labels are added to the list
    config.shipPlacePrompt.append(carrierPrompt)
    config.shipPlacePrompt.append(battleshipPrompt)
    config.shipPlacePrompt.append(cruiserPrompt)
    config.shipPlacePrompt.append(destroyerPrompt)
    config.shipPlacePrompt.append(submarinePrompt)

    #first prompt is shown
    carrierPrompt.pack()

    def placeCarrier(position, rotation):
        #creates the object 'carrier' for the class 'DisplayShip'
        carrier = DisplayShip(position, "carrier", rotation)
        #if the ship was correctly positioned, 'config.numOfShipsPlaced' is increment and the prompt is refreshed for the new ship
        if carrier.correctPlacement == True:
            config.numOfShipsPlaced = 1
            config.shipPlacePrompt[0].destroy()
            config.shipPlacePrompt[1].pack()

    def placeBattleship(position, rotation):
        #creates the object 'battleship' for the class 'DisplayShip'            
        battleship = DisplayShip(position, "battleship", rotation)
        #if the ship was correctly positioned, 'config.numOfShipsPlaced' is increment and the prompt is refreshed for the new ship
        if battleship.correctPlacement == True:
            config.numOfShipsPlaced = 2
            config.shipPlacePrompt[1].destroy()
            config.shipPlacePrompt[2].pack()
            
    def placeCruiser(position, rotation):
        #creates the object 'cruiser' for the class 'DisplayShip'            
        cruiser = DisplayShip(position, "cruiser", rotation)
        #if the ship was correctly positioned, 'config.numOfShipsPlaced' is increment and the prompt is refreshed for the new ship
        if cruiser.correctPlacement == True:
            config.numOfShipsPlaced = 3
            config.shipPlacePrompt[2].destroy()
            config.shipPlacePrompt[3].pack()

            
    def placeDestroyer(position, rotation):
        #creates the object 'destroyer' for the class 'DisplayShip'            
        destroyer = DisplayShip(position, "destroyer", rotation)
        #if the ship was correctly positioned, 'config.numOfShipsPlaced' is increment and the prompt is refreshed for the new ship
        if destroyer.correctPlacement == True:
            config.numOfShipsPlaced = 4
            config.shipPlacePrompt[3].destroy()
            config.shipPlacePrompt[4].pack()
            
    def placeSubmarine(position, rotation):
        #creates the object 'submarine' for the class 'DisplayShip'            
        submarine = DisplayShip(position, "submarine", rotation)
        #if the ship was correctly positioned, 'config.numOfShipsPlaced' is increment and the prompt is refreshed for the new ship
        if submarine.correctPlacement == True:
            config.numOfShipsPlaced = 5
            config.shipPlacePrompt[4].destroy()

            config.gameStartUpComplete = True
            game.gamePlaying()
            

    def shipPlaceChooser(position, rotation):

        #decides which ship needs to be rendered next and calls the appropriate function
        if config.numOfShipsPlaced == 0:
            placeCarrier(position, rotation)
        if config.numOfShipsPlaced == 1:
            placeBattleship(position, rotation)
        if config.numOfShipsPlaced == 2:
            placeCruiser(position, rotation)
        if config.numOfShipsPlaced == 3:
            placeDestroyer(position, rotation)
        if config.numOfShipsPlaced == 4:
            placeSubmarine(position, rotation)
            

    loopCondition = False
    numOfAiShips = 0
    config.AiShipsPositions = [[], [], [], [], []]
    
    placeAiShips(loopCondition, numOfAiShips)


def placeAiShips(loopCondition, numOfAiShips):

    def AiShipPlacementChecker(rotation, position, length):
        #global config.AiShipsPositions
        
        #creates list for the positions the ship will be rendered it
        selectedPositions = []

        #adds position to 'selectedPosition'
        for i in range(length):
            if rotation == 0: #(up)
                selectedPositions.append(position-(i*11))
            if rotation == 1: #(right)
                selectedPositions.append(position+i)
            if rotation == 2: #(down)
                selectedPositions.append(position+(i*11))
            if rotation == 3: #(left)
                selectedPositions.append(position-i)

        #compares 'selectedPosition' to each list in 'shipsPositions' and sees if there are any matches
        #if it finds a match it returns 'False' if not 'True' is returned
        for i in range(5):
            check = any(item in selectedPositions for item in config.AiShipsPositions[i])
            if check == True:
                return False

        return True

    
    #this acts as a while loop until 5 ships have been placed by the AI
    if loopCondition == False:

        #assigns the right length to the ship
        if numOfAiShips == 0:   #carrier
            length = 5
        if numOfAiShips == 1:   #battleship
            length = 4
        if numOfAiShips == 2:   #cruiser
            length = 3
        if numOfAiShips == 3:   #destroyer
            length = 2
        if numOfAiShips == 4:   #submarine
            length = 2

        #creates a random position and rotation
        ranNum = random.randint(1, 121)
        ranRotation = random.randint(0,3)
        
        #gets the row and column of the button pressed
        buttonInfo = config.EcoordinateButtons[ranNum].grid_info()
        buttonColumn = buttonInfo['column']
        buttonRow = buttonInfo['row']

        #this if statement checks if any of the positions for the ship that's wanted to be positioned is occupied by another ship
        if AiShipPlacementChecker(ranRotation, ranNum, length) == True:

            #Checks to see if the random position is in the playing area
            if buttonColumn != 0 and buttonRow != 0:
            
                if ranRotation == 0: #(up)
                    #checks to see if the ships position would fit where it has been placed
                    if buttonRow > (length - 1) and buttonColumn != 0 and buttonRow !=0:
                        for i in range(length):
                            config.AiShipsPositions[numOfAiShips].append(ranNum-(i*11))
                        numOfAiShips += 1

                if ranRotation == 1: #(right)
                    #checks to see if the ships position would fit where it has been placed
                    if buttonColumn < (12 - length) and buttonColumn != 0 and buttonRow !=0:
                        for i in range(length):
                            config.AiShipsPositions[numOfAiShips].append(ranNum+i)
                        numOfAiShips += 1

                if ranRotation == 2: #(down)
                    #checks to see if the ships position would fit where it has been placed
                    if buttonRow < (12 - length) and buttonColumn != 0 and buttonRow !=0:
                        for i in range(length):
                            config.AiShipsPositions[numOfAiShips].append(ranNum+(i*11))
                        numOfAiShips += 1

                if ranRotation == 3: #(left)
                    #checks to see if the ships position would fit where it has been placed
                    if buttonColumn > (length - 1) and buttonColumn != 0 and buttonRow !=0:
                        for i in range(length):
                            config.AiShipsPositions[numOfAiShips].append(ranNum-i)
                        numOfAiShips += 1

        #checks to see if 5 ships have been placed, if it has the loop is broken if not the function is repeated
        if numOfAiShips < 5:
            placeAiShips(loopCondition, numOfAiShips)
        else:
            loopCondition = True
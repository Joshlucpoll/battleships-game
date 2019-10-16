import config

import main, board, assets

import sys
import time
import random
import tkinter as tk
from tkinter import *
import tkinter

global playerFire

def gamePlaying():
    global playerFire


    def tryAgain():

        config.root.destroy()
        main.main()

    def giveUp():

        exit()

    def gameWin():
        
        config.gameOver = True
        config.fireInstructions.destroy()
        endMessage = Label(config.commandWin, text="CONGRATULATIONS ADMIRAL, YOU HAVE\nSUCCESSFULLY DESTROYED THE ENEMY FLEET.\nCHALLENGE ANOTHER?", font="Courier", bg = "grey", fg = "white")
        endMessage.pack()

        tryAgainButton = Button(config.commandWin, text="TRY AGAIN", font="Courier", bg = "dark grey", fg = "white", command = tryAgain)
        tryAgainButton.pack()

        giveUpButton = Button(config.commandWin, text="GIVE UP", font="Courier", bg = "dark grey", fg = "white", command = giveUp)
        giveUpButton.pack()
        
    def gameLose():
        
        config.gameOver = True
        config.fireInstructions.destroy()
        endMessage = Label(config.commandWin, text="ADMIRAL YOUR FLEET HAS BEEN DESTROYED.\nSHOULD I SEND REINFORCEMENTS?", font="Courier", bg = "grey", fg = "white")
        endMessage.pack()

        tryAgainButton = Button(config.commandWin, text="TRY AGAIN", font="Courier", bg = "dark grey", fg = "white", command = tryAgain)
        tryAgainButton.pack()

        giveUpButton = Button(config.commandWin, text="GIVE UP", font="Courier", bg = "dark grey", fg = "white", command = giveUp)
        giveUpButton.pack()
            


    def playerFire(position):
        global playerFire

        if config.shipsLeftAi == 0:
            gameLose()

        else:
        
            config.EcoordinateButtons[position].config(image=config.sea)

            for i in range(config.shipsLeftPlayer):
                if position in config.AiShipsPositions[i]:
                    check = True
                    break
                check =  False

            config.positionsAttackedPlayer.append(position)

            if check == False:
                config.EcoordinateButtons[position].config(image=config.whitePeg)
            else:
                config.EcoordinateButtons[position].config(image=config.redPeg)

            config.playersTurn = False

        
            for i in range(config.shipsLeftPlayer):
                check = set(config.AiShipsPositions[i]).issubset(config.positionsAttackedPlayer)
                if check == True:
                    break

            if check == True:
                for n in range(len(config.AiShipsPositions[i])):
                    config.EcoordinateButtons[config.AiShipsPositions[i][n]].config(image="")
                    config.EcoordinateButtons[config.AiShipsPositions[i][n]].config(image=config.sunkShip, bg= "red")
                config.shipsLeftPlayer -= 1
                config.AiShipsPositions.pop(i)

            config.root.after(1000, AiTurn)
        

    def AiTurn():

        def AiRanNumGenerator():

            #creates a random position
            AiGuess = random.randint(1, 121)

            if AiGuess not in config.positionsAttackedAi:


                #gets the row and column of the button
                buttonInfo = config.PcoordinateButtons[AiGuess].grid_info()
                buttonColumn = buttonInfo['column']
                buttonRow = buttonInfo['row']

                #only allows buttons in the playing area
                if buttonRow != 0 and buttonColumn != 0:
                    config.positionsAttackedAi.append(AiGuess)
                    displayAiFire(AiGuess)
                else:
                    AiRanNumGenerator()
            else:
                AiRanNumGenerator()

        def displayAiFire(AiGuess):

            for i in range(config.shipsLeftAi):
                check = AiGuess in config.shipsPositions[i]
                if check == True:
                    break
            
            if check == False:
                config.PcoordinateButtons[AiGuess].config(image="")
                config.PcoordinateButtons[AiGuess].config(image=config.whitePeg)
            else:
                config.PcoordinateButtons[AiGuess].config(image="")
                config.PcoordinateButtons[AiGuess].config(image=config.redPeg)
                config.positionsToHit = list(config.shipsPositions[i])
                config.positionsToHit.remove(AiGuess)


        if config.shipsLeftPlayer == 0:
            gameWin()

        else:

            if len(config.positionsToHit) != 0:

                config.positionsAttackedAi.append(config.positionsToHit[0])
                config.PcoordinateButtons[config.positionsToHit[0]].config(image="")
                config.PcoordinateButtons[config.positionsToHit[0]].config(image=config.redPeg)
                config.positionsToHit.remove(config.positionsToHit[0])

                for i in range(config.shipsLeftAi):
                    check = set(config.shipsPositions[i]).issubset(config.positionsAttackedAi)
                    if check == True:
                        break
                if check == True:
                    for n in range(len(config.shipsPositions[i])):
                        config.PcoordinateButtons[config.shipsPositions[i][n]].config(image="")
                        config.PcoordinateButtons[config.shipsPositions[i][n]].config(image=config.sunkShip, bg= "red")
                    config.shipsLeftAi -= 1
                    config.shipsPositions.pop(i)
                    if config.shipsLeftAi == 0:
                        gameLose()

            else:
                AiRanNumGenerator()


        
            config.playersTurn = True
        

    config.rotationButton.destroy()
    config.fireInstructions = Label(config.commandWin, text="ADMIRAL, COMMENCE ATTACK\n ON THE ENEMY FLEET!", font="Courier", bg = "grey", fg = "white")
    config.fireInstructions.pack()

    config.playersTurn = True
    config.gameOver = False

    config.positionsAttackedPlayer = []
    config.positionsAttackedAi = []
    config.positionsToHit = []

    config.shipsLeftPlayer = 5
    config.shipsLeftAi = 5
    
    config.redPeg = PhotoImage(file="./assets/redPeg.gif")
    config.whitePeg = PhotoImage(file="./assets/whitePeg.gif")
    config.sunkShip = PhotoImage(file="./assets/sunkShip.gif")
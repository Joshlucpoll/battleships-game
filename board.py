import config
import main, assets, game

import tkinter as tk
from tkinter import *
import tkinter


def gameSetup():

    def createBoard(event=None):

        #Generates Buttons for the ENEMY grid in a 11x11 shape

        config.sea = PhotoImage(file="./assets/sea.gif")
        config.crosshair = PhotoImage(file="./assets/crosshair.gif")

        config.gameStartUpComplete = False
        config.gameOver = False
        
        config.EcoordinateButtons = [None]     #'E' = enemy
        
        
        for x in range(0, 11):
            for y in range(0, 11):

                #Adds variable of each Button to the list 'EcoordinatesButons' for later configuration
                b = Button(enemyGrid, image=config.sea, bg='dark blue', height = 35, width = 33)
                b.grid(row=x, column=y)
                config.EcoordinateButtons.append(b)

                #Removes image of blue square to add number/letter, as well as change size to match
                if x == 0 or y == 0:
                    b.config(image="", height=2, width=4)
                    
                #Event triggers created to identify coordinate player wants to hit
                b.bind("<Button-1>", main.Eclick)
                b.bind("<Enter>", main.Eenter)
                b.bind("<Leave>", main.Eexit)

        for i in range(11):
            #Excludes button with position 1
            if i != 0:
                #Generates numbers across the top of the enemy board
                config.EcoordinateButtons[i+1].config(text=str(i), fg='white', state=DISABLED)
                #Generates Letters down the side of enemy board
                config.EcoordinateButtons[((11*i)+1)].config(text=chr(int(i+64)), fg='white', state=DISABLED)
        


        #Generates Buttons for the PLAYER grid in a 11x11 shape
        config.PcoordinateButtons = [None]     #'P' = player

        for x in range(0, 11):          
            for y in range(0, 11):

                #Adds variable of each Button to the list 'PcoordinatesButons' for later configuration
                b = Button(playerGrid,image=config.sea, bg="dark blue", height = 35, width = 33)
                b.grid(row=x, column=y)
                config.PcoordinateButtons.append(b)

                #Removes image of blue square to add number/letter, as well as change size to match
                if x == 0 or y == 0:
                    b.config(image="", height=2, width=4)
                
                #Event triggers created to identify where the player wants to place ships
                b.bind("<Enter>", main.Penter)
                b.bind("<Leave>", main.Pexit)
                b.bind("<Button-1>", main.Pclick)


        for i in range(11):
            #Excludes button with position 1
            if i != 0:
                #Generates numbers across the top of the player board
                config.PcoordinateButtons[i+1].config(text=str(i), fg='white', state=DISABLED)
                #Generates numbers across the top of the player board
                config.PcoordinateButtons[((11*i)+1)].config(text=chr(int(i+64)), fg='white', state=DISABLED)  

        createcommandWin()

    #If the vertical resolution isn't big enough the grids will be rendered side by side instead of top and bottom
    if config.root.winfo_screenheight() < 1080:

        config.root.geometry("950x500")
        
        topFrame = Frame(config.root, bg = "grey", height = 385, width = 726)
        topFrame.pack()

        #Creates a Canvas for the enemy grid to be rendered into
        enemyGrid = tk.Canvas(topFrame, height=385, width=363, bg='dark blue', highlightthickness=0)
        enemyGrid.grid(row = 0, column = 0)

        #Creates a frame to separate the enemy and player grids (None functional)
        boardSeparator = Frame(topFrame, height=363, width=20, bg='grey')
        boardSeparator.grid(row = 0, column = 1)

        #Creates a Canvas for the player grid to be rendered into
        playerGrid = tk.Canvas(topFrame, height=385, width=363, bg='dark blue', highlightthickness=0)
        playerGrid.grid(row = 0, column = 2)


    else:
        
        topFrame = Frame(config.root, bg = "grey", height = 790, width = 380)
        topFrame.pack()

        #Creates a Canvas for the enemy grid to be rendered into
        enemyGrid = tk.Canvas(topFrame, height=385, width=363, bg='dark blue', highlightthickness=0)
        enemyGrid.pack()

        #Creates a frame to separate the enemy and player grids (None functional)
        boardSeparator = Frame(topFrame, height=20, width=363, bg='grey')
        boardSeparator.pack()

        #Creates a Canvas for the player grid to be rendered into
        playerGrid = tk.Canvas(topFrame, height=385, width=363, bg='dark blue', highlightthickness=0)
        playerGrid.pack()

    config.root.after(1000, createBoard)


    def createcommandWin():
        
        def executeRotation():

            #when the rotate button is pressed 'config.currentRotation' is incremented
            if config.currentRotation == "right":
                config.currentRotation = "down"
            elif config.currentRotation == "down":
                config.currentRotation = "left"
            elif config.currentRotation == "left":
                config.currentRotation = "up"
            elif config.currentRotation == "up":
                config.currentRotation = "right"

        config.currentRotation = "right"
        
        #Creates the pop up window for firing
        config.commandWin = Toplevel(config.root)
        config.commandWin.title("Command Centre")
        config.commandWin.geometry("550x150")
        config.commandWin.configure(bg='grey')
        config.commandWin.resizable(False, False)
        config.rotationButton = Button(config.commandWin, text="ROTATE", font="Courier", command = executeRotation)
        config.rotationButton.pack(side=TOP)
        
        assets.assetsInitialisation()
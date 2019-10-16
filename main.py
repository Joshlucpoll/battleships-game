import sys
import time
import random
import tkinter as tk
from tkinter import *
import tkinter

import config

import board, assets, game


def Eclick(event=None):

    #gets the row and column of the button pressed
    buttonInfo = event.widget.grid_info()
    buttonColumn = buttonInfo['column']
    buttonRow = buttonInfo['row']

    #only allows you to click a button inside the playing area
    if buttonRow != 0 and buttonColumn != 0 and config.gameOver == False:

        #'playerFire' function is only called if the player has placed all of their ships and it's their turn
        if config.gameStartUpComplete == True and config.playersTurn == True:

            #Splits up the 'event.widget' string to just an integer which is equal to the position
            position = str(event.widget)[23:]

            #checks to see if the tile selected was already selected
            if int(position) not in config.positionsAttackedPlayer:
                
                #'playerFire' function is called when the user clicks in the enemy grid
                game.playerFire(int(position))
    

def Eenter(event=None):

    #the config.crosshair is only displayed if the player has placed all of their ships and it's their turn
    if config.gameStartUpComplete == True and config.playersTurn == True and config.gameOver == False:

        #gets the row and column of the button pressed
        buttonInfo = event.widget.grid_info()
        buttonColumn = buttonInfo['column']
        buttonRow = buttonInfo['row']

        #Splits up the 'event.widget' string to just an integer which is equal to the position
        position = str(event.widget)[23:]

        #if the button pressed is inside the playing area, that button will have it's image cleared and the image of a cross hair will replace it
        if buttonColumn != 0 and buttonRow != 0:
            if int(position) not in config.positionsAttackedPlayer:
                config.EcoordinateButtons[int(position)].config(image="")
                config.EcoordinateButtons[int(position)].config(image=config.crosshair)

def Eexit(event=None):

    #the crosshair is only removed if the player has placed all of their ships and it's their turn
    if config.gameStartUpComplete == True and config.playersTurn == True and config.gameOver == False:


        #gets the row and column of the button pressed
        buttonInfo = event.widget.grid_info()
        buttonColumn = buttonInfo['column']
        buttonRow = buttonInfo['row']

        #Splits up the 'event.widget' string to just an integer which is equal to the position
        position = str(event.widget)[23:]

        #if the button pressed is inside the playing area, that button will have it's image set back to config.sea(default)
        if buttonColumn != 0 and buttonRow != 0:
            if int(position) not in config.positionsAttackedPlayer:
                config.EcoordinateButtons[int(position)].config(image=config.sea)


def Pclick(event=None):

    #only works if the game is still in the start up phase(the player is still placing down ships)
    if config.gameStartUpComplete == False and config.gameOver == False:

        #creates a local variable of the #global version
        rotation = config.currentRotation

        #Splits up the 'event.widget' string to just an integer which is equal to the position
        position = str(event.widget)[24:]

        #'shipPlaceChooser' function is called
        assets.shipPlaceChooser(int(position), rotation)

        
def Penter(event=None):

    #gets the row and column of the button pressed
    buttonInfo = event.widget.grid_info()
    buttonColumn = buttonInfo['column']
    buttonRow = buttonInfo['row']
        
    def arrowPlacement(position):

        #only works if the game is still in the start up phase(the player is still placing down ships)
        if config.gameStartUpComplete == False:
            if config.currentRotation == "right":
                config.PcoordinateButtons[position].config(image="")
                config.PcoordinateButtons[position].config(image=config.arrowRight)
            if config.currentRotation == "down":
                config.PcoordinateButtons[position].config(image="")
                config.PcoordinateButtons[position].config(image=config.arrowDown)
            if config.currentRotation == "left":
                config.PcoordinateButtons[position].config(image="")
                config.PcoordinateButtons[position].config(image=config.arrowLeft)
            if config.currentRotation == "up":
                config.PcoordinateButtons[position].config(image="")
                config.PcoordinateButtons[position].config(image=config.arrowUp)
            
    #Splits up the 'event.widget' string to just an integer which is equal to the position
    position = str(event.widget)[24:]
                
    #Checks to see if arrow is in the playing grid
    if buttonColumn != 0 and buttonRow != 0 and config.gameOver == False and config.gameStartUpComplete == False:
        #checks to see is the arrow is on top of a rendered ship, as if it is it would delete it
        for i in range(5):
            check = int(position) in config.shipsPositions[i]
            if check == True:
                break

    
        if check == False:
                arrowPlacement(int(position))


def Pexit(event=None):

    #gets the row and column of the button pressed
    buttonInfo = event.widget.grid_info()
    buttonColumn = buttonInfo['column']
    buttonRow = buttonInfo['row']

    #Splits up the 'event.widget' string to just an integer which is equal to the position
    position = str(event.widget)[24:]


    #Checks to see if arrow is in the playing grid
    if buttonColumn != 0 and buttonRow != 0 and config.gameOver == False and config.gameStartUpComplete == False:
        #checks to see is the arrow is on top of a rendered ship, as if it is it would delete it
        for i in range(5):
            check = int(position) in config.shipsPositions[i]
            if check == True:
                break

        #if the button has no ships are under it and is in the start up phase, that button will have it's image set back to config.sea(default)
        if check == False:
            config.PcoordinateButtons[int(position)].config(image=config.sea)


def main():

    config.root = tk.Tk()
    config.root.title("Board")
    config.root.geometry("600x950")
    config.root.configure(background='grey')
    config.root.resizable(False, False)
    
    board.gameSetup()
    config.root.mainloop()

if __name__ == "__main__":
    main()
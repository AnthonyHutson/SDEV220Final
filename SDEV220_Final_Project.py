"""Authors: Anthony Hutson/Paul Alexander Kane
   Date Written: 11/29/2024
   Program Name: BriansPizzaApp.py
   This program will provide the user with an interactive GUI that will guide the user through 
   ordering menu items. The program will keep list the price amount for each order and will show
   a pay screen once an item is selected. The user will then be prompted to enter credit card information
   which will be validated and then will display whether the information is correct or not."""

    #Tools imported for GUI
import tkinter as tk
from tkinter import ttk
import re
####################WORK IN PROGRESS######################
# from PIL import ImageTK, Image
# import PIL
####################END WORK IN PROGRESS######################


    #Define Fonts for Label/Button letters
labelFont = ('Comic Sans MS', 20, 'bold')
buttonFont = ('Botthanie', 15, 'bold')

    #Super Class for frames, Defines Container for frames and defines methods for button outputs
class BriansGUI(tk.Tk):
    def __init__(self, *args):
        tk.Tk.__init__(self, *args)
        self.geometry("400x700")
        self.title("Brian's Pizza")
        self.configure(bg = 'medium sea green')

            #Container for frames
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.frames = {}
        self.frameStack = []

            #Tuple that consists of the frames displayed in the GUI
            #(Add class to this list anytime a new frame is created and implemented into GUI)    
        for F in (startPage, menuPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
    
            #Display the startPage frame anytime BriansGUI is initialized
        self.showFrame(startPage)
    
        #Method for going to the previous frame in the GUI
    def back(self):
        if self.frameStack:
            lastFrame = self.frameStack.pop()
            self.showFrame(lastFrame)
    
        #Method to display the selected frame
    def showFrame(self, cont):
        currentFrame = self.currentFrame()
        if currentFrame != cont:
            self.frameStack.append(currentFrame)
        frame = self.frames[cont]
        frame.tkraise()

        #Method to define the currentFrame variable for "showFrame" and "back" methods
    def currentFrame(self):
        for cont, frame in self.frames.items():
            if frame.winfo_viewable():
                return cont
        return
    
    #Default starting page for the app, initiated when program is ran
class startPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        ####################WORK IN PROGRESS######################
             # Image for the start page
        # logoFile = Image.open("BriansPizzaImage.jpg")
        # logoFile = logoFile.resize((200, 200))
        # logoImage = ImageTk.PhotoImage(logoFile)
        ####################END WORK IN PROGRESS######################

            #Color of background for all frames and labels
        self.configure(bg = "medium sea green")
        style = ttk.Style()
        style.configure("Style.Label", background = "medium sea green")

            #Label for startPage
        label = ttk.Label(self, text = "Brian's Pizza", style = "Style.Label", font = labelFont)
        label.place(x = 100, y = 0)

        ####################WORK IN PROGRESS######################
             # Label containing logo image
        # logoLabel = ttk.Label(self, image = logoImage)
        # logoLabel.image = logoImage
        # logoLabel.place(x = 100, y = 250)
        ####################END WORK IN PROGRESS######################
        
            #Button for quitting the app
        quitButton = ttk.Button(self, text = "Quit", command = lambda : controller.destroy())
        quitButton.place(x = 150, y = 650)

####################WORK IN PROGRESS######################
class menuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
####################END WORK IN PROGRESS######################

    #Execute the program using driver code
app = BriansGUI()
app.mainloop()
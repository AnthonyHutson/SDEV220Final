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
from PIL import Image, ImageTk
import PIL



    #Define Fonts for Label/Button letters
labelFont = ('Comic Sans MS', 20, 'bold')
buttonFont = ('Botthanie', 15, 'bold')
    #Define total tracker value
total = 0

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
        
            #Message space for Subtotal tracker
        self.subtotalLabel = ttk.Label(self, text="", font=labelFont, style="Style.Label")
        self.subtotalLabel.place(x=390, y=690)

        
            #Tuple that consists of the frames displayed in the GUI
            #(Add class to this list anytime a new frame is created and implemented into GUI)    
        for F in (startPage, menuPage, payWindow):
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
    def clearSubtotal(self, event):
        self.subtotalLabel.config(text="")

    def addSubtotal(self, event):
        self.total += price

    
    #Default starting page for the app, initiated when program is ran
class startPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

             #Image for the start page
        logoFile = Image.open("BriansPizzaImage.jpg")
        logoFile = logoFile.resize((200, 200))
        logoImage = ImageTk.PhotoImage(logoFile)

            #Label containing the logo
        logoLabel = ttk.Label(self, image = logoImage)
        logoLabel.image = logoImage
        logoLabel.place(x=100, y=250)

            #Color of background for all frames and labels
        self.configure(bg = "medium sea green")
        style = ttk.Style()
        style.configure("Style.Label", background = "medium sea green")

            #Label for startPage
        label = ttk.Label(self, text = "Brian's Pizza", style = "Style.Label", font = labelFont)
        label.place(x = 100, y = 0)

            #Button for navigating to menuPage
        menuButton = ttk.Button(self, text="Main Menu", command= lambda : controller.showFrame(payWindow))
        menuButton.place(x=150, y=600)

            #Button for quitting the app
        quitButton = ttk.Button(self, text = "Quit", command = lambda : controller.destroy())
        quitButton.place(x = 150, y = 650)


class menuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

            #Color of windown and labels
        self.configure(bg="medium sea green")
        style = ttk.Style()
        style.configure("Style.Label", background = "medium sea green")

            #Label to indicate pick up menu
        label = ttk.Label(self, text="Main Menu", font = labelFont, style="Style.Label")
        label.place(x=125, y=0)

            #Button to navigate to pizzaMenu frame
        pizzaButton = ttk.Button(self, text="Pizza", command = lambda : controller.showFrame(pizzaMenu))
        pizzaButton.place(x=50, y=600)

            #Button to navigate to wingsMenu frame
        wingsButton = ttk.Button(self, text="Wings", command = lambda : controller.showFrame(wingMenu))
        wingsButton.place(x=250, y=600)

            #Button to navigate to previous window
        backButton = ttk.Button(self, text="Back", command = lambda : controller.back())
        backButton.place(x=150, y=650)

class payWindow(tk.Frame):
    def __init__(self, parent, controller):

            #Color of window and labels  
        tk.Frame.__init__(self,parent)
        self.configure(bg="medium sea green")
        style = ttk.Style()
        style.configure("Style.Label", background="medium sea green")

            #Label to indicate payment window
        label = ttk.Label(self, text="Payment Window", font=labelFont, style="Style.Label")
        label.place(x=75,y=0)

            #Name on card entry label
        nameLabel = ttk.Label(self, text="Name on card:", font=labelFont, style="Style.Label")
        nameLabel.place(x=50, y=100)

            #Name on card entry line
        self.nameEntry = tk.Entry(self, font=('Arial', 16), width=20)
        self.nameEntry.place(x=50,y=150)

            #Card number entry label
        entryLabel = ttk.Label(self, text="Enter Credit Card Number:", font=labelFont, style="Style.Label")
        entryLabel.place(x=50,y=200)

            #Card number entry line
        self.cardEntry = tk.Entry(self, font=('Arial', 16), width=20)
        self.cardEntry.place(x=50,y=250)

            #Bind the key release event to format the card number
        self.cardEntry.bind('<KeyRelease>', self.formatCardNumber)

            #Label to display either errors or that the payment has been processed
        self.messageLabel = ttk.Label(self, text="", font=('Arial', 12, 'bold'), foreground="red", background="medium sea green")
        self.messageLabel.place(x=50,y=350)

            #Button to submit payment information
        payButton = ttk.Button(self, text="Pay", command=self.pay)
        payButton.place(x=150,y=290)

            #Button for going to the previous screen
        backButton = ttk.Button(self, text="Back", command= lambda: controller.back())
        backButton.place(x=150, y=650)

            #Button to go back to the startPage
        self.continueButton = ttk.Button(self, text="Continue", command=lambda: controller.showFrame(startPage))
        self.continueButton.place(x=150, y=650)
        self.continueButton.place_forget()
        
    def formatCardNumber(self, event):

            # Remove any non-digit characters
        card_number = ''.join(filter(str.isdigit, self.cardEntry.get()))

            # Format the card number into groups of 4 digits
        formatted_number = ' '.join(card_number[i:i + 4] for i in range(0, len(card_number), 4))

            # Update the entry with the formatted number
        self.cardEntry.delete(0, tk.END)
        self.cardEntry.insert(0, formatted_number)    

    def clearMessage(self, event):
        self.messageLabel.config(text="")
    
    def clearMessage(self, event):
        self.messageLabel.config(text="")  # Clear the message label

    def pay(self):
        customerName = self.nameEntry.get().strip()
        if not customerName:
            # Changed to use messageLabel to display error
            self.messageLabel.config(text="Error: Name on card cannot be empty.")
            return
        if not re.match(r"^[A-Za-z\s]+$", customerName):
            self.messageLabel.config(text="Error: Name can only contain letters and spaces.")
            return

        card_number = self.cardEntry.get().replace(" ", "").strip()
        if not card_number.isdigit() or len(card_number) != 16:
            self.messageLabel.config(text="Error: Invalid credit card number. \n It should be 16 digits long.")
            return

        firstName = customerName.split()[0]
        self.messageLabel.config(text=f"Processing payment for: {firstName}")
        self.continueButton.place(x=50, y=650)

    #Execute the program using driver code
app = BriansGUI()
app.mainloop()
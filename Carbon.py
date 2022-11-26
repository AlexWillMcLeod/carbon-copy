from tkinter import*
from PIL import ImageTk, Image  
import keyboard, time
import pyautogui as pya # This is for keybinds
import pyperclip  # Cross-platform Text Handler

def copy_clipboard():
    pyperclip.copy("")  # <- This prevents last copy replacing current copy of null.
    pya.hotkey('ctrl', 'c') 
    time.sleep(.2)  # Ctrl+C is usually very fast but your program may execute faster
    return pyperclip.paste() # This returns what the user has selected


def RefreshPasteDropDown(): # This will replace all of the information in the drop down for pasting, use when something new is added

    if len(CopiedList) > 1: # If there is more than one item in the list of copied item
        for i in range(len(CopiedList)): # This goes through every item in the copied list
            CreatePasteButton(i) # This creates a button for each item of information
    else: # If there is one or zero items in the copie list it will say that there is no copied items
        Error = Label(root, text="No information copied", font=(DefFont, 18), bg="gray8", fg="orangered1", justify="center")
        Error.place(relx=0.5, rely=0.25, anchor = CENTER)
        OkayButton = Button(root, text="Okay", font=(DefFont, 18), bg="gray19", fg="white", relief='flat', width = 22, activeforeground="white", activebackground="gray19",highlightthickness=0, bd=0, command = lambda: root.destroy(), height = 1).place(relx=0.5, rely = 0.29, anchor = CENTER)


def RefreshCopyDropDown(): # This will replace all of the information in the drop down menu for copying, use when something new is added

    for i in range(len(CopiedList)): # This goes through every item in the copied list
        CreateCopyButton(i) # This creates a button for each item of information


def CreatePasteButton(i): # This creates the button you can click to paste the text in the button

    if len(CopiedList[i]) > 22: # If there is more than 22 characters in the name of the text
        showedtext = (CopiedList[i])[0:22] + "..." # If there is over the 22 characters it will remove the last digits and replace them with ellipses
    else:
        showedtext = (CopiedList[i])

    if showedtext == '+': # If the item is a plus it will not add it to the list
        return

    # The below line creates the button using tkinter and configures it accordingly
    globals()["Button" + str(i)] = Button(root, text=showedtext, font=(DefFont, 18), bg="gray19", fg="white", relief='flat', width = 22, activeforeground="white", activebackground="gray19",highlightthickness=0, bd=0, command = lambda: paste(i), height = 1).place(relx=0.5, rely = (0.15 + (i * 0.05)), anchor = CENTER)

def CreateCopyButton(i):  # This creates a button that you can click and it will save your information to that slot

    if len(CopiedList[i]) > 22: # If there is more than 22 characters in the name of the text
        showedtext = (CopiedList[i])[0:22] + "..." # If there is over the 22 characters it will remove the last digits and replace them with ellipses
    else:
        showedtext = (CopiedList[i])

    fgc = 'white'

    if showedtext == '+': # If there is a plus it will have a foreground colour of orange
        fgc = "orange"
        
    # The below line creates the button using tkinter and configures it accordingly
    globals()["Button" + str(i)] = Button(root, text=showedtext, font=(DefFont, 18), bg="gray19", fg=fgc, relief='flat', width = 22, activeforeground=fgc, activebackground="gray19",highlightthickness=0, bd=0, command = lambda: copy(i), height = 1).place(relx=0.5, rely = (0.15 + (i * 0.05)), anchor = CENTER)



def paste(i): # This is the function that pastes what the user selected

    if CopiedList[i] != '+':
        root.destroy()
        keyboard.write(CopiedList[i]) # This command writes what the user selected on the keyboard

def copy(i): # This adds what the user copied to the list

    root.destroy() # This destroys the window

    copied_info = str(copy_clipboard()) # This sets what the user selected as a variable 

    if copied_info != '' and copied_info != '+' and copied_info not in CopiedList: # This checks that the user has typed something, and it has not already being stored and it is not a plus
        CopiedList[i] = copied_info # This replaces the item the user clicked on with this information
        
    elif copied_info in CopiedList: # If it has been used before it will give the user an error message

        Init()
        CarbonText.destroy()
        Error = Label(root, text="Clipboard is already copied", font=(DefFont, 18), bg="gray8", fg="orangered1", justify="center")
        Error.place(relx=0.5, rely=0.25, anchor = CENTER)
        OkayButton = Button(root, text="Okay", font=(DefFont, 18), bg="gray19", fg="white", relief='flat', width = 22, activeforeground="white", activebackground="gray19",highlightthickness=0, bd=0, command = lambda: root.destroy(), height = 1).place(relx=0.5, rely = 0.29, anchor = CENTER)
        

    if '' not in CopiedList and '+' not in CopiedList and len(CopiedList) < 17 and copied_info != '' and copied_info != '+': # If there is space for a plus and there isn't one it will create a new one
        CopiedList.append('+')







def Init(): # This initialises the window with standard settings

    global CopiedList
    global root
    global CarbonText

    root = Tk() # This creates the first window
    root.title("Carbon") # This titles it at the top 
    root.geometry("330x1080") # This chooses the size
    root.config(bg="gray8") # This makes the background colour gray
    root.attributes('-topmost', True) # This automagically focuses the window
    root.overrideredirect(True) # This removes the top window
    CarbonText = Label(root, text="Carbon", font = (DefFont, 60),bg="gray8",fg="orange") # This creates the title label at the top
    CarbonText.place(relx=0.5, rely=0.08, anchor = CENTER) # This places the label
    root.focus_force() # This also forces the focus
    root.bind("<Escape>", lambda event: root.destroy()) # Pressing escape will close the tab
    root.geometry("+0+0") # This positions it at the top left of the screen


def InitialiseCopy(): # This intialises the copy window

    Init()
    RefreshCopyDropDown()
    root.mainloop()

def InitialisePaste(): # This intialises the paste window
    
    Init()
    RefreshPasteDropDown()
    root.mainloop()



CopiedList= ['+'] # This creates the list and adds the first plus
DefFont = "Product Sans"  # This selects the default font as product sans
keyboard.add_hotkey('ctrl+win+v', InitialisePaste) # This adds the hotkey for paste
keyboard.add_hotkey('ctrl+win+c', InitialiseCopy) # This adds the hotkey for copy
keyboard.wait() # This means the program is always waiting for a keybind to be used

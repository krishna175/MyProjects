# Python program to create
# a file explorer in Tkinter
  
# import all components
# from the tkinter library
from tkinter import *
from PIL import ImageTk,Image

# import filedialog module
from tkinter import filedialog
  
# Function for opening the
# file explorer window
def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Image files",
                                                        "*.png*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    imagelocation_count = filename.rfind("/")
    global image_name
    image_name=filename[(imagelocation_count+1):]
    label_file_explorer.configure(text="File Opened: "+filename)

      


def idcard():
    home = Toplevel()

    home.configure(bg="white")
    home.title('Electrica 2.0.1')

    home.resizable(False, False)
    window_width, window_height = 500, 240

    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    home.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # readings = Image.open(f"Hari.png")
    # reading = ImageTk.PhotoImage(readings)
    # home.photo = reading  # solution for bug in `PhotoImage`
    # receipt_toplo = Label(home, image=reading, borderwidth="0")
    # receipt_toplo.place(x="37", y="300")
    splashframe = Frame(home, highlightbackground="grey", highlightthickness=3, width=110, height=140, bd="0",bg="white")
    splashframe.place(x=15, y=35)

    conentry_top = Image.open(f"{filename}")
    imagesize = conentry_top.resize((100, 130), Image.ANTIALIAS)
    entrytop = ImageTk.PhotoImage(imagesize)
    home.photo = entrytop  # solution for bug in `PhotoImage`
    receipt = Label(home, image=entrytop, borderwidth="0")
    receipt.place(x="20", y="40")
    print(image_name)
    print(filename)
    home.mainloop()

def mainwindow():
    # Create the root window
    window = Tk()

    # Set window title
    window.title('File Explorer')

    # Set window size
    window.geometry("500x500")

    #Set window background color
    window.config(background = "white")

    # Create a File Explorer label
    global label_file_explorer
    label_file_explorer = Label(window,
                                text = "",
                                width = 100, height = 4,
                                fg = "blue")


    button_explore = Button(window,
                            text = "Browse Files",
                            command = browseFiles)

    button_exit = Button(window,
                         text = "Create",
                         command = idcard)


    # readings_down = Image.open(f"Hari.png")
    # readingdown = ImageTk.PhotoImage(readings_down)
    # window.photo = readingdown  # solution for bug in `PhotoImage`
    # receipt_toplogo = Label(window, image=readingdown, borderwidth="0")
    # receipt_toplogo.place(x="37", y="300")

    # Grid method is chosen for placing
    # the widgets at respective positions
    # in a table like structure by
    # specifying rows and columns
    label_file_explorer.grid(column = 1, row = 1)

    button_explore.grid(column = 1, row = 2)

    button_exit.grid(column = 1,row = 3)

    # Let the window wait for any events
    window.mainloop()

mainwindow()
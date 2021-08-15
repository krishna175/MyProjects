import pyautogui
from tkinter import *
from PIL import ImageTk,Image

def homeWindow():
    home = Tk()

    home.configure(bg="white")
    home.title('Electrica')
    home.iconbitmap("Images/icon2.ico")
    home.resizable(False, False)
    window_width, window_height = 885, 700

    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    home.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    temp_size = Image.open("Images/home_template.png")
    temp_resized = temp_size.resize((395, 704), Image.ANTIALIAS)
    template = ImageTk.PhotoImage(temp_resized)
    template_image = Label(home, image=template, borderwidth="0")
    template_image.place(x="-3", y="-3")

    addcon_size = Image.open("Images/adconsumer_ss.png")
    addcon_resized = addcon_size.resize((220, 50), Image.ANTIALIAS)
    addcon_image = ImageTk.PhotoImage(addcon_resized)
    Label(image=addcon_image)
    button_receipt = Button(home, image=addcon_image, borderwidth="0", activebackground='blue')
    button_receipt.place(x=530, y=30)


    home.mainloop()

homeWindow()
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

    temp_size = Image.open("Images/home_template2.png")
    temp_resized = temp_size.resize((395, 704), Image.ANTIALIAS)
    template = ImageTk.PhotoImage(temp_resized)
    template_image = Label(home, image=template, borderwidth="0")
    template_image.place(x="-3", y="-3")

    backtemplate_size = Image.open("Images/backtemp1.png")
    backtemplate_resized = backtemplate_size.resize((410, 700), Image.ANTIALIAS)
    backtemplate = ImageTk.PhotoImage(backtemplate_resized)
    backtemplate_image = Label(home, image=backtemplate, borderwidth="0")
    backtemplate_image.place(x="430", y="0")

    addcon_size = Image.open("Images/adconsumer_btn.png")
    addcon_resized = addcon_size.resize((220, 50), Image.ANTIALIAS)
    addcon_image = ImageTk.PhotoImage(addcon_resized)
    Label(image=addcon_image)
    button_receipt = Button(home, image=addcon_image, borderwidth="0", activebackground='blue',command=consumerEntry)
    button_receipt.place(x=530, y=30)

    editdetails_size = Image.open("Images/edit_details_btn.png")
    editdetails_resized = editdetails_size.resize((220, 50), Image.ANTIALIAS)
    editdetails_image = ImageTk.PhotoImage(editdetails_resized)
    Label(image=editdetails_image)
    button_editreceipt = Button(home, image=editdetails_image, borderwidth="0", activebackground='blue')
    button_editreceipt.place(x=530, y=100)

    readings_size = Image.open("Images/readings_btn.png")
    readings_resized = readings_size.resize((220, 50), Image.ANTIALIAS)
    readings_image = ImageTk.PhotoImage(readings_resized)
    Label(image=readings_image)
    button_readings = Button(home, image=readings_image, borderwidth="0")
    button_readings.place(x=530, y=170)

    generatebill_size = Image.open("Images/generatebill_btn.png")
    generatebill_resized = generatebill_size.resize((220, 50), Image.ANTIALIAS)
    generatebill_image = ImageTk.PhotoImage(generatebill_resized)
    Label(image=generatebill_image)
    button_generatebill = Button(home, image=generatebill_image, borderwidth="0")
    button_generatebill.place(x=530, y=240)

    sendalert_size = Image.open("Images/sendalert_btn.png")
    sendalert_resized = sendalert_size.resize((220, 50), Image.ANTIALIAS)
    sendalert_image = ImageTk.PhotoImage(sendalert_resized)
    Label(image=sendalert_image)
    button_sendalert = Button(home, image=sendalert_image, borderwidth="0")
    button_sendalert.place(x=530, y=310)

    home.mainloop()


def consumerEntry():
    conentry = Toplevel()

    window_width, window_height = 1000, 800
    screen_width = conentry.winfo_screenwidth()
    screen_height = conentry.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    conentry.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    conentry.title("CONSUMER DETAILS ENTRY")
    conentry.configure(bg="white")
    conentry.resizable(width=False, height=False)
    conentry.iconbitmap('Images/icon2.ico')

    conentry_top = Image.open("Images/adcon_toptemp.png")
    entrytop = ImageTk.PhotoImage(conentry_top)
    conentry.photo = entrytop  # solution for bug in `PhotoImage`
    receipt_toplogo = Label(conentry, image=entrytop, borderwidth="0")
    receipt_toplogo.place(x="37", y="2")

    con_name = Label(conentry, text="Name : ", font="lucida 12 bold ", bg="white", fg="blue4")
    con_name.place(x="300", y="150")
    conname_entry = Entry(conentry, width="40", font="lucida 12", bd="3", bg="grey94")
    conname_entry.place(x="380", y="150")

    conphone = Label(conentry, text="Phone No : ", font="lucida 12 bold ", bg="white", fg="blue4")
    conphone.place(x="300", y="200")
    conphone_entry = Entry(conentry, width="20", font="lucida 12", bd="3", bg="grey94")
    conphone_entry.place(x="425", y="200")

    conentry.mainloop()


homeWindow()
import pyautogui
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import cx_Oracle
import pygetwindow
import webbrowser
from plyer import notification
import time
from pdf_mail import sendpdf
import datetime
import smtplib
from email.message import EmailMessage
from fpdf import FPDF



def notifyrecmail():
    messagebox.showinfo("Message","Mail send successfully!")
    sendsplash.destroy()


def billingSplash():
    billing = Toplevel()
    window_width, window_height = 300, 100
    screen_width = billing.winfo_screenwidth()
    screen_height = billing.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    billing.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    billing.configure(bg="white")
    billing.resizable(width=False, height=False)
    billing.overrideredirect(True)

    splashframe = Frame(billing, highlightbackground="black", highlightthickness=3, width=300, height=110, bd="0",bg="white")
    splashframe.pack()



    file = "Images/preloader.gif"

    info = Image.open(file)

    frames = info.n_frames  # gives total number of frames that gif contains

    # creating list of PhotoImage objects for each frames
    im = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]

    count = 0
    anim = None

    def animation(count):
        global anim
        im2 = im[count]

        gif_label.configure(image=im2)
        count += 1
        if count == frames:
            count = 0
        anim = billing.after(500, lambda: animation(count))

    gif_label = Label(billing, image="", bd="0")
    gif_label.place(x="75", y="25")
    animation(count)

    sending_label = Label(billing, text="Generating Bill...", font="lucida 8 ", bg="white", fg="black")
    sending_label.place(x="100", y="53")
    loading_label = Label(billing, text="Please wait", font="lucida 8 ", bg="white", fg="black")
    loading_label.place(x="110", y="72")
    billing.after(5000,notifyrecmail)

    billing.mainloop()

def sendmailsplash():
    global sendsplash
    sendsplash = Toplevel()
    window_width, window_height = 300, 100
    screen_width = sendsplash.winfo_screenwidth()
    screen_height = sendsplash.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    sendsplash.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    sendsplash.configure(bg="white")
    sendsplash.resizable(width=False, height=False)
    sendsplash.overrideredirect(True)

    splashframe = Frame(sendsplash, highlightbackground="black", highlightthickness=3, width=300, height=110, bd="0",bg="white")
    splashframe.pack()






    file = "Images/loader2.gif"

    info = Image.open(file)

    frames = info.n_frames  # gives total number of frames that gif contains

    # creating list of PhotoImage objects for each frames
    im = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]

    count = 0
    anim = None

    def animation(count):
        global anim
        im2 = im[count]

        gif_label.configure(image=im2)
        count += 1
        if count == frames:
            count = 0
        anim = sendsplash.after(50, lambda: animation(count))

    gif_label = Label(sendsplash, image="", bd="0")
    gif_label.place(x="110", y="3")
    animation(count)

    sending_label = Label(sendsplash, text="Sending...", font="lucida 8 ", bg="white", fg="black")
    sending_label.place(x="117", y="55")
    loading_label = Label(sendsplash, text="Please wait", font="lucida 8 ", bg="white", fg="black")
    loading_label.place(x="110", y="74")
    sendsplash.after(3000, sendmail)

    sendsplash.mainloop()


def sendmail():
    con = cx_Oracle.connect('system/12345@localhost:1521/xe')
    cursor = con.cursor()
    x = cursor.execute("SELECT * FROM ADD_CONSUMER WHERE CON_ID = (SELECT MAX(CON_ID) FROM ADD_CONSUMER)")
    values = x.fetchall()
    for i in values:
        name = i[1]
        supply = i[10]
        requrement = i[14]
        email = i[7]
        # Create an object of sendpdf function
        k = sendpdf("electrica.org@gmail.com",
                    f"{email}",
                    "Electrica@1234",
                    "Electrica New Connection",
                    f"Dear {name} ,\nYour connection request for {supply} ({requrement}) current supply has been approved.\nConnection will be established within 24hrs.\n\nRegards,\nElectrica",
                    "Receipt",
                    "C:/Users/Vandana/Documents/Clg Doc/OneDrive/ProjectGit/Electrica")

    # sending an email
        k.email_send()
        notifyrecmail()

# SEND MAIL AFTER UPDATING

def editmailsplash():
    global sendsplash
    sendsplash = Toplevel()
    window_width, window_height = 300, 100
    screen_width = sendsplash.winfo_screenwidth()
    screen_height = sendsplash.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    sendsplash.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    sendsplash.configure(bg="white")
    sendsplash.resizable(width=False, height=False)
    sendsplash.overrideredirect(True)

    splashframe = Frame(sendsplash, highlightbackground="black", highlightthickness=3, width=300, height=110, bd="0",bg="white")
    splashframe.pack()






    file = "Images/loader2.gif"

    info = Image.open(file)

    frames = info.n_frames  # gives total number of frames that gif contains

    # creating list of PhotoImage objects for each frames
    im = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]

    count = 0
    anim = None

    def animation(count):
        global anim
        im2 = im[count]

        gif_label.configure(image=im2)
        count += 1
        if count == frames:
            count = 0
        anim = sendsplash.after(50, lambda: animation(count))

    gif_label = Label(sendsplash, image="", bd="0")
    gif_label.place(x="110", y="3")
    animation(count)

    sending_label = Label(sendsplash, text="Sending...", font="lucida 8 ", bg="white", fg="black")
    sending_label.place(x="117", y="55")
    loading_label = Label(sendsplash, text="Please wait", font="lucida 8 ", bg="white", fg="black")
    loading_label.place(x="110", y="74")
    sendsplash.after(3000, ssformail)

    sendsplash.mainloop()



def ssformail():
    sendsplash.destroy()
    path = "C:/Users/Vandana/Documents/Clg Doc/OneDrive/ProjectGit/Electrica/Receipt_img.png"
    titles =pygetwindow.getAllTitles()

    # x1, y1 = width, height = pygetwindow.getWindowsWithTitle('Patholab')
    window = pygetwindow.getWindowsWithTitle('RECEIPT')[0]
    x1 = window.left+10
    y1 = window.top+30
    height = window.height-150
    width = window.width-20
    x2 = x1 + width
    y2 = y1 + height

    pyautogui.screenshot(path)

    im = Image.open(path)
    im = im.crop((x1,y1,x2,y2))
    im.save(path)
    # im.show(path)
    sstopdfformail()

def sstopdfformail():
    filename = "C:/Users/Vandana/Documents/Clg Doc/OneDrive/ProjectGit/Electrica/Receipt_img.png"
    image = Image.open(filename)

    if image.mode == "RGBA":
        image = image.convert("RGB")
    output = "C:/Users/Vandana/Documents/Clg Doc/OneDrive/ProjectGit/Electrica/Receipt.pdf"
    image.save(output, "PDF", resolution=100.0)
    sendeditmail()

def sendeditmail():
    identered = id_entry.get()
    con = cx_Oracle.connect('system/12345@localhost:1521/xe')
    cursor = con.cursor()
    x = cursor.execute(f"SELECT * FROM ADD_CONSUMER WHERE CON_ID = {identered}")
    values = x.fetchall()
    for i in values:
        name = i[1]
        supply = i[10]
        requrement = i[14]
        email = i[7]
        # Create an object of sendpdf function
        k = sendpdf("electrica.org@gmail.com",
                    f"{email}",
                    "Electrica@1234",
                    "Electrica New Connection",
                    f"Dear {name} ,\nYour connection request for {supply} ({requrement}) current supply has been approved.\nConnection will be established within 24hrs.\n\nRegards,\nElectrica",
                    "Receipt",
                    "C:/Users/Vandana/Documents/Clg Doc/OneDrive/ProjectGit/Electrica")

        # sending an email
        k.email_send()
        notifyrecmail()

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
    button_editreceipt = Button(home, image=editdetails_image, borderwidth="0", activebackground='blue',command=editwindow)
    button_editreceipt.place(x=530, y=100)

    readings_size = Image.open("Images/readings_btn.png")
    readings_resized = readings_size.resize((220, 50), Image.ANTIALIAS)
    readings_image = ImageTk.PhotoImage(readings_resized)
    Label(image=readings_image)
    button_readings = Button(home, image=readings_image, borderwidth="0",activebackground="blue",command=enterReadings)
    button_readings.place(x=530, y=170)

    generatebill_size = Image.open("Images/generatebill_btn.png")
    generatebill_resized = generatebill_size.resize((220, 50), Image.ANTIALIAS)
    generatebill_image = ImageTk.PhotoImage(generatebill_resized)
    Label(image=generatebill_image)
    button_generatebill = Button(home, image=generatebill_image, borderwidth="0",command=billingSplash)
    button_generatebill.place(x=530, y=240)

    sendalert_size = Image.open("Images/sendalert_btn.png")
    sendalert_resized = sendalert_size.resize((220, 50), Image.ANTIALIAS)
    sendalert_image = ImageTk.PhotoImage(sendalert_resized)
    Label(image=sendalert_image)
    button_sendalert = Button(home, image=sendalert_image, borderwidth="0",command=alerts)
    button_sendalert.place(x=530, y=310)

    defaulter_size = Image.open("Images/defaulters_btn.png")
    defaulter_resized = defaulter_size.resize((220, 50), Image.ANTIALIAS)
    defaulter_image = ImageTk.PhotoImage(defaulter_resized)
    Label(image=defaulter_image)
    button_defaulter = Button(home, image=defaulter_image, borderwidth="0")
    button_defaulter.place(x=530, y=380)

    fraud_size = Image.open("Images/sendbill_btn.png")
    fraud_resized = fraud_size.resize((220, 50), Image.ANTIALIAS)
    fraud_image = ImageTk.PhotoImage(fraud_resized)
    Label(image=fraud_image)
    button_fraud = Button(home, image=fraud_image, borderwidth="0",command=sendbill)
    button_fraud.place(x=530, y=450)

    payment_size = Image.open( "Images/payment_btn.png")
    payment_resized = payment_size.resize((220, 50), Image.ANTIALIAS)
    payment_image = ImageTk.PhotoImage(payment_resized)
    Label(image=payment_image)
    button_payment = Button(home, image=payment_image, borderwidth="0",command=billPayment)
    button_payment.place(x=530, y=520)

    home.mainloop()


def consumerEntry():
    global conentry
    conentry = Toplevel()
    global conname_entry, conphone_entry, address1_entry, address2_entry, address3_entry, pincode_entry, email_entry, aadhar_entry, pan_entry, click,click2, var, meter_entry
    window_width, window_height = 1000, 950
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

    conentry_left = Image.open("Images/charges2.png")
    entryleft = ImageTk.PhotoImage(conentry_left)
    conentry.photo = entryleft  # solution for bug in `PhotoImage`
    receipt_leftcharges = Label(conentry, image=entryleft, borderwidth="0")
    receipt_leftcharges.place(x="70", y="230")

    entrydown = Image.open("Images/adcon_downtempnew.png")
    entrydown = ImageTk.PhotoImage(entrydown)
    conentry.photo = entrydown  # solution for bug in `PhotoImage`
    receipt_toplogo = Label(conentry, image=entrydown, borderwidth="0")
    receipt_toplogo.place(x="37", y="820")



    con_name = Label(conentry, text="Name                           : ", font="lucida 12 bold ", bg="white", fg="blue4")
    con_name.place(x="300", y="150")
    conname_entry = Entry(conentry, width="32", font="lucida 12", bd="3", bg="grey94")
    conname_entry.place(x="530", y="150")

    conphone = Label(conentry, text="Phone No                    :", font="lucida 12 bold ", bg="white", fg="blue4")
    conphone.place(x="300.5", y="200")
    conphone_entry = Entry(conentry, width="20", font="lucida 12", bd="3", bg="grey94")
    conphone_entry.place(x="530", y="200")

    address_label = Label(conentry, text="Address :",font="lucida 12 bold underline", bg="white")
    address_label.place(x="300", y="250")



    address1_label = Label(conentry, text="Flat, House no./ Company  :",font="lucida 10 bold",bg="white",fg="blue4")
    address1_label.place(x="300",y="290")
    address1_entry = Entry(conentry, width="35", font="lucida 11", bd="3", bg="grey94")
    address1_entry.place(x="530", y="290")

    address2_label = Label(conentry, text="Area, Street, Village           :", font="lucida 10 bold", bg="white", fg="blue4")
    address2_label.place(x="301", y="330")
    address2_entry = Entry(conentry, width="35", font="lucida 11", bd="3", bg="grey94")
    address2_entry.place(x="530", y="330")

    address3_label = Label(conentry, text="Landmark, Town/City         :", font="lucida 10 bold", bg="white", fg="blue4")
    address3_label.place(x="300", y="370")
    address3_entry = Entry(conentry, width="35", font="lucida 11", bd="3", bg="grey94")
    address3_entry.place(x="530", y="370")

    pincode_label = Label(conentry, text="Pincode                              :", font="lucida 10 bold", bg="white", fg="blue4")
    pincode_label.place(x="300", y="410")
    pincode_entry = Entry(conentry, width="14", font="lucida 11", bd="3", bg="grey94")
    pincode_entry.place(x="530", y="410")

    email_label = Label(conentry, text="Email                           :",font="lucida 12 bold" ,bg="white",fg="blue4")
    email_label.place(x="300",y="460")
    email_entry = Entry(conentry, width="30", font="lucida 12", bd="3", bg="grey94")
    email_entry.place(x="530", y="460")

    aadhar_label = Label(conentry, text="Aadhar No                   :",font="lucida 12 bold", bg="white",fg="blue4")
    aadhar_label.place(x="300",y="510")
    aadhar_entry = Entry(conentry, width="13", font="lucida 12", bd="3", bg="grey94")
    aadhar_entry.place(x="530", y="510")

    pan_label = Label(conentry, text="PAN                             : ", font="lucida 12 bold", bg="white", fg="blue4")
    pan_label.place(x="300", y="560")
    pan_entry = Entry(conentry, width="13", font="lucida 12", bd="3", bg="grey94")
    pan_entry.place(x="530", y="560")

    supplytype_label = Label(conentry, text="Supply Type                :", font="lucida 12 bold", bg="white", fg="blue4")
    supplytype_label.place(x="300", y="610")
    list1 = ['SINGLE PHASE','THREE PHASE']
    click = StringVar()
    click.set("Select Type")
    type_dropdown = OptionMenu(conentry, click, *list1)
    type_dropdown.config(bg="blue4", fg="white", width="12", activebackground="dodger blue", activeforeground="black")
    type_dropdown.place(x="530", y="605")

    list2 = ['Up to 5 kW', '5-10 kW','10-20 kW','20-50 kW','50-150 kW','Above 150 kW']
    click2 = StringVar()
    click2.set("Select Requirement")
    test_dropdown = OptionMenu(conentry, click2, *list2)
    test_dropdown.config(bg="blue4", fg="white", width="15", activebackground="dodger blue", activeforeground="black")
    test_dropdown.place(x="690", y="605")

    usage_label = Label(conentry, text="Purpose of Supply      :", font="lucida 12 bold", bg="white", fg="blue4")
    usage_label.place(x="301", y="660")
    var = StringVar()
    domsymbol = Image.open("Images/domesticss_btn.png")
    domsymbol = ImageTk.PhotoImage(domsymbol)
    conentry.photo = domsymbol  # solution for bug in `PhotoImage`
    domestic_radio = Radiobutton(conentry, image=domsymbol, variable=var, bg="white", fg="blue", font="2", value="DOMESTIC",bd="0",activebackground="white")
    domestic_radio.place(x="530", y="650")

    indsymbol = Image.open("Images/industrialss_btn.png")
    indsymbol = ImageTk.PhotoImage(indsymbol)
    conentry.photo = indsymbol  # solution for bug in `PhotoImage`
    industry_radio = Radiobutton(conentry, image=indsymbol, variable=var, bg="white", fg="blue", font="2", value="INDUSTRIAL", bd="0", activebackground="white")
    industry_radio.place(x="600", y="650")

    meter_label = Label(conentry, text="Meter No                     : ", font="lucida 12 bold", bg="white", fg="blue4")
    meter_label.place(x="300", y="710")
    meter_entry = Entry(conentry, width="13", font="lucida 12", bd="3", bg="grey94")
    meter_entry.place(x="530", y="710")

    global declare
    declare=IntVar()
    declaration = Checkbutton(conentry,text="   I hereby declare that the information given in this application is true and correct to  \n best of my knowledge and belief.In case any information given in this application \n     proves to be false or incorrect, I shall be responsible for the consequences.               ",variable=declare,font="lucida 7 ",bg="white",fg="red")
    declaration.place(x="300",y="755")

    submitsymbol = Image.open("Images/submit_button.png")
    submitsymbol = ImageTk.PhotoImage(submitsymbol)
    conentry.photo3 = submitsymbol
    submit_receipt = Button(conentry, image=submitsymbol, bg="white", bd="0", activebackground='green',command=submit)
    submit_receipt.place(x="825", y="765")


    conentry.mainloop()

def submit():
    declaration = declare.get()
    if(declaration==0):
        messagebox.showinfo("Message", "Please select the declaration Checkbox")
    else:
        addconsumerdb()

def addconsumerdb():
    # conname_entry, conphone_entry, address1_entry, address2_entry, address3_entry, pincode_entry, email_entry, aadhar_entry, pan_entry, click, var, meter_entry



    name = conname_entry.get()
    phone = conphone_entry.get()
    address1 = address1_entry.get()
    address2 = address2_entry.get()
    address3 = address3_entry.get()
    pincode = pincode_entry.get()
    email = email_entry.get()
    aadhar = aadhar_entry.get()
    pan = pan_entry.get()
    supply = click.get()
    pos = var.get()
    meterno = meter_entry.get()
    requirement = click2.get()

    if (supply == 'SINGLE PHASE' and (requirement=='Up to 5 kW' or requirement=='5-10 kW')):
        cc = 2050
    elif (supply == 'THREE PHASE' and requirement=='10-20 kW'):
        cc = 4575
    elif  (supply == 'THREE PHASE' and requirement=='20-50 kW'):
        cc = 6575
    elif (supply == 'THREE PHASE' and requirement=='50-150 kW'):
        cc = 12075
    elif (supply == 'THREE PHASE' and requirement=='Above 150 kW'):
        cc = 250075
    else:
        cc = 2050
    try:
        con = cx_Oracle.connect('system/12345@localhost:1521/xe')
        print(con.version)
        cursor = con.cursor()
        cursor.execute(f"INSERT INTO ADD_CONSUMER VALUES(consumer_seq.nextval,'{name}',{phone},'{address1}','{address2}','{address3}',{pincode},'{email}',{aadhar},'{pan}','{supply}','{pos}',{meterno},sysdate,'{requirement}',{cc})")
        messagebox.showinfo("Message", "Consumer Added Successfully")
        cursor.close()
        con.commit()
        print('Consumer added!')
        displayentry()
        con.close()
    except Exception as e:
        messagebox.showerror("Error","Some error occured.\n\n⭕ Enter valid details. \n⭕ Fields should not be empty.")



#print the consuemr receipt
def printrec():
    path = "C:/Users/Vandana/Documents/Clg Doc/OneDrive/ProjectGit/Electrica/Receipt_img.png"
    titles =pygetwindow.getAllTitles()

    # x1, y1 = width, height = pygetwindow.getWindowsWithTitle('Patholab')
    window = pygetwindow.getWindowsWithTitle('RECEIPT')[0]
    x1 = window.left+10
    y1 = window.top+30
    height = window.height-150
    width = window.width-20
    x2 = x1 + width
    y2 = y1 + height

    pyautogui.screenshot(path)

    im = Image.open(path)
    im = im.crop((x1,y1,x2,y2))
    im.save(path)
    # im.show(path)
    sstopdf()

def sstopdf():
    filename = "C:/Users/Vandana/Documents/Clg Doc/OneDrive/ProjectGit/Electrica/Receipt_img.png"
    image = Image.open(filename)

    if image.mode == "RGBA":
        image = image.convert("RGB")
    output = "C:/Users/Vandana/Documents/Clg Doc/OneDrive/ProjectGit/Electrica/Receipt.pdf"
    image.save(output, "PDF", resolution=100.0)
    printreceipt()

def printreceipt():
    webbrowser.open_new(r'file://C:/Users/Vandana/Documents/Clg Doc/OneDrive/ProjectGit/Electrica/Receipt.pdf')


def displayentry():
    conentry.destroy()
    condisplay = Toplevel()
    window_width, window_height = 1000, 950
    screen_width = condisplay.winfo_screenwidth()
    screen_height = condisplay.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    condisplay.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    condisplay.title("RECEIPT")
    condisplay.configure(bg="white")
    condisplay.resizable(width=False, height=False)
    condisplay.iconbitmap('Images/icon2.ico')

    conentry_top = Image.open("Images/adcon_toptemp.png")
    entrytop = ImageTk.PhotoImage(conentry_top)
    condisplay.photo = entrytop  # solution for bug in `PhotoImage`
    receipt_toplogo = Label(condisplay, image=entrytop, borderwidth="0")
    receipt_toplogo.place(x="37", y="2")

    iddisplay = Image.open("Images/iddisplaynew.png")
    iddislpayleft = ImageTk.PhotoImage(iddisplay)
    condisplay.photo = iddislpayleft  # solution for bug in `PhotoImage`
    iddisplay_leftcharges = Label(condisplay, image=iddislpayleft, borderwidth="0")
    iddisplay_leftcharges.place(x="70", y="230")

    con_name = Label(condisplay, text="Connection Charges :  ", font="lucida 9 bold ", bg="white",fg="red")
    con_name.place(x="75", y="290")

    conentry_left = Image.open("Images/connectionchageimg.png")
    entryleft = ImageTk.PhotoImage(conentry_left)
    condisplay.photo = entryleft  # solution for bug in `PhotoImage`
    receipt_leftcharges = Label(condisplay, image=entryleft, borderwidth="0")
    receipt_leftcharges.place(x="70", y="310")

    gpay_logo = Image.open("Images/payment_image.png")
    gpay_logo = ImageTk.PhotoImage(gpay_logo)
    condisplay.photo2 = gpay_logo  # solution for bug in `PhotoImage`
    rec_gpay_logo = Label(condisplay, image=gpay_logo, borderwidth="0", bg="white")
    rec_gpay_logo.place(x="100", y="510")

    entrydown = Image.open("Images/adcon_downtempnew.png")
    entrydown = ImageTk.PhotoImage(entrydown)
    condisplay.photo = entrydown  # solution for bug in `PhotoImage`
    receipt_toplogo = Label(condisplay, image=entrydown, borderwidth="0")
    receipt_toplogo.place(x="37", y="720")



    con_name = Label(condisplay, text="Name                           : ", font="lucida 12 bold ", bg="white", fg="blue4")
    con_name.place(x="300", y="150")


    conphone = Label(condisplay, text="Phone No                    :", font="lucida 12 bold ", bg="white", fg="blue4")
    conphone.place(x="300.5", y="200")


    address_label = Label(condisplay, text="Address                      :", font="lucida 12 bold ", bg="white",fg="blue4")
    address_label.place(x="301", y="250")


    email_label = Label(condisplay, text="Email                           :", font="lucida 12 bold", bg="white",fg="blue4")
    email_label.place(x="300", y="400")


    aadhar_label = Label(condisplay, text="Aadhar No                   :", font="lucida 12 bold", bg="white", fg="blue4")
    aadhar_label.place(x="300", y="450")


    pan_label = Label(condisplay, text="PAN                             : ", font="lucida 12 bold", bg="white",fg="blue4")
    pan_label.place(x="300", y="500")


    supplytype_label = Label(condisplay, text="Supply Type                :", font="lucida 12 bold", bg="white",fg="blue4")
    supplytype_label.place(x="300", y="550")


    usage_label = Label(condisplay, text="Purpose of Supply      :", font="lucida 12 bold", bg="white", fg="blue4")
    usage_label.place(x="301", y="600")


    meter_label = Label(condisplay, text="Meter No                     : ", font="lucida 12 bold", bg="white", fg="blue4")
    meter_label.place(x="300", y="650")



    #CONNECTION DB

    con = cx_Oracle.connect('system/12345@localhost:1521/xe')
    cursor = con.cursor()
    x = cursor.execute("SELECT * FROM ADD_CONSUMER WHERE CON_ID = (SELECT MAX(CON_ID) FROM ADD_CONSUMER)")
    values = x.fetchall()
    for i in values:
        con_iddis = Label(condisplay, text=i[0], font="lucida 13 bold ", bg="midnight blue", fg="white")
        con_iddis.place(x="170", y="240")

        con_namedis = Label(condisplay, text= i[1], font="lucida 12 bold ", bg="white", fg="black")
        con_namedis.place(x="530", y="152")

        conphonedis = Label(condisplay, text= i[2], font="lucida 12 bold ", bg="white", fg="black")
        conphonedis.place(x="530", y="202")

        address1 = Label(condisplay, text= i[3], font="lucida 11 bold ", bg="white", fg="black")
        address1.place(x="530", y="252")
        address2 = Label(condisplay, text= i[4], font="lucida 11 bold ", bg="white", fg="black")
        address2.place(x="530", y="280")
        address3 = Label(condisplay, text= i[5], font="lucida 11 bold ", bg="white", fg="black")
        address3.place(x="530", y="310")
        pincode = Label(condisplay, text=f"PINCODE : {i[6]}", font="lucida 11 bold ", bg="white", fg="black")
        pincode.place(x="530", y="340")

        emaildis = Label(condisplay, text= i[7], font="lucida 11 bold ", bg="white",fg="black")
        emaildis.place(x="530", y="400")

        aadhardis = Label(condisplay, text= i[8], font="lucida 11 bold ", bg="white", fg="black")
        aadhardis.place(x="530", y="450")

        pandis = Label(condisplay, text= i[9], font="lucida 11 bold ", bg="white", fg="black")
        pandis.place(x="530", y="500")

        supplytypedis = Label(condisplay, text= i[10]+ f" ({i[14]})", font="lucida 11 bold ", bg="white", fg="black")
        supplytypedis.place(x="530", y="550")

        usagedis = Label(condisplay, text= i[11], font="lucida 11 bold ", bg="white", fg="black")
        usagedis.place(x="530", y="600")

        meterdis = Label(condisplay, text= i[12], font="lucida 11 bold ", bg="white", fg="black")
        meterdis.place(x="530", y="650")

        total_amount = i[15]
        supplytypeamount = total_amount%100
        cc_amount = total_amount - supplytypeamount
        stcharge = Label(condisplay, text=supplytypeamount, font="lucida 11 bold ", bg="goldenrod1", fg="black")
        stcharge.place(x="185", y="343")

        cc = Label(condisplay, text=cc_amount, font="lucida 11 bold ", bg="goldenrod1", fg="black")
        cc.place(x="185", y="394")

        cctotal = Label(condisplay, text=total_amount, font="lucida 11 bold ", bg="goldenrod1", fg="black")
        cctotal.place(x="185", y="433")

        gpayamount = Label(condisplay, text=f"Amount : {total_amount} Rs", font="lucida 11 bold ", bg="white", fg="black")
        gpayamount.place(x="80", y="670")




    y = cursor.execute("SELECT to_char(JOINDATE,'DD-MON-YYYY'),to_char(JOINDATE,'hh24:mi') FROM ADD_CONSUMER WHERE CON_ID = (SELECT MAX(CON_ID) FROM ADD_CONSUMER)")
    time_date = y.fetchall()
    for i in time_date:

        date_label = Label(condisplay, text=f"{i[0]} |", font="lucida 9 bold ", bg="white", fg="black")
        date_label.place(x="800", y="120")

        time_label = Label(condisplay, text=i[1], font="lucida 9 bold ", bg="white", fg="black")
        time_label.place(x="900", y="120")

    cursor.close()
    con.close()

    printbtn = Image.open("Images/print_btn.png")
    printbtn = ImageTk.PhotoImage(printbtn)
    condisplay.photo3 = printbtn
    submit_receipt = Button(condisplay, image=printbtn, bg="white", bd="0", activebackground='green',command=printrec)
    submit_receipt.place(x="370", y="850")

    mailbtn = Image.open("Images/mail_btn.png")
    mailbtn = ImageTk.PhotoImage(mailbtn)
    condisplay.photo3 = mailbtn
    submit_receipt = Button(condisplay, image=mailbtn, bg="white", bd="0", activebackground='green',command=sendmailsplash)
    submit_receipt.place(x="530", y="850")

    print("Consumer details displayed")

    condisplay.mainloop()

def editwindow():
    editentry = Toplevel()
    global id_entry
    window_width, window_height = 583,430
    screen_width = editentry.winfo_screenwidth()
    screen_height = editentry.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    editentry.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    editentry.title("EDIT DETAILS")
    editentry.configure(bg="white")
    editentry.resizable(width=False, height=False)
    editentry.iconbitmap('Images/icon2.ico')


    bg_logo = Image.open("Images/editwindowbg.png")
    bg_logo = ImageTk.PhotoImage(bg_logo)
    editentry.photo2 = bg_logo  # solution for bug in `PhotoImage`
    background_logo = Label(editentry, image=bg_logo, borderwidth="0", bg="white")
    background_logo.place(x="0", y="0")

    id_label = Label(editentry, text="CON_ID : ", font="lucida 14 bold ", bg="goldenrod1", fg="black")
    id_label.place(x="185", y="100")

    id_entry = Entry(editentry, width="8", font="lucida 12 bold", bd="3", bg="grey94")
    id_entry.place(x="300", y="102")

    showdetailsbtn = Image.open("Images/showdetails_btn2.png")
    showdetailsbtn = ImageTk.PhotoImage(showdetailsbtn)
    editentry.photo3 = showdetailsbtn
    submit_receipt = Button(editentry, image=showdetailsbtn, bg="goldenrod1", bd="0", activebackground='green',command=showentry)
    submit_receipt.place(x="190", y="170")

    editdetailsbtn = Image.open("Images/editdetails_btn.png")
    editdetailsbtn = ImageTk.PhotoImage(editdetailsbtn)
    editentry.photo3 = editdetailsbtn
    submit_receipt = Button(editentry, image=editdetailsbtn, bg="goldenrod1", bd="0", activebackground='green',command=editentries)
    submit_receipt.place(x="190", y="220")

    deletedetailsbtn = Image.open("Images/delete_details_btn.png")
    deletedetailsbtn = ImageTk.PhotoImage(deletedetailsbtn)
    editentry.photo3 = deletedetailsbtn
    submit_receipt = Button(editentry, image=deletedetailsbtn, bg="goldenrod1", bd="0", activebackground='green',command=security)
    submit_receipt.place(x="190", y="270")
    editentry.mainloop()



def showentry():
    # conentry.destroy()
    try:
        identered = id_entry.get()
        con = cx_Oracle.connect('system/12345@localhost:1521/xe')
        cursor = con.cursor()
        x = cursor.execute(f"SELECT COUNT(*) FROM ADD_CONSUMER WHERE CON_ID={identered} ")
        list1 = x.fetchall()
        for i in list1:
            if (i[0] == 0):
                messagebox.showerror("Error", f"CON_ID {identered} Does not exist. ")
                break
            else:
                condisplay = Toplevel()
                window_width, window_height = 1000, 950
                screen_width = condisplay.winfo_screenwidth()
                screen_height = condisplay.winfo_screenheight()
                position_top = int(screen_height / 2 - window_height / 2)
                position_right = int(screen_width / 2 - window_width / 2)
                condisplay.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

                condisplay.title("RECEIPT")
                condisplay.configure(bg="white")
                condisplay.resizable(width=False, height=False)
                condisplay.iconbitmap('Images/icon2.ico')

                conentry_top = Image.open("Images/adcon_toptemp.png")
                entrytop = ImageTk.PhotoImage(conentry_top)
                condisplay.photo = entrytop  # solution for bug in `PhotoImage`
                receipt_toplogo = Label(condisplay, image=entrytop, borderwidth="0")
                receipt_toplogo.place(x="37", y="2")

                iddisplay = Image.open("Images/iddisplaynew.png")
                iddislpayleft = ImageTk.PhotoImage(iddisplay)
                condisplay.photo = iddislpayleft  # solution for bug in `PhotoImage`
                iddisplay_leftcharges = Label(condisplay, image=iddislpayleft, borderwidth="0")
                iddisplay_leftcharges.place(x="70", y="230")

                con_name = Label(condisplay, text="Connection Charges :  ", font="lucida 9 bold ", bg="white",fg="red")
                con_name.place(x="75", y="290")

                conentry_left = Image.open("Images/connectionchageimg.png")
                entryleft = ImageTk.PhotoImage(conentry_left)
                condisplay.photo = entryleft  # solution for bug in `PhotoImage`
                receipt_leftcharges = Label(condisplay, image=entryleft, borderwidth="0")
                receipt_leftcharges.place(x="70", y="310")

                gpay_logo = Image.open("Images/payment_image.png")
                gpay_logo = ImageTk.PhotoImage(gpay_logo)
                condisplay.photo2 = gpay_logo  # solution for bug in `PhotoImage`
                rec_gpay_logo = Label(condisplay, image=gpay_logo, borderwidth="0", bg="white")
                rec_gpay_logo.place(x="100", y="510")

                entrydown = Image.open("Images/adcon_downtempnew.png")
                entrydown = ImageTk.PhotoImage(entrydown)
                condisplay.photo = entrydown  # solution for bug in `PhotoImage`
                receipt_toplogo = Label(condisplay, image=entrydown, borderwidth="0")
                receipt_toplogo.place(x="37", y="720")



                con_name = Label(condisplay, text="Name                           : ", font="lucida 12 bold ", bg="white", fg="blue4")
                con_name.place(x="300", y="150")


                conphone = Label(condisplay, text="Phone No                    :", font="lucida 12 bold ", bg="white", fg="blue4")
                conphone.place(x="300.5", y="200")


                address_label = Label(condisplay, text="Address                      :", font="lucida 12 bold ", bg="white",fg="blue4")
                address_label.place(x="301", y="250")


                email_label = Label(condisplay, text="Email                           :", font="lucida 12 bold", bg="white",fg="blue4")
                email_label.place(x="300", y="400")


                aadhar_label = Label(condisplay, text="Aadhar No                   :", font="lucida 12 bold", bg="white", fg="blue4")
                aadhar_label.place(x="300", y="450")


                pan_label = Label(condisplay, text="PAN                             : ", font="lucida 12 bold", bg="white",fg="blue4")
                pan_label.place(x="300", y="500")


                supplytype_label = Label(condisplay, text="Supply Type                :", font="lucida 12 bold", bg="white",fg="blue4")
                supplytype_label.place(x="300", y="550")


                usage_label = Label(condisplay, text="Purpose of Supply      :", font="lucida 12 bold", bg="white", fg="blue4")
                usage_label.place(x="301", y="600")


                meter_label = Label(condisplay, text="Meter No                     : ", font="lucida 12 bold", bg="white", fg="blue4")
                meter_label.place(x="300", y="650")

                printbtn = Image.open("Images/print_btn.png")
                printbtn = ImageTk.PhotoImage(printbtn)
                condisplay.photo3 = printbtn
                submit_receipt = Button(condisplay, image=printbtn, bg="white", bd="0", activebackground='green', command=printrec)
                submit_receipt.place(x="370", y="850")

                mailbtn = Image.open("Images/mail_btn.png")
                mailbtn = ImageTk.PhotoImage(mailbtn)
                condisplay.photo3 = mailbtn
                submit_receipt = Button(condisplay, image=mailbtn, bg="white", bd="0", activebackground='green', command=editmailsplash)
                submit_receipt.place(x="530", y="850")


                #CONNECTION DB
                try:
                    identered = id_entry.get()
                    con = cx_Oracle.connect('system/12345@localhost:1521/xe')
                    cursor = con.cursor()
                    x = cursor.execute(f"SELECT * FROM ADD_CONSUMER WHERE CON_ID = {identered}")
                    values = x.fetchall()
                    for i in values:
                        con_iddis = Label(condisplay, text=i[0], font="lucida 13 bold ", bg="midnight blue", fg="white")
                        con_iddis.place(x="170", y="240")

                        con_namedis = Label(condisplay, text= i[1], font="lucida 12 bold ", bg="white", fg="black")
                        con_namedis.place(x="530", y="152")

                        conphonedis = Label(condisplay, text= i[2], font="lucida 12 bold ", bg="white", fg="black")
                        conphonedis.place(x="530", y="202")

                        address1 = Label(condisplay, text= i[3], font="lucida 11 bold ", bg="white", fg="black")
                        address1.place(x="530", y="252")
                        address2 = Label(condisplay, text= i[4], font="lucida 11 bold ", bg="white", fg="black")
                        address2.place(x="530", y="280")
                        address3 = Label(condisplay, text= i[5], font="lucida 11 bold ", bg="white", fg="black")
                        address3.place(x="530", y="310")
                        pincode = Label(condisplay, text=f"PINCODE : {i[6]}", font="lucida 11 bold ", bg="white", fg="black")
                        pincode.place(x="530", y="340")

                        emaildis = Label(condisplay, text= i[7], font="lucida 11 bold ", bg="white",fg="black")
                        emaildis.place(x="530", y="400")

                        aadhardis = Label(condisplay, text= i[8], font="lucida 11 bold ", bg="white", fg="black")
                        aadhardis.place(x="530", y="450")

                        pandis = Label(condisplay, text= i[9], font="lucida 11 bold ", bg="white", fg="black")
                        pandis.place(x="530", y="500")

                        supplytypedis = Label(condisplay, text= i[10]+ f" ({i[14]})", font="lucida 11 bold ", bg="white", fg="black")
                        supplytypedis.place(x="530", y="550")

                        usagedis = Label(condisplay, text= i[11], font="lucida 11 bold ", bg="white", fg="black")
                        usagedis.place(x="530", y="600")

                        meterdis = Label(condisplay, text= i[12], font="lucida 11 bold ", bg="white", fg="black")
                        meterdis.place(x="530", y="650")

                        total_amount = i[15]
                        supplytypeamount = total_amount%100
                        cc_amount = total_amount - supplytypeamount
                        stcharge = Label(condisplay, text=supplytypeamount, font="lucida 11 bold ", bg="goldenrod1", fg="black")
                        stcharge.place(x="185", y="343")

                        cc = Label(condisplay, text=cc_amount, font="lucida 11 bold ", bg="goldenrod1", fg="black")
                        cc.place(x="185", y="394")

                        cctotal = Label(condisplay, text=total_amount, font="lucida 11 bold ", bg="goldenrod1", fg="black")
                        cctotal.place(x="185", y="433")

                        gpayamount = Label(condisplay, text=f"Amount : {total_amount} Rs", font="lucida 11 bold ", bg="white", fg="black")
                        gpayamount.place(x="80", y="670")




                    y = cursor.execute(f"SELECT to_char(JOINDATE,'DD-MON-YYYY'),to_char(JOINDATE,'hh24:mi') FROM ADD_CONSUMER WHERE CON_ID = {identered}")
                    time_date = y.fetchall()
                    for i in time_date:

                        date_label = Label(condisplay, text=f"{i[0]} |", font="lucida 9 bold ", bg="white", fg="black")
                        date_label.place(x="800", y="120")

                        time_label = Label(condisplay, text=i[1], font="lucida 9 bold ", bg="white", fg="black")
                        time_label.place(x="900", y="120")

                    cursor.close()
                    con.close()

                except Exception as e:
                    messagebox.showerror("Error","Some error occured\n\n ⭕ Enter valid CON_ID")
                    condisplay.destroy()



                print("Consumer details displayed")

                condisplay.mainloop()

    except Exception as e:
        messagebox.showerror("Error","Some Error Occured \n\n ⭕ Entry field should not be Empty.\n ⭕ Enter valid CON_ID")



def editentries():
    try:
        identered = id_entry.get()
        con = cx_Oracle.connect('system/12345@localhost:1521/xe')
        cursor = con.cursor()
        x = cursor.execute(f"SELECT COUNT(*) FROM ADD_CONSUMER WHERE CON_ID={identered} ")
        list1 = x.fetchall()
        for i in list1:
            if (i[0] == 0):
                messagebox.showerror("Error", f"CON_ID {identered} Does not exist. ")
                break
            else:
                global editconentry
                editconentry = Toplevel()
                global uconname_entry, uconphone_entry, uaddress1_entry, uaddress2_entry, uaddress3_entry, upincode_entry, uemail_entry, uaadhar_entry, upan_entry, uclick, uclick2, uvar, umeter_entry
                window_width, window_height = 1000, 950
                screen_width = editconentry.winfo_screenwidth()
                screen_height = editconentry.winfo_screenheight()
                position_top = int(screen_height / 2 - window_height / 2)
                position_right = int(screen_width / 2 - window_width / 2)
                editconentry.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

                editconentry.title("CONSUMER DETAILS ENTRY")
                editconentry.configure(bg="white")
                editconentry.resizable(width=False, height=False)
                editconentry.iconbitmap('Images/icon2.ico')

                conentry_top = Image.open("Images/adcon_toptemp.png")
                entrytop = ImageTk.PhotoImage(conentry_top)
                editconentry.photo = entrytop  # solution for bug in `PhotoImage`
                receipt_toplogo = Label(editconentry, image=entrytop, borderwidth="0")
                receipt_toplogo.place(x="37", y="2")

                conentry_left = Image.open("Images/charges2.png")
                entryleft = ImageTk.PhotoImage(conentry_left)
                editconentry.photo = entryleft  # solution for bug in `PhotoImage`
                receipt_leftcharges = Label(editconentry, image=entryleft, borderwidth="0")
                receipt_leftcharges.place(x="70", y="230")

                entrydown = Image.open("Images/adcon_downtempnew.png")
                entrydown = ImageTk.PhotoImage(entrydown)
                editconentry.photo = entrydown  # solution for bug in `PhotoImage`
                receipt_toplogo = Label(editconentry, image=entrydown, borderwidth="0")
                receipt_toplogo.place(x="37", y="800")

                ucon_name = Label(editconentry, text="Name                           : ", font="lucida 12 bold ", bg="white", fg="blue4")
                ucon_name.place(x="300", y="150")
                uconname_entry = Entry(editconentry, width="32", font="lucida 12", bd="3", bg="grey94")
                uconname_entry.place(x="530", y="150")

                uconphone = Label(editconentry, text="Phone No                    :", font="lucida 12 bold ", bg="white", fg="blue4")
                uconphone.place(x="300.5", y="200")
                uconphone_entry = Entry(editconentry, width="20", font="lucida 12", bd="3", bg="grey94")
                uconphone_entry.place(x="530", y="200")

                uaddress_label = Label(editconentry, text="Address :", font="lucida 12 bold underline", bg="white")
                uaddress_label.place(x="300", y="250")

                uaddress1_label = Label(editconentry, text="Flat, House no./ Company  :", font="lucida 10 bold", bg="white", fg="blue4")
                uaddress1_label.place(x="300", y="290")
                uaddress1_entry = Entry(editconentry, width="35", font="lucida 11", bd="3", bg="grey94")
                uaddress1_entry.place(x="530", y="290")

                uaddress2_label = Label(editconentry, text="Area, Street, Village           :", font="lucida 10 bold", bg="white",
                                       fg="blue4")
                uaddress2_label.place(x="301", y="330")
                uaddress2_entry = Entry(editconentry, width="35", font="lucida 11", bd="3", bg="grey94")
                uaddress2_entry.place(x="530", y="330")

                uaddress3_label = Label(editconentry, text="Landmark, Town/City         :", font="lucida 10 bold", bg="white",
                                       fg="blue4")
                uaddress3_label.place(x="300", y="370")
                uaddress3_entry = Entry(editconentry, width="35", font="lucida 11", bd="3", bg="grey94")
                uaddress3_entry.place(x="530", y="370")

                upincode_label = Label(editconentry, text="Pincode                              :", font="lucida 10 bold", bg="white",
                                      fg="blue4")
                upincode_label.place(x="300", y="410")
                upincode_entry = Entry(editconentry, width="14", font="lucida 11", bd="3", bg="grey94")
                upincode_entry.place(x="530", y="410")

                uemail_label = Label(editconentry, text="Email                           :", font="lucida 12 bold", bg="white",
                                    fg="blue4")
                uemail_label.place(x="300", y="460")
                uemail_entry = Entry(editconentry, width="30", font="lucida 12", bd="3", bg="grey94")
                uemail_entry.place(x="530", y="460")

                uaadhar_label = Label(editconentry, text="Aadhar No                   :", font="lucida 12 bold", bg="white", fg="blue4")
                uaadhar_label.place(x="300", y="510")
                uaadhar_entry = Entry(editconentry, width="13", font="lucida 12", bd="3", bg="grey94")
                uaadhar_entry.place(x="530", y="510")

                upan_label = Label(editconentry, text="PAN                             : ", font="lucida 12 bold", bg="white",
                                  fg="blue4")
                upan_label.place(x="300", y="560")
                upan_entry = Entry(editconentry, width="13", font="lucida 12", bd="3", bg="grey94")
                upan_entry.place(x="530", y="560")

                supplytype_label = Label(editconentry, text="Supply Type                :", font="lucida 12 bold", bg="white",
                                         fg="blue4")
                supplytype_label.place(x="300", y="610")
                list1 = ['SINGLE PHASE', 'THREE PHASE']
                uclick = StringVar()
                uclick.set("Select Type")
                utype_dropdown = OptionMenu(editconentry, uclick, *list1)
                utype_dropdown.config(bg="blue4", fg="white", width="12", activebackground="dodger blue", activeforeground="black")
                utype_dropdown.place(x="530", y="605")

                list2 = ['Up to 5 kW', '5-10 kW', '10-20 kW', '20-50 kW', '50-150 kW', 'Above 150 kW']
                uclick2 = StringVar()
                uclick2.set("Select Requirement")
                utest_dropdown = OptionMenu(editconentry, uclick2, *list2)
                utest_dropdown.config(bg="blue4", fg="white", width="15", activebackground="dodger blue", activeforeground="black")
                utest_dropdown.place(x="690", y="605")

                uusage_label = Label(editconentry, text="Purpose of Supply      :", font="lucida 12 bold", bg="white", fg="blue4")
                uusage_label.place(x="301", y="660")
                uvar = StringVar()
                domsymbol = Image.open("Images/domesticss_btn.png")
                domsymbol = ImageTk.PhotoImage(domsymbol)
                editconentry.photo = domsymbol  # solution for bug in `PhotoImage`
                domestic_radio = Radiobutton(editconentry, image=domsymbol, variable=uvar, bg="white", fg="blue", font="2",
                                             value="DOMESTIC", bd="0", activebackground="white")
                domestic_radio.place(x="530", y="650")

                indsymbol = Image.open("Images/industrialss_btn.png")
                indsymbol = ImageTk.PhotoImage(indsymbol)
                editconentry.photo = indsymbol  # solution for bug in `PhotoImage`
                industry_radio = Radiobutton(editconentry, image=indsymbol, variable=uvar, bg="white", fg="blue", font="2",value="INDUSTRIAL", bd="0", activebackground="white")
                industry_radio.place(x="600", y="650")

                umeter_label = Label(editconentry, text="Meter No                     : ", font="lucida 12 bold", bg="white", fg="blue4")
                umeter_label.place(x="300", y="710")
                umeter_entry = Entry(editconentry, width="13", font="lucida 12", bd="3", bg="grey94")
                umeter_entry.place(x="530", y="710")


                savechangessymbol = Image.open("Images/save_changes_button.png")
                savechangessymbol = ImageTk.PhotoImage(savechangessymbol)
                editconentry.photo3 = savechangessymbol
                savechanges_receipt = Button(editconentry, image=savechangessymbol, bg="white", bd="0", activebackground='green', command=Updatedb)
                savechanges_receipt.place(x="785", y="750")

                #insert details in the entry box
                identered = id_entry.get()
                con = cx_Oracle.connect('system/12345@localhost:1521/xe')
                cursor = con.cursor()
                x = cursor.execute(f"SELECT * FROM ADD_CONSUMER WHERE CON_ID = {identered}")
                values = x.fetchall()
                # global uconname_entry, uconphone_entry, uaddress1_entry, uaddress2_entry, uaddress3_entry, upincode_entry, uemail_entry, uaadhar_entry, upan_entry, uclick, uclick2, uvar, umeter_entry

                for i in values:
                    uconname_entry.insert(0, i[1])
                    uconphone_entry.insert(0, i[2])
                    uaddress1_entry.insert(0, i[3])
                    uaddress2_entry.insert(0, i[4])
                    uaddress3_entry.insert(0, i[5])
                    upincode_entry.insert(0, i[6])
                    uemail_entry.insert(0, i[7])
                    uaadhar_entry.insert(0, i[8])
                    upan_entry.insert(0, i[9])
                    uclick.set(i[10])
                    uclick2.set(i[14])
                    uvar.set(i[11])
                    umeter_entry.insert(0,i[12])

                cursor.close()
                con.close()
                editconentry.mainloop()
    except Exception as e:
        messagebox.showerror("Error", "Some Error Occured \n\n ⭕ Entry field should not be Empty.\n ⭕ Enter valid CON_ID")


def security():
    global secure
    secure = Toplevel()
    window_width, window_height = 200,140
    screen_width = secure.winfo_screenwidth()
    screen_height = secure.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    secure.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    secure.title("CONSUMER DETAILS ENTRY")
    secure.configure(bg="black")
    secure.resizable(width=False, height=False)
    secure.iconbitmap('Images/icon2.ico')

    text_label = Label(secure,text="Enter security password",font="lucida 8 bold",bg="black",fg="white")
    text_label.place(x="20",y="10")
    global pass_entry
    pass_entry = Entry(secure,font="lucida 11 bold",width="4",bd="3")
    pass_entry.place(x="75",y="40")

    unlockbtn = Image.open("Images/unlock_btn.png")
    unlockbtn = ImageTk.PhotoImage(unlockbtn)
    secure.photo3 = unlockbtn
    submit_receipt = Button(secure, image=unlockbtn, bg="black", bd="0", activebackground='black',command=passCheck)
    submit_receipt.place(x="20", y="75")

    secure.mainloop()

def passCheck():
    try:
        identered = id_entry.get()
        passentered = pass_entry.get()
        if (passentered=='1234'):
            con = cx_Oracle.connect('system/12345@localhost:1521/xe')
            cursor = con.cursor()
            x = cursor.execute(f"SELECT * FROM ADD_CONSUMER WHERE CON_ID = {identered}")
            values = x.fetchall()
            for i in values:
                response = messagebox.askyesno("Ask Question", f"Are you sure you want to delete details\n\nCONSUMER ID: {i[0]}\nNAME: {i[1]}\nMETER NO: {i[12]}")

                if response == True:
                     cursor.execute(f"DELETE FROM ADD_CONSUMER WHERE CON_ID={identered}")
                     secure.destroy()
                     messagebox.showinfo("MESSAGE",f"Consumer No {identered} deleted from record.")

                elif response == False:
                    pass
            cursor.close()
            con.commit()
            con.close()
            secure.destroy()
        else:
            messagebox.showinfo("MESSAGE","INVALID PASSWORD")
            secure.destroy()
    except Exception as e:
        messagebox.showerror("ERROR","Some Error Occured\n\n⭕ Enter Valid Consumer_id\n⭕ Try again.")
        secure.destroy()

def Updatedb():
    # global uconname_entry, uconphone_entry, uaddress1_entry, uaddress2_entry, uaddress3_entry, upincode_entry, uemail_entry, uaadhar_entry,
    # upan_entry, uclick, uclick2, uvar, umeter_entry
    try:
        uname = uconname_entry.get()
        uphone = uconphone_entry.get()
        uaddress1 = uaddress1_entry.get()
        uaddress2 = uaddress2_entry.get()
        uaddress3 = uaddress3_entry.get()
        upincode = upincode_entry.get()
        uemail = uemail_entry.get()
        uaadhar = uaadhar_entry.get()
        upan = upan_entry.get()
        usupply = uclick.get()
        upos = uvar.get()
        umeter = umeter_entry.get()
        urequirement = uclick2.get()
        identered = id_entry.get()

        if (usupply == 'SINGLE PHASE' and (urequirement=='Up to 5 kW' or urequirement=='5-10 kW')):
            cc = 2050
        elif (usupply == 'THREE PHASE' and urequirement=='10-20 kW'):
            cc = 4575
        elif  (usupply == 'THREE PHASE' and urequirement=='20-50 kW'):
            cc = 6575
        elif (usupply == 'THREE PHASE' and urequirement=='50-150 kW'):
            cc = 12075
        elif (usupply == 'THREE PHASE' and urequirement=='Above 150 kW'):
            cc = 250075
        else:
            cc = 2050

        con = cx_Oracle.connect('system/12345@localhost:1521/xe')
        cursor = con.cursor()
        cursor.execute(f"""
                        UPDATE ADD_CONSUMER SET
                        CON_NAME='{uname}',
                        PHONE_NO={uphone},
                        ADDRESS1='{uaddress1}',
                        ADDRESS2='{uaddress2}',
                        ADDRESS3='{uaddress3}',
                        PIN_CODE={upincode},
                        EMAILID='{uemail}',
                        AADHAR={uaadhar},
                        PAN='{upan}',
                        SUPPLY_TYPE='{usupply}',
                        POS='{upos}',
                        METER_NO={umeter},
                        REQUIREMENT='{urequirement}',
                        TOTAL_CC={cc}
                        WHERE CON_ID={identered}
                        """)

        cursor.close()
        con.commit()
        con.close()
        editconentry.destroy()
        showupdatemessage()

    except Exception as e:
        messagebox.showerror("Error","Some Error Occured \n\n ⭕ Entry field should not be Empty.\n ⭕ Entry must be valid.")

def showupdatemessage():
    messagebox.showinfo("Message", "Details Updated Successfully!")
    showentry()

def enterReadings():
    global meterread
    meterread = Toplevel()
    global conid_entry, meterread_entry,month
    window_width, window_height = 800, 600
    screen_width = meterread.winfo_screenwidth()
    screen_height = meterread.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    meterread.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    meterread.title("ENTER METER READINGS")
    meterread.configure(bg="white")
    meterread.resizable(width=False, height=False)
    meterread.iconbitmap('Images/icon2.ico')

    conentry_top = Image.open("Images/readings_topbg.png")
    entrytop = ImageTk.PhotoImage(conentry_top)
    meterread.photo = entrytop  # solution for bug in `PhotoImage`
    receipt_toplogo = Label(meterread, image=entrytop, borderwidth="0")
    receipt_toplogo.place(x="37", y="2")

    unitslab = Image.open("Images/unit_slab (1).png")
    unitslabimg = ImageTk.PhotoImage(unitslab)
    meterread.photo = unitslabimg  # solution for bug in `PhotoImage`
    receipt_toplogo = Label(meterread, image=unitslabimg, borderwidth="0")
    receipt_toplogo.place(x="37", y="280")

    readings_down = Image.open("Images/readings_downtemp.png")
    readingdown = ImageTk.PhotoImage(readings_down)
    meterread.photo = readingdown  # solution for bug in `PhotoImage`
    receipt_toplogo = Label(meterread, image=readingdown, borderwidth="0")
    receipt_toplogo.place(x="37", y="510")

    conid_label = Label(meterread, text="CON_ID                           :", font="lucida 12 bold", bg="white",fg="blue4")
    conid_label.place(x="226", y="130")
    conid_entry = Entry(meterread, font="lucida 13 bold ",width="10", bg="grey94", fg="black")
    conid_entry.place(x="480", y="130")


    meterread_label = Label(meterread, text="METER READING (kW h) :", font="lucida 12 bold", bg="white", fg="blue4")
    meterread_label.place(x="225", y="170")
    meterread_entry = Entry(meterread, font="lucida 13 bold ", width="10", bg="grey94", fg="black")
    meterread_entry.place(x="480", y="170")

    conid_label = Label(meterread, text="READING MONTH            :", font="lucida 12 bold", bg="white",fg="blue4")
    conid_label.place(x="224", y="210")
    list1 = ['JAN-21', 'FEB-21','MAR-21','APR-21','MAY-21','JUN-21','JUL-21','AUG-21','SEP-21','OCT-21','NOV-21','DEC-21']
    month = StringVar()
    month.set(" Select Month")
    month_dropdown = OptionMenu(meterread, month, *list1)
    month_dropdown.config(bg="blue4", fg="white", width="9",font='lucida 8 bold', activebackground="dodger blue", activeforeground="black")
    month_dropdown.place(x="478", y="205")

    submitreading = Image.open("Images/submit_reading_button.png")
    submitreading = ImageTk.PhotoImage(submitreading)
    meterread.photo3 = submitreading
    savechanges_receipt = Button(meterread, image=submitreading, bg="white", bd="0",command=insertreadings)
    savechanges_receipt.place(x="320", y="450")


    meterread.mainloop()

def insertreadings():
    conid = conid_entry.get()
    meterreading = meterread_entry.get()
    entry_date = "01-"+str(month.get())
    try:
        con = cx_Oracle.connect('system/12345@localhost:1521/xe')
        cursor = con.cursor()
        x = cursor.execute(f"SELECT COUNT(*) FROM ADD_CONSUMER WHERE CON_ID={conid}  ")
        list1  = x.fetchall()
        y = cursor.execute(f"SELECT COUNT(*) FROM METER_READING WHERE CON_ID={conid} and reading_date='{entry_date}'")
        readings = y.fetchall()

        z = cursor.execute(f"select count(*) from charge_master_track  where last_day(bill_date)>'{entry_date}'")
        cnt = z.fetchall()

        for i in list1:
            for value in readings:
                for predat in cnt:
                    if (i[0]==0 ):
                        messagebox.showerror("Error",f"CON_ID {conid} Does not exist. ")
                        break
                    if (predat[0]>0):
                        messagebox.showerror("Error","Billing already processed for this month")
                        break
                    if (value[0] == 1):
                        response = messagebox.askyesno("Ask Question",f"CON_ID {conid} Meter Reading already inserted\nfor current months billing.\n\nDo you want to edit and update reading?")

                        if response == True:
                            readingUpdate()

                        elif response == False:
                            pass


                    else:
                        cursor.execute(f"INSERT INTO METER_READING VALUES ({conid},{meterreading},'{entry_date}',sysdate)")
                        messagebox.showinfo("Message", "Readings Added Successfully!")
                        cursor.close()
                        con.commit()

                        con.close()
                        meterread.destroy()


    except Exception as e:
        messagebox.showerror("Error", "Error occured\n\n ⭕ Entry field should not be Empty.\n ⭕ Enter Valid CON_ID\n ⭕ Meter reading should be greater than previous reading. ")
        print(Exception)
        print(e)
        print(entry_date)

def readingUpdate():
    conid = conid_entry.get()
    entry_date = "01-"+str(month.get())
    global umeterread_entry,umeterread
    umeterread = Toplevel()
    window_width, window_height = 800, 600
    screen_width = umeterread.winfo_screenwidth()
    screen_height = umeterread.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    umeterread.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    umeterread.title("ENTER METER READINGS")
    umeterread.configure(bg="white")
    umeterread.resizable(width=False, height=False)
    umeterread.iconbitmap('Images/icon2.ico')

    conentry_top = Image.open("Images/readings_topbg.png")
    entrytop = ImageTk.PhotoImage(conentry_top)
    umeterread.photo = entrytop  # solution for bug in `PhotoImage`
    receipt_toplogo = Label(umeterread, image=entrytop, borderwidth="0")
    receipt_toplogo.place(x="37", y="2")

    unitslab = Image.open("Images/unit_slab (1).png")
    unitslabimg = ImageTk.PhotoImage(unitslab)
    umeterread.photo = unitslabimg  # solution for bug in `PhotoImage`
    receipt_toplogo = Label(umeterread, image=unitslabimg, borderwidth="0")
    receipt_toplogo.place(x="37", y="280")

    readings_down = Image.open("Images/readings_downtemp.png")
    readingdown = ImageTk.PhotoImage(readings_down)
    umeterread.photo = readingdown  # solution for bug in `PhotoImage`
    receipt_toplogo = Label(umeterread, image=readingdown, borderwidth="0")
    receipt_toplogo.place(x="37", y="510")

    uconid_label = Label(umeterread, text="CON_ID                           :", font="lucida 12 bold", bg="white",fg="blue4")
    uconid_label.place(x="226", y="130")



    umeterread_label = Label(umeterread, text="METER READING (kW h) :", font="lucida 12 bold", bg="white", fg="blue4")
    umeterread_label.place(x="225", y="170")
    umeterread_entry = Entry(umeterread, font="lucida 13 bold ", width="10", bg="grey94", fg="black")
    umeterread_entry.place(x="480", y="170")

    conid_label = Label(umeterread, text="READING MONTH            :", font="lucida 12 bold", bg="white", fg="blue4")
    conid_label.place(x="224", y="210")

    con = cx_Oracle.connect('system/12345@localhost:1521/xe')
    cursor = con.cursor()
    x = cursor.execute(f"SELECT CON_ID,CURRENT_READING,to_char(sysdate,'MON-YY') FROM METER_READING WHERE CON_ID={conid} AND READING_DATE='{entry_date}'")
    prevalue = x.fetchall()
    for i in prevalue:
        uconid_entry = Label(umeterread, text=i[0], font="lucida 13 bold ", bg="white", fg="black")
        uconid_entry.place(x="480", y="130")
        umeterread_label = Label(umeterread, text=i[2], font="lucida 12 bold", bg="white", fg="black")
        umeterread_label.place(x="480", y="210")
        umeterread_entry.insert(0,i[1])
    cursor.close()
    con.close()

    submitreading = Image.open("Images/submit_reading_button.png")
    submitreading = ImageTk.PhotoImage(submitreading)
    umeterread.photo3 = submitreading
    savechanges_receipt = Button(umeterread, image=submitreading, bg="white", bd="0", command=updatenewreading)
    savechanges_receipt.place(x="320", y="450")

    umeterread.mainloop()


def updatenewreading():
    conid = conid_entry.get()
    entry_date = "01-" + str(month.get())
    newreading = umeterread_entry.get()
    con = cx_Oracle.connect('system/12345@localhost:1521/xe')
    cursor = con.cursor()
    cursor.execute(f"UPDATE METER_READING SET CURRENT_READING={newreading} WHERE  CON_ID={conid} AND READING_DATE='{entry_date}'")
    cursor.close()
    con.commit()

    meterread.destroy()
    umeterread.destroy()
    messagebox.showinfo("Message","Readings Update Successfully!")
    con.close()

#Alert window

def alerts():
    alertbox = Toplevel()
    global alert_text, alertconid_entry
    window_width, window_height = 760, 600
    screen_width = alertbox.winfo_screenwidth()
    screen_height = alertbox.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    alertbox.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    alertbox.title("Send Alert")
    alertbox.configure(bg="white")
    alertbox.resizable(width=False, height=False)
    alertbox.iconbitmap('Images/icon2.ico')

    alertwindow_top = Image.open("Images/aletrwindow_top1.png")
    alerttop = ImageTk.PhotoImage(alertwindow_top)
    alertbox.photo = alerttop  # solution for bug in `PhotoImage`
    alertwindow_toplogo = Label(alertbox, image=alerttop, borderwidth="0")
    alertwindow_toplogo.place(x="20", y="2")

    alertwindow_down = Image.open("Images/alertwindow_down 1.png")
    alertdown = ImageTk.PhotoImage(alertwindow_down)
    alertbox.photo = alertdown  # solution for bug in `PhotoImage`
    receipt_toplogo = Label(alertbox, image=alertdown, borderwidth="0")
    receipt_toplogo.place(x="20", y="480")

    alertconid_label = Label(alertbox, text="CON_ID            :", font="lucida 12 bold", bg="white",fg="blue4")
    alertconid_label.place(x="235", y="130")
    alertconid_entry = Entry(alertbox, font="lucida 13 bold ", width="10", bg="grey94", fg="black")
    alertconid_entry.place(x="420", y="130")

    alertmessage_label = Label(alertbox, text="ALERT MESSAGE", font="lucida 13 bold underline", bg="white", fg="blue4")
    alertmessage_label.place(x="280", y="180")

    alertmsg1 = Image.open("Images/preload_alertmsg.png")
    alertmsg1 = ImageTk.PhotoImage(alertmsg1)
    alertbox.photo3 = alertmsg1
    msg1_btn = Button(alertbox, image=alertmsg1, bg="white", bd="0",command=message1)
    msg1_btn.place(x="203", y="230")

    alertmsg2 = Image.open("Images/msg2.png")
    alertmsg2 = ImageTk.PhotoImage(alertmsg2)
    alertbox.photo3 = alertmsg2
    msg2_btn = Button(alertbox, image=alertmsg2, bg="white", bd="0",command=message2)
    msg2_btn.place(x="293", y="230")

    alertmsg3 = Image.open("Images/msg3.png")
    alertmsg3 = ImageTk.PhotoImage(alertmsg3)
    alertbox.photo3 = alertmsg3
    msg3_btn = Button(alertbox, image=alertmsg3, bg="white", bd="0",command=message3)
    msg3_btn.place(x="383", y="230")

    alertmsg4 = Image.open("Images/msg4.png")
    alertmsg4 = ImageTk.PhotoImage(alertmsg4)
    alertbox.photo3 = alertmsg4
    msg4_btn = Button(alertbox, image=alertmsg4, bg="white", bd="0",command=message4)
    msg4_btn.place(x="473", y="230")

    global alert_text
    alert_text = Text(alertbox,font="lucida 8 bold ",width="51",height="6", bg="gray94",fg="black")
    alert_text.place(x="200",y="280")

    global website
    website = IntVar()
    websitelink = Checkbutton(alertbox, text="Include Website link. ", variable=website, font="lucida 7 ", bg="white", fg="black")
    websitelink.place(x="200", y="380")

    global payment
    payment = IntVar()
    paymentlink = Checkbutton(alertbox, text="Include Payment site link. ", variable=payment, font="lucida 7 ", bg="white", fg="black")
    paymentlink.place(x="400", y="380")

    whatsappalert = Image.open("Images/alert_whatsapp1.png")
    whatsappalert = ImageTk.PhotoImage(whatsappalert)
    alertbox.photo3 = whatsappalert
    savechanges_receipt = Button(alertbox, image=whatsappalert, bg="white", bd="0", command=sendingwmsg)
    savechanges_receipt.place(x="400", y="430")

    gmailalert = Image.open("Images/alert_email1.png")
    gmailalert = ImageTk.PhotoImage(gmailalert)
    alertbox.photo3 = gmailalert
    savechanges_receipt = Button(alertbox, image=gmailalert, bg="white", bd="0", command=alertmailsplash)
    savechanges_receipt.place(x="200", y="430")

    alertbox.mainloop()

# Message text for alert message
def message1():
    newtext="""Dear Consumer,
we are experiencing service disruptions due to internal 
agitation on past issues. Team Electrica is working to 
resolve the issues at the earliest. 
Regret the inconvenience caused, we will update you 
on developments."""
    alert_text.delete("1.0","end")
    alert_text.config(alert_text.insert("1.0",newtext))


def message2():
    newtext = """Dear Consumer, 
we are aware of the power interruption in your area 
and are striving hard to restore supply by 01:21 AM. 
Sorry for the inconvenience caused."""
    alert_text.delete("1.0", "end")
    alert_text.config(alert_text.insert("1.0", newtext))

def message3():
    newtext = """Dear Consumer,
We have resorted to power supply switch off in your 
area due to saftey reasons. We are monitoring the 
situation and will restore the power supply post safety 
checks of the system to avoid any mishaps.
    """
    alert_text.delete("1.0", "end")
    alert_text.config(alert_text.insert("1.0", newtext))

def message4():
    newtext = """Dear Consumer,
We have not received your bill paytment since 
3 months.Please pay your bill through below link before 
the due date to avoid power cut
    """
    alert_text.delete("1.0", "end")
    alert_text.config(alert_text.insert("1.0", newtext))

def submitalertmessage():
    try:
        alertconid = alertconid_entry.get()
        msg = alert_text.get("1.0",END)
        websitelink = ""
        paymentlink = ""

        print(msg)
        web = website.get()
        pay = payment.get()
        if web == 1:
            websitelink = "*Visit Website*:https://www.adanielectricity.com/"
        if pay == 1:
            paymentlink = "\n*Pay Bill*:https://www.adanielectricity.com/Payment/Online-Payments"

        con = cx_Oracle.connect('system/12345@localhost:1521/xe')
        cursor = con.cursor()
        checkcount = cursor.execute(f"SELECT COUNT(*) FROM ADD_CONSUMER WHERE CON_ID={alertconid} ")
        count = checkcount.fetchall()
        values = cursor.execute(f"SELECT * FROM ADD_CONSUMER WHERE CON_ID={alertconid}")
        phoneno = values.fetchall()
        for number in count:
            print(number[0])
            if (number[0]==0):
                sendsplash.destroy()
                messagebox.showerror("Error", f"CON_ID {alertconid} does not Exist.")
                break
            else:
                    try:
                        for i in phoneno:
                            now = datetime.datetime.now()
                            import pywhatkit as kit
                            kit.sendwhatmsg(f"+91{i[2]}",f"🛑🛑🛑🛑🛑🛑🛑\n*Alert*\n{msg}{websitelink}{paymentlink}\n⚠⚠⚠⚠⚠⚠⚠",now.hour, now.minute+1)

                    except Exception as e:
                        messagebox.showerror("ERROR","Network Error Occured\nPlease check your Internet connection and Try Again")
                        tryagainSplash()


        cursor.close()
        con.close()
    except Exception as e:
        messagebox.showerror("Error", "Some error occured.\n\n⭕ Enter valid details. \n⭕ Fields should not be empty.")





def sendingwmsg():
    global sendsplash
    sendsplash = Toplevel()
    window_width, window_height = 300, 100
    screen_width = sendsplash.winfo_screenwidth()
    screen_height = sendsplash.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    sendsplash.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    sendsplash.configure(bg="white")
    sendsplash.resizable(width=False, height=False)
    sendsplash.overrideredirect(True)


    splashframe = Frame(sendsplash, highlightbackground="black", highlightthickness=3, width=300, height=111, bd="0", bg="white")
    splashframe.pack()

    file = "Images/loader2.gif"

    info = Image.open(file)

    frames = info.n_frames  # gives total number of frames that gif contains

    # creating list of PhotoImage objects for each frames
    im = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]

    count = 0
    anim = None

    def animation(count):
        global anim
        im2 = im[count]

        gif_label.configure(image=im2)
        count += 1
        if count == frames:
            count = 0
        anim = sendsplash.after(50, lambda: animation(count))

    gif_label = Label(sendsplash, image="", bd="0",bg="white")
    gif_label.place(x="110", y="3")
    animation(count)

    sending_label = Label(sendsplash, text="Sending...", font="lucida 8 ", bg="white", fg="black")
    sending_label.place(x="117", y="55")
    loading_label = Label(sendsplash, text="Please wait", font="lucida 8 ", bg="white", fg="black")
    loading_label.place(x="110", y="74")
    sendsplash.after(2000,submitalertmessage)

    sendsplash.mainloop()

def tryagainSplash():
    global splashwin
    splashwin = Toplevel()
    window_width, window_height = 300,110
    screen_width = splashwin.winfo_screenwidth()
    screen_height = splashwin.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    splashwin.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    splashwin.configure(bg="white")
    splashwin.resizable(width=False, height=False)
    splashwin.overrideredirect(True)

    splashframe = Frame(splashwin, highlightbackground="black", highlightthickness=3, width=300, height=111, bd="0", bg="white" )
    splashframe.pack()

    file = "Images/loader2.gif"

    info = Image.open(file)

    frames = info.n_frames  # gives total number of frames that gif contains

    # creating list of PhotoImage objects for each frames
    im = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]

    count = 0
    anim = None

    def animation(count):
        global anim
        im2 = im[count]

        gif_label.configure(image=im2)
        count += 1
        if count == frames:
            count = 0
        anim = splashwin.after(50, lambda: animation(count))



    gif_label = Label(splashwin, image="",bd="0")
    gif_label.place(x="110", y="5")
    animation(count)

    sending_label = Label(splashwin,text="Sending...",font="lucida 8 ",bg="white",fg="black")
    sending_label.place(x="117",y="60")
    loading_label = Label(splashwin, text="Please wait", font="lucida 8 ", bg="white", fg="black")
    loading_label.place(x="110", y="79")
    splashwin.after(7000,submitalertmessage)

    splashwin.mainloop()

def alertmailsplash():
    global sendsplash
    sendsplash = Toplevel()
    window_width, window_height = 300, 100
    screen_width = sendsplash.winfo_screenwidth()
    screen_height = sendsplash.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    sendsplash.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    sendsplash.configure(bg="white")
    sendsplash.resizable(width=False, height=False)
    sendsplash.overrideredirect(True)

    splashframe = Frame(sendsplash, highlightbackground="black", highlightthickness=3, width=300, height=110, bd="0",bg="white")
    splashframe.pack()






    file = "Images/loader2.gif"

    info = Image.open(file)

    frames = info.n_frames  # gives total number of frames that gif contains

    # creating list of PhotoImage objects for each frames
    im = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]

    count = 0
    anim = None

    def animation(count):
        global anim
        im2 = im[count]

        gif_label.configure(image=im2)
        count += 1
        if count == frames:
            count = 0
        anim = sendsplash.after(50, lambda: animation(count))

    gif_label = Label(sendsplash, image="", bd="0")
    gif_label.place(x="110", y="3")
    animation(count)

    sending_label = Label(sendsplash, text="Sending...", font="lucida 8 ", bg="white", fg="black")
    sending_label.place(x="117", y="55")
    loading_label = Label(sendsplash, text="Please wait", font="lucida 8 ", bg="white", fg="black")
    loading_label.place(x="110", y="74")
    sendsplash.after(3000,sendalertmail)

    sendsplash.mainloop()

def sendalertmail():
    try:
        alertconid = alertconid_entry.get()
        message = alert_text.get("1.0",END)
        websitelink = ""
        paymentlink = ""

        web = website.get()
        pay = payment.get()
        if web == 1:
            websitelink = "Visit Website: https://www.adanielectricity.com/"
        if pay == 1:
            paymentlink = "\nPay Bill: https://www.adanielectricity.com/Payment/Online-Payments"

        con = cx_Oracle.connect('system/12345@localhost:1521/xe')
        cursor = con.cursor()
        checkcount = cursor.execute(f"SELECT COUNT(*) FROM ADD_CONSUMER WHERE CON_ID={alertconid} ")
        count = checkcount.fetchall()
        values = cursor.execute(f"SELECT * FROM ADD_CONSUMER WHERE CON_ID={alertconid}")
        emailid = values.fetchall()
        for number in count:
            print(number[0])
            if (number[0]==0):
                sendsplash.destroy()
                messagebox.showerror("Error", f"CON_ID {alertconid} does not Exist.")
                break
            else:
                try:
                    for i in emailid:
                        msg = EmailMessage()
                        msg.set_content(f"{message}{websitelink}{paymentlink}")

                        msg['Subject'] = 'Alert'
                        msg['From'] = "electrica.org@gmail.com"
                        msg['To'] = f"{i[7]}"

                        # Send the message via our own SMTP server.
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.login("electrica.org@gmail.com", "Electrica@1234")
                        server.send_message(msg)
                        server.quit()
                        messagebox.showinfo('Message',"Mail sent Successfully")
                        sendsplash.destroy()
                except Exception as e:
                    messagebox.showerror("ERROR","Network Error Occured\nPlease check your Internet connection and Try Again")
                    print(e)


        cursor.close()
        con.close()
    except Exception as e:
        messagebox.showerror("Error", "Some error occured.\n\n⭕ Enter valid details. \n⭕ Fields should not be empty.")
        print(e)

def billPayment():
    global payment
    payment = Toplevel()
    window_width, window_height = 760, 350
    screen_width = payment.winfo_screenwidth()
    screen_height = payment.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    payment.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    payment.title("PAYMENT")
    payment.configure(bg="white")
    payment.resizable(width=False, height=False)
    payment.iconbitmap('Images/icon2.ico')

    paymentwindow_top = Image.open("Images/payment_templatetopss.png")
    paymenttop = ImageTk.PhotoImage(paymentwindow_top)
    payment.photo = paymenttop  # solution for bug in `PhotoImage`
    paymentwindow_toplogo = Label(payment, image=paymenttop, borderwidth="0")
    paymentwindow_toplogo.place(x="20", y="2")

    paymentwindow_down = Image.open("Images/payment_templatedown.png")
    paymentdown = ImageTk.PhotoImage(paymentwindow_down)
    payment.photo = paymentdown  # solution for bug in `PhotoImage`
    payment_toplogo = Label(payment, image=paymentdown, borderwidth="0")
    payment_toplogo.place(x="20", y="250")
    global paymentconid_entry
    paymentconid_label = Label(payment, text="CON_ID            :", font="lucida 12 bold", bg="white", fg="blue4")
    paymentconid_label.place(x="235", y="130")
    paymentconid_entry = Entry(payment, font="lucida 13 bold ", width="10", bg="grey94", fg="black")
    paymentconid_entry.place(x="420", y="130")

    showbillbtn = Image.open("Images/showbill_btn1.png")
    showbillbtn = ImageTk.PhotoImage(showbillbtn)
    payment.photo3 = showbillbtn
    shobill_btn = Button(payment, image=showbillbtn, bg="white", bd="0", activebackground='black',command=validateid)
    shobill_btn.place(x="280", y="200")

    payment.mainloop()

def validateid():
    try:
        conid = paymentconid_entry.get()
        con = cx_Oracle.connect('system/12345@localhost:1521/xe')
        cursor = con.cursor()
        getcount = cursor.execute(f"SELECT COUNT(*) FROM ADD_CONSUMER WHERE CON_ID={conid}")
        validate = getcount.fetchall()
        for value in validate:
            if value[0] == 0:
                messagebox.showerror("Error",f"CON_ID {conid} does not exist.")
            else:
                showbilling()

    except Exception as e:
        messagebox.showerror("Error", "Some error occured.\n\n⭕ Enter valid details. \n⭕ Fields should not be empty.")


def showbilling():
    global seebill
    seebill = Toplevel()
    window_width, window_height = 760, 600
    screen_width = seebill.winfo_screenwidth()
    screen_height = seebill.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    seebill.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    seebill.title("BILL")
    seebill.configure(bg="white")
    seebill.resizable(width=False, height=False)
    seebill.iconbitmap('Images/icon2.ico')

    billbg_size = Image.open("Images/billwindowbg.png")
    billbg_resized = billbg_size.resize((700, 580), Image.ANTIALIAS)
    billbg_image = ImageTk.PhotoImage(billbg_resized)
    Label(image=billbg_image)
    label_bg = Label(seebill, image=billbg_image, borderwidth="0", )
    label_bg.place(x=28, y=0)

    paymentconid_label = Label(seebill, text="CON_ID                    :", font="lucida 10 bold", bg="white", fg="blue4")
    paymentconid_label.place(x="200", y="80")

    conname_label = Label(seebill, text="NAME                       :", font="lucida 10 bold", bg="white", fg="blue4")
    conname_label.place(x="200", y="140")

    conphone_label = Label(seebill, text="PHONE NO               :", font="lucida 10 bold", bg="white", fg="blue4")

    conphone_label.place(x="200", y="200")

    balance_label = Label(seebill, text="BALANCE AMOUNT  :", font="lucida 10 bold", bg="white", fg="blue4")
    balance_label.place(x="200", y="260")

    balance_label = Label(seebill, text="BILL DATE                :", font="lucida 10 bold", bg="white", fg="blue4")
    balance_label.place(x="200", y="320")

    balance_label = Label(seebill, text="PAYMENT STATUS   :", font="lucida 10 bold", bg="white", fg="blue4")
    balance_label.place(x="200", y="380")

    netbill_label = Label(seebill, text="NET BILL AMOUNT   :", font="lucida 10 bold", bg="white", fg="blue4")
    netbill_label.place(x="200", y="440")

    paynowbtn = Image.open("Images/proceedtopay_btn.png")
    paynowbtn = ImageTk.PhotoImage(paynowbtn)
    seebill.photo3 = paynowbtn
    submit_receipt = Button(seebill, image=paynowbtn, bg="white", bd="0", activebackground='black',command=checkstatus)
    submit_receipt.place(x="280", y="490")

    conid = paymentconid_entry.get()
    con = cx_Oracle.connect('system/12345@localhost:1521/xe')
    cursor = con.cursor()

    paydetails = cursor.execute(f"""
                                SELECT T1.CON_ID,T1.CON_NAME,T1.PHONE_NO,T2.BALANCE_AMT,to_char(T2.BILL_DATE,'DD-MON-YY')
                                ,T2.BILL_STATUS,T2.CHARGE_AMT FROM ADD_CONSUMER T1, CHARGE_MASTER_TRACK T2 
                                WHERE T1.CON_ID =T2.CON_ID   AND T2.CON_ID = {conid} AND 
                                BILL_DATE=(SELECT MAX(BILL_DATE) FROM CHARGE_MASTER_TRACK)
                                """)
    showbill_list = paydetails.fetchall()
    for values in showbill_list:
        disid_label = Label(seebill, text=f"{values[0]}", font="lucida 10 bold", bg="white", fg="black")
        disid_label.place(x="380", y="80")

        disname_label = Label(seebill, text=f"{values[1]}", font="lucida 10 bold", bg="white", fg="black")
        disname_label.place(x="380", y="140")

        disphone_label = Label(seebill, text=f"{values[2]}", font="lucida 10 bold", bg="white", fg="black")
        disphone_label.place(x="380", y="200")

        disbalamt_label = Label(seebill, text=u"\u20B9"+f" {values[3]}", font="lucida 10 bold", bg="white", fg="black")
        disbalamt_label.place(x="380", y="260")

        disbildate_label = Label(seebill, text=f"{values[4]}", font="lucida 10 bold", bg="white", fg="black")
        disbildate_label.place(x="380", y="320")
        if (values[5]=="PAID"):
            dispaystat_label = Label(seebill, text=f"{values[5]}", font="lucida 10 bold", bg="white", fg="green")
            dispaystat_label.place(x="380", y="380")
            print(values[5])
        else:
            dispaystat_label = Label(seebill, text=f"{values[5]}", font="lucida 10 bold", bg="white", fg="red")
            dispaystat_label.place(x="380", y="380")

        disbilamt_label = Label(seebill, text=u"\u20B9"+f" {values[6]}", font="lucida 10 bold", bg="white", fg="black")
        disbilamt_label.place(x="380", y="440")
    cursor.close()
    con.close()
    seebill.mainloop()


def checkstatus():
    seebill.destroy()
    con_id = paymentconid_entry.get()
    con = cx_Oracle.connect('system/12345@localhost:1521/xe')
    cursor = con.cursor()
    paydetails = cursor.execute(f"""
                                    SELECT BILL_STATUS FROM CHARGE_MASTER_TRACK WHERE CON_ID = {con_id}
                                     AND BILL_DATE =(SELECT MAX(BILL_DATE) FROM CHARGE_MASTER_TRACK)
                                    """)
    status_list = paydetails.fetchall()
    for value in status_list:
        if (value[0]=="PAID"):
            messagebox.showinfo("Message","Bill already payed for this month.")
        else:
            pay()

    cursor.close()
    con.close()


def pay():
    seebill.destroy()
    global paynow
    paynow = Toplevel()
    window_width, window_height = 400, 320
    screen_width = paynow.winfo_screenwidth()
    screen_height = paynow.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    paynow.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    paynow.title("BILL")
    paynow.configure(bg="white")
    paynow.resizable(width=False, height=False)
    paynow.iconbitmap('Images/icon2.ico')

    billbg_size = Image.open("Images/billwindowbg.png")
    billbg_resized = billbg_size.resize((380, 300), Image.ANTIALIAS)
    billbg_image = ImageTk.PhotoImage(billbg_resized)
    Label(image=billbg_image)
    label_bg = Label(paynow, image=billbg_image, borderwidth="0", )
    label_bg.place(x=10, y=-5)

    payamt_label = Label(paynow, text="BILL AMOUNT            : ", font="lucida 10 bold", bg="white",fg="blue4")
    payamt_label.place(x="30", y="80")

    receivedamt_label = Label(paynow, text="RECEIVED AMOUNT   : ", font="lucida 10 bold", bg="white", fg="blue4")
    receivedamt_label.place(x="30", y="140")

    paynowbtn = Image.open("Images/submit_btn2pay.png")
    paynowbtn = ImageTk.PhotoImage(paynowbtn)
    paynow.photo3 = paynowbtn
    submit_receipt = Button(paynow, image=paynowbtn, bg="white", bd="0", activebackground='black', command=securitycheck)
    submit_receipt.place(x="140", y="200")
    con_id = paymentconid_entry.get()
    con = cx_Oracle.connect('system/12345@localhost:1521/xe')
    cursor = con.cursor()
    paydetails = cursor.execute(f"""
                                        SELECT CHARGE_AMT FROM CHARGE_MASTER_TRACK WHERE CON_ID = {con_id}
                                         AND BILL_DATE =(SELECT MAX(BILL_DATE) FROM CHARGE_MASTER_TRACK)
                                        """)
    status_list = paydetails.fetchall()
    for value in status_list:
        payamt_label = Label(paynow, text=u"\u20B9"+f" {value[0]}", font="lucida 10 bold", bg="white", fg="black")
        payamt_label.place(x="220", y="80")

    amtreceived_entry = Entry(paynow, font="lucida 13 bold ", width="10", bg="grey94", fg="black")
    amtreceived_entry.place(x="220", y="140")



    paynow.mainloop()

def securitycheck():
    global secure
    secure = Toplevel()
    window_width, window_height = 200,140
    screen_width = secure.winfo_screenwidth()
    screen_height = secure.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    secure.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    secure.title("CONSUMER DETAILS ENTRY")
    secure.configure(bg="black")
    secure.resizable(width=False, height=False)
    secure.iconbitmap('Images/icon2.ico')

    text_label = Label(secure,text="Enter security password",font="lucida 8 bold",bg="black",fg="white")
    text_label.place(x="20",y="10")
    global pass_entry
    pass_entry = Entry(secure,font="lucida 11 bold",width="4",bd="3")
    pass_entry.place(x="75",y="40")

    unlockbtn = Image.open("Images/unlock_btn.png")
    unlockbtn = ImageTk.PhotoImage(unlockbtn)
    secure.photo3 = unlockbtn
    submit_receipt = Button(secure, image=unlockbtn, bg="black", bd="0", activebackground='black',command=checkPassword)
    submit_receipt.place(x="20", y="75")

    secure.mainloop()




def checkPassword():
    try:
        passentered = pass_entry.get()
        if (passentered=='1234'):
            paySplash()

        else:
            messagebox.showinfo("MESSAGE","INVALID PASSWORD")
            secure.destroy()
    except Exception as e:
        messagebox.showerror("ERROR","Some Error Occured\n\n⭕ Enter Valid Consumer_id\n⭕ Try again.")
        secure.destroy()


def paySplash():
    secure.destroy()
    paynow.destroy()
    global billing
    billing = Toplevel()
    window_width, window_height = 300, 100
    screen_width = billing.winfo_screenwidth()
    screen_height = billing.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    billing.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    billing.configure(bg="white")
    billing.resizable(width=False, height=False)
    billing.overrideredirect(True)

    splashframe = Frame(billing, highlightbackground="black", highlightthickness=3, width=300, height=110, bd="0",bg="white")
    splashframe.pack()



    file = "Images/preloader.gif"

    info = Image.open(file)

    frames = info.n_frames  # gives total number of frames that gif contains

    # creating list of PhotoImage objects for each frames
    im = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]

    count = 0
    anim = None

    def animation(count):
        global anim
        im2 = im[count]

        gif_label.configure(image=im2)
        count += 1
        if count == frames:
            count = 0
        anim = billing.after(500, lambda: animation(count))

    gif_label = Label(billing, image="", bd="0")
    gif_label.place(x="75", y="25")
    animation(count)

    sending_label = Label(billing, text="Payment Processing...", font="lucida 8 ", bg="white", fg="black")
    sending_label.place(x="80", y="53")
    loading_label = Label(billing, text="Please wait", font="lucida 8 ", bg="white", fg="black")
    loading_label.place(x="110", y="72")
    billing.after(5000,updateStatus)

    billing.mainloop()


def updateStatus():
    billing.destroy()
    con_id = paymentconid_entry.get()
    try:
        con = cx_Oracle.connect('system/12345@localhost:1521/xe')
        cursor = con.cursor()
        cursor.execute(f"""
                        UPDATE CHARGE_MASTER_TRACK SET BILL_STATUS = 'PAID',PAY_DATE = SYSDATE 
                        WHERE CON_ID={con_id} AND BILL_STATUS = 'UNPAID'
                        """)

        cursor.close()
        con.commit()
        messagebox.showinfo("Message","Bill Payed Successfully!")
        con.close()
    except Exception as e:
        messagebox.showerror("Error","Some error occured.")



def sendbill():
    sendb = Toplevel()
    window_width, window_height = 760, 350
    screen_width = sendb.winfo_screenwidth()
    screen_height = sendb.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    sendb.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    sendb.title("Send Bill")
    sendb.configure(bg="white")
    sendb.resizable(width=False, height=False)

    paymentwindow_top = Image.open("Images/sendbill_top.png")
    paymenttop = ImageTk.PhotoImage(paymentwindow_top)
    sendb.photo = paymenttop  # solution for bug in `PhotoImage`
    paymentwindow_toplogo = Label(sendb, image=paymenttop, borderwidth="0")
    paymentwindow_toplogo.place(x="20", y="2")

    paymentwindow_down = Image.open('Images/sendbill_down.png')
    paymentdown = ImageTk.PhotoImage(paymentwindow_down)
    sendb.photo = paymentdown  # solution for bug in `PhotoImage`
    payment_toplogo = Label(sendb, image=paymentdown, borderwidth="0")
    payment_toplogo.place(x="20", y="250")


    global sendbillconid_entry, sendbillbillno_entry

    sendbillconid_label = Label(sendb, text="CON_ID    :", font="lucida 12 bold", bg="white", fg="blue4")
    sendbillconid_label.place(x="235", y="130")
    sendbillconid_entry = Entry(sendb, font="lucida 13 bold ", width="10", bg="grey90", fg="black")
    sendbillconid_entry.place(x="370", y="130")

    sendbillbillno_label = Label(sendb, text="BILL_NO  :", font="lucida 12 bold", bg="white", fg="blue4")
    sendbillbillno_label.place(x="235", y="190")
    sendbillbillno_entry = Entry(sendb, font="lucida 13 bold ", width="10", bg="grey90", fg="black")
    sendbillbillno_entry.place(x="370", y="190")

    idnextbtn = Image.open("Images/next_btn1.png")
    idnextbtn = ImageTk.PhotoImage(idnextbtn)
    sendb.photo3 = idnextbtn
    idnext = Button(sendb, image=idnextbtn, bg="white", bd="0", activebackground='black', command=writeMessage)
    idnext.place(x="540", y="127")

    bnonextbtn = Image.open("Images/next_btn1.png")
    bnonextbtn = ImageTk.PhotoImage(bnonextbtn)
    sendb.photo3 = bnonextbtn
    bnonext = Button(sendb, image=bnonextbtn, bg="white", bd="0", activebackground='black')
    bnonext.place(x="540", y="187")

    sendb.mainloop()

def writeMessage():
    writemsg = Toplevel()
    window_width, window_height = 760, 350
    screen_width = writemsg.winfo_screenwidth()
    screen_height = writemsg.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    writemsg.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    writemsg.title("Bill Message")
    writemsg.configure(bg="white")
    writemsg.resizable(width=False, height=False)

    printbill_back = Image.open("Images/printbill_background1.png")
    sendbillback = ImageTk.PhotoImage(printbill_back)
    writemsg.photo = sendbillback  # solution for bug in `PhotoImage`
    sendbill_bg = Label(writemsg, image=sendbillback, borderwidth="0")
    sendbill_bg.place(x="60", y="2")
    global msg_text
    msg_text = Text(writemsg, font="lucida 10 bold ", width="50", height="7", bg="gray92", fg="black",bd="2")
    msg_text.place(x="155", y="80")

    msg_label = Label(writemsg,text="⚠ Write Important Messages on Bill ⚠", font="lucida 10 bold underline", bg="white", fg="red4")
    msg_label.place(x="220",y="30")

    default_text = "o Tentative meter reading date for your NOV-21 bill is \n   05-11-2021.\no Pay your bill before 20-10-2021.\no"
    msg_text.insert("1.0",default_text)

    mailbillbtn = Image.open("Images/mailbill_btn1.png")
    mailbillbtn = ImageTk.PhotoImage(mailbillbtn)
    writemsg.photo3 = mailbillbtn
    bill_mail_btn = Button(writemsg, image=mailbillbtn, bg="white", bd="0", activebackground='black',command=sendbillsplash)
    bill_mail_btn.place(x="400", y="270")

    printbillbtn = Image.open("Images/printbill_btn.png")
    printbillbtn = ImageTk.PhotoImage(printbillbtn)
    writemsg.photo3 = printbillbtn
    bill_print_btn = Button(writemsg, image=printbillbtn, bg="white", bd="0", activebackground='black',command=pdfGeneration)
    bill_print_btn.place(x="250", y="270")

    writemsg.mainloop()

def pdfGeneration():
    consumer_id = sendbillconid_entry.get()
    # create FPDF object
    # Layout ('P','L')
    # Unit ('mm', 'cm', 'in')
    # format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150))
    pdf = FPDF('P', 'mm', (210, 297))

    # Add a page
    pdf.add_page()

    # specify font
    # fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
    # 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., ('BU'))
    pdf.set_font('helvetica', 'B', 8)
    pdf.set_text_color(0, 0, 0)
    # Add text
    # w = width
    # h = height
    # txt = your text
    # ln (0 False; 1 True - move cursor down to next line)

    # border (0 False; 1 True - add border around cell)
    # pdf.cell(20, 10, 'Hello World!', ln=True)
    pdf.image('Images/bill_toptemplate.png', 5, 5, 200, 47)
    pdf.image("Images/bill_nametemplate.png", 20, 55, 80, 80)
    pdf.image("Images/bill_amounttemplate.png", 17, 135, 85, 65)
    pdf.image("Images/bill_contacttemplate.png", 115, 60, 75, 37)
    pdf.image("Images/bill_consuptiontemplate.png", 113, 103, 75, 50)
    pdf.image("Images/bill_impmsgtemplate.png", 114, 155, 72, 35)
    pdf.image("Images/bill_protocoltemplate.png", 114, 195, 72, 35)
    pdf.image("Images/bill_cuttemplate.png", 5, 240, 200, 8)

    name = "HARIKRISHNAN SATHYAN"
    phone = 9820767941
    pdf.text(30, 79, 'NAME          : ')
    pdf.text(29.9, 84, 'PHONE NO  :')
    pdf.text(30, 89, 'ADDRESS   :')
    pdf.text(30, 104, 'PINCODE    :')
    pdf.text(30, 109, 'EMAIL         :')
    pdf.text(30, 114, 'AADHAR     :')
    pdf.text(30, 119, 'CL in kW     :')

    pdf.set_font('helvetica', 'B', 8)
    pdf.set_text_color(0, 0, 0)
    pdf.text(116, 103, "YOUR CURRENT CONSUMPTION")

    pdf.set_font('helvetica', 'B', 7)
    pdf.text(120, 114, "BILL NO                                  :")
    pdf.text(120, 120, "BILL DATE                             :")
    pdf.text(120, 126, "TYPE OF SUPPLY                 :")
    pdf.text(120, 132, "PRESENT READING             :")
    pdf.text(120, 138, "PREVIOUS READING           :")
    pdf.text(120, 144, "CONSUPTION (UNIT kWh)   :")
    imp_msg = msg_text.get("1.0", END)
    pdf.set_xy(117, 166)
    pdf.multi_cell(200, 4,f"{imp_msg}")

    pdf.set_font('helvetica', 'B', 10)
    pdf.text(46, 209, "JOIN US ON")

    pdf.image("Images/bill_fbtemplate.png", 30, 213, 10, 10, link="https://www.facebook.com/")
    pdf.image("Images/bill_instatemplate.png", 45, 213, 10, 10, link="https://www.instagram.com/?hl=en")
    pdf.image("Images/bill_youtubetemplate.png", 60, 213, 10, 10, link="https://www.youtube.com/")
    pdf.image("Images/bill_linkedintemplate.png", 75, 213, 10, 10, link="https://in.linkedin.com/")

    # Check slip
    pdf.image("Images/bill_paysliptemplate.png", 7, 248, 8, 40)
    pdf.image("Images/bill_barcodetemplate.png", 20, 264, 100, 10)
    pdf.image("Images/bill_payslip2template.png", 20, 276, 145, 10)

    pdf.set_font('helvetica', '', 7)
    pdf.text(20, 250, "If paying by cheque, please remember:")
    pdf.text(20, 254, "- Cheque should be Account payee of local clearing and not post-dated")
    pdf.text(20, 258,
             "- Always attach payment slip. Do not staple         - Make cheque payable to Electrica Electricity Mumbai Ltd. A/C No.:152191709")
    pdf.text(20, 262,
             "- Mention A/c No. and respective amount on back of the cheque,when making multiple bill payments by single cheque")
    pdf.set_font('helvetica', 'B', 7)
    pdf.text(25, 280, "BILL DATE : ")
    pdf.text(96, 280, "BILL AMOUNT : ")
    pdf.text(25, 284.5, "DUE DATE : ")
    pdf.text(96, 284.5, "AMOUNT AFTER DUE DATE : ")

    # VALUES OF THE FIELDS


    con = cx_Oracle.connect('system/12345@localhost:1521/xe')
    cursor = con.cursor()
    consumer_details = cursor.execute(f"""
                                   SELECT CON_NAME,PHONE_NO,ADDRESS1,ADDRESS2,ADDRESS3,PIN_CODE,EMAILID,AADHAR,
                                   SUPPLY_TYPE,REQUIREMENT FROM ADD_CONSUMER WHERE CON_ID={consumer_id}
                                    """)
    details_list = consumer_details.fetchall()
    for con_values in details_list:
        emailid = con_values[6]
        encpt_emailid = emailid[0:3] + "******" + emailid[-10:]

        aadhar = str(con_values[7])
        encpt_aadhar = aadhar[0:3] + "******" + aadhar[-3:]

        pdf.set_font('helvetica', '', 7)
        pdf.text(50, 79, f"{con_values[0]}")
        pdf.text(50, 84, f"{con_values[1]}")
        pdf.text(50, 89, f"{con_values[2]}")
        pdf.text(50, 94, f"{con_values[3]}")
        pdf.text(50, 99, f"{con_values[4]}")
        pdf.text(50, 104, f"{con_values[5]}")
        pdf.text(50, 109, f"{encpt_emailid}")
        pdf.text(50, 114, f"{encpt_aadhar}")
        pdf.text(50, 119, f"{con_values[9]}")
        pdf.set_font('helvetica', 'B', 7)
        pdf.text(63, 62, f"{con_values[8]}")

    bill_details = cursor.execute(f"""
                                   SELECT *  FROM CHARGE_MASTER_TRACK WHERE CON_ID = {consumer_id}
                                    """)
    bill_details_list = bill_details.fetchall()
    for details in bill_details_list:
        pdf.set_font('helvetica', '', 7)
        pdf.text(155, 114, f"{details[14]}")
        pdf.text(155, 120, f"{str(details[2])[:11]}")
        pdf.text(155, 126, f"{details[1]}")
        pdf.text(155, 132, f"{details[4]}")
        pdf.text(155, 138, f"{details[3]}")
        pdf.text(155, 144, f"{details[5]}")
        pdf.text(40, 280, f"{str(details[2])[:11]}")
        bill_amt = str(details[7])
        o = ".00"
        pdf.text(115, 280, f"{bill_amt}{o}/- Rs")
        bill_amt_aftdue = str(details[7] + 50)
        o = ".00"
        pdf.text(131, 284.5, f"{bill_amt_aftdue}{o}/- Rs")
        pdf.set_font('helvetica', 'B', 14)
        pdf.text(51.5, 191.5, f"{bill_amt}{o}")

        pdf.set_font('helvetica', 'B', 8)

        pdf.text(65, 148, f"{details[0]}")
        pdf.text(65, 159, f"{details[15]}")

    pdf.add_page()

    pdf.image("Images/bill_howtemplate.png", 7, 10, 110, 100)
    pdf.image("Images/bill_protocol2template.png", 135, 11, 60, 94)
    pdf.image("Images/bill_triff2template.png", 68, 120, 130, 35)
    pdf.image("Images/bill_trifftoptemplate.png", 66, 113, 135, 6)
    pdf.image("Images/bill_billsumtemplate.png", 6, 109, 60, 50)

    pdf.set_font('helvetica', 'B', 10)
    pdf.text(13, 20, "HOW BILL WAS CALCULATED ")
    pdf.set_font('helvetica', 'B', 7)

    pdf.text(13, 33, "FIXED CHARGE ")
    pdf.text(13, 38.5, "WHEELING CHARGE")
    pdf.text(13, 43.8, "REGULATORY ASSET CHARGE (RAC)")
    pdf.text(13, 49.2, "ENERGY CHARGE")
    pdf.text(13, 54.4, "FUEL ADJUSTMENT CHARGE (FAC)")
    pdf.text(13, 60, "GOVERNMENT ELECTRICITY DUTY                                       16%")
    pdf.text(13, 65.2, "MAHARASHTRA GOVT. TAX ON SALE OF ELECTRICITY     26.04 p/unit")
    pdf.text(13, 70.5, "CURRENT MONTHS BILL AMOUNT (A)")
    pdf.text(13, 75.8, "PREVIOUS MONTHS BILL AMOUNT")
    pdf.text(13, 81.3, "PROMPT PAYMENT DISCOUNT")
    pdf.text(13, 86.8, "NET PREVIOUS BALANCE (B)")
    pdf.text(13, 91.9, "TOTAL BILL AMOUNT (A+B)")
    pdf.text(69, 116, "KEEP A WATCH TO MANAGE YOUR ELECTRICITY CONSUPTION")

    pdf.set_font('helvetica', '', 5)
    pdf.text(69, 118, "YOUR TRIFF STRUCTURE")

    pdf.set_font('helvetica', 'B', 9)
    pdf.text(11, 123, "ROUND SUM")
    pdf.text(11, 128, "PAYABLE")
    pdf.text(11, 133, "FOR THIS BILL")

    pdf.set_font('helvetica', 'B', 6)
    pdf.text(10, 143, "METER READING DATE")
    pdf.text(10, 149, "PREVIOUS METER")
    pdf.text(10, 151, "READING DATE")

    bill_details = cursor.execute(f"""
                                   SELECT *  FROM CHARGE_MASTER_TRACK WHERE CON_ID = {consumer_id}
                                    """)
    bill_details_list = bill_details.fetchall()
    for details in bill_details_list:
        pdf.set_font('helvetica', '', 8)
        pdf.text(103, 33, f"{details[8]}/-")
        pdf.text(103, 38.3, f"{details[10]}/-")
        pdf.text(103, 43.7, f"0.00/-")
        pdf.text(103, 49.3, f"{details[9]}/-")
        pdf.text(103, 54.4, f"0.00/-")
        pdf.text(103, 60, f"{details[11]}/-")
        pdf.text(103, 65.4, f"{details[4] * 0.26}/-")
        pdf.text(103, 70.5, f"{details[7]}/-")
        pdf.text(103, 75.5, f"{details[6]}/-")
        pdf.text(103, 81, f"0/-")
        pdf.text(103, 87.1, f"{details[6]}/-")
        pdf.text(103, 92, f"{details[7]}/-")

        pdf.set_font('helvetica', 'B', 9)
        pdf.text(43, 127, f"{details[7]}/- Rs")

    pdf.output('C:/Users/Vandana/Documents/Clg Doc/OneDrive/ProjectGit/Electrica/Bill.pdf')
    webbrowser.open_new(r'file://C:/Users/Vandana/Documents/Clg Doc/OneDrive/ProjectGit/Electrica/Bill.pdf')

def sendbillsplash():
    global sendsplash
    sendsplash = Toplevel()
    window_width, window_height = 300, 100
    screen_width = sendsplash.winfo_screenwidth()
    screen_height = sendsplash.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    sendsplash.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    sendsplash.configure(bg="white")
    sendsplash.resizable(width=False, height=False)
    sendsplash.overrideredirect(True)

    splashframe = Frame(sendsplash, highlightbackground="black", highlightthickness=3, width=300, height=110, bd="0",bg="white")
    splashframe.pack()


    file = "Images/loader2.gif"

    info = Image.open(file)

    frames = info.n_frames  # gives total number of frames that gif contains

    # creating list of PhotoImage objects for each frames
    im = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]

    count = 0
    anim = None

    def animation(count):
        global anim
        im2 = im[count]

        gif_label.configure(image=im2)
        count += 1
        if count == frames:
            count = 0
        anim = sendsplash.after(50, lambda: animation(count))

    gif_label = Label(sendsplash, image="", bd="0")
    gif_label.place(x="110", y="3")
    animation(count)

    sending_label = Label(sendsplash, text="Sending...", font="lucida 8 ", bg="white", fg="black")
    sending_label.place(x="117", y="55")
    loading_label = Label(sendsplash, text="Please wait", font="lucida 8 ", bg="white", fg="black")
    loading_label.place(x="110", y="74")
    sendsplash.after(3000, mailbill)

    sendsplash.mainloop()


def mailbill():
    consumer_id = sendbillconid_entry.get()
    con = cx_Oracle.connect('system/12345@localhost:1521/xe')
    cursor = con.cursor()
    x = cursor.execute(f"SELECT * FROM ADD_CONSUMER WHERE CON_ID = {consumer_id}")
    values = x.fetchall()
    for i in values:
        name = i[1]
        supply = i[10]
        requrement = i[14]
        email = i[7]
        print(name,supply,requrement,email)
        # Create an object of sendpdf function
        k = sendpdf("electrica.org@gmail.com",
                    f"{email}",
                    "Electrica@1234",
                    "Electrica Bill",
                    f"Dear {name} ,\nYour connection request for {supply} ({requrement}) current supply has been approved.\nConnection will be established within 24hrs.\n\nRegards,\nElectrica",
                    "Bill",
                    "C:/Users/Vandana/Documents/Clg Doc/OneDrive/ProjectGit/Electrica")

    # sending an email
        k.email_send()
        showpopup()

def showpopup():
    sendsplash.destroy()
    messagebox.showinfo("Message","Mail send Successfully!")



homeWindow()

# writeMessage()
# pay()
# showbilling()

# sendmailsplash()
# splash()
# sendingwmsg()
# splash()
# alerts()
# editwindow()
# security()
# enterReadings()

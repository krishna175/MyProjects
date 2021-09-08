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



def notifyrecmail():
    notification.notify(
        title = "Mail send",
        message = "Receipt sent to the Consumer",
        timeout = 1
    )
    time.sleep(0)

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
                    f"Dear {name} ,\nYour connection for request for {supply} ({requrement}) current supply has been approved.\nConnection will be established within 24hrs.\n\nRegards,\nElectrica",
                    "Receipt",
                    "C:/Users/Vandana/Documents/Clg Doc/OneDrive/ProjectGit/Electrica")

    # sending an email
        k.email_send()
        notifyrecmail()

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
                    f"Dear {name} ,\nYour connection for request for {supply} ({requrement}) current supply has been approved.\nConnection will be established within 24hrs.\n\nRegards,\nElectrica",
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
    button_readings = Button(home, image=readings_image, borderwidth="0",command=enterReadings)
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

    defaulter_size = Image.open("Images/defaulters_btn.png")
    defaulter_resized = defaulter_size.resize((220, 50), Image.ANTIALIAS)
    defaulter_image = ImageTk.PhotoImage(defaulter_resized)
    Label(image=defaulter_image)
    button_defaulter = Button(home, image=defaulter_image, borderwidth="0")
    button_defaulter.place(x=530, y=380)

    fraud_size = Image.open("Images/fraud.png")
    fraud_resized = fraud_size.resize((220, 50), Image.ANTIALIAS)
    fraud_image = ImageTk.PhotoImage(fraud_resized)
    Label(image=fraud_image)
    button_fraud = Button(home, image=fraud_image, borderwidth="0")
    button_fraud.place(x=530, y=450)

    payment_size = Image.open( "Images/payment_btn.png")
    payment_resized = payment_size.resize((220, 50), Image.ANTIALIAS)
    payment_image = ImageTk.PhotoImage(payment_resized)
    Label(image=payment_image)
    button_payment = Button(home, image=payment_image, borderwidth="0")
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
    submit_receipt = Button(condisplay, image=mailbtn, bg="white", bd="0", activebackground='green',command=sendmail)
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

    printbtn = Image.open("Images/print_btn.png")
    printbtn = ImageTk.PhotoImage(printbtn)
    condisplay.photo3 = printbtn
    submit_receipt = Button(condisplay, image=printbtn, bg="white", bd="0", activebackground='green',command=printrec)
    submit_receipt.place(x="370", y="850")

    mailbtn = Image.open("Images/mail_btn.png")
    mailbtn = ImageTk.PhotoImage(mailbtn)
    condisplay.photo3 = mailbtn
    submit_receipt = Button(condisplay, image=mailbtn, bg="white", bd="0", activebackground='green',command=sendeditmail)
    submit_receipt.place(x="530", y="850")

    print("Consumer details displayed")

    condisplay.mainloop()

def editentries():
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
    industry_radio = Radiobutton(editconentry, image=indsymbol, variable=uvar, bg="white", fg="blue", font="2",
                                 value="INDUSTRIAL", bd="0", activebackground="white")
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

def showupdatemessage():
    messagebox.showinfo("Message", "Details Updated Successfully!")
    showentry()

def enterReadings():
    meterread = Toplevel()
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
    receipt_toplogo.place(x="37", y="250")

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




    meterread.mainloop()





homeWindow()

# editwindow()
# security()
# enterReadings()

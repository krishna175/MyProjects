import pyautogui
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import cx_Oracle



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

    conentry_left = Image.open("Images/charges.png")
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

    cursor.close()
    con.commit()
    con.close()

def displayentry():
    condisplay = Toplevel()
    window_width, window_height = 1000, 950
    screen_width = condisplay.winfo_screenwidth()
    screen_height = condisplay.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    condisplay.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    condisplay.title("DISPLAY DETAILS")
    condisplay.configure(bg="white")
    condisplay.resizable(width=False, height=False)
    condisplay.iconbitmap('Images/icon2.ico')

    conentry_top = Image.open("Images/adcon_toptemp.png")
    entrytop = ImageTk.PhotoImage(conentry_top)
    condisplay.photo = entrytop  # solution for bug in `PhotoImage`
    receipt_toplogo = Label(condisplay, image=entrytop, borderwidth="0")
    receipt_toplogo.place(x="37", y="2")

    con_name = Label(condisplay, text="Connection Charges :  ", font="lucida 9 bold ", bg="white",fg="red")
    con_name.place(x="75", y="240")
    conentry_left = Image.open("Images/connectionchageimg.png")
    entryleft = ImageTk.PhotoImage(conentry_left)
    condisplay.photo = entryleft  # solution for bug in `PhotoImage`
    receipt_leftcharges = Label(condisplay, image=entryleft, borderwidth="0")
    receipt_leftcharges.place(x="70", y="270")

    gpay_logo = Image.open("Images/payment_image.png")
    gpay_logo = ImageTk.PhotoImage(gpay_logo)
    condisplay.photo2 = gpay_logo  # solution for bug in `PhotoImage`
    rec_gpay_logo = Label(condisplay, image=gpay_logo, borderwidth="0", bg="white")
    rec_gpay_logo.place(x="100", y="490")

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

    con_namedis = Label(condisplay, text="HARIKRISHNAN SATHYAN ", font="lucida 12 bold ", bg="white", fg="black")
    con_namedis.place(x="530", y="152")

    conphonedis = Label(condisplay, text="9820767948 ", font="lucida 12 bold ", bg="white", fg="black")
    conphonedis.place(x="530", y="202")

    address1 = Label(condisplay, text="B-403 DIVYA APT, ", font="lucida 11 bold ", bg="white", fg="black")
    address1.place(x="530", y="252")
    address2 = Label(condisplay, text="TRIVENI NAGAR, KURAR VILLAGE, ", font="lucida 11 bold ", bg="white", fg="black")
    address2.place(x="530", y="280")
    address3 = Label(condisplay, text="NEAR JOYTI HOTEL, MALAD(E)", font="lucida 11 bold ", bg="white", fg="black")
    address3.place(x="530", y="310")
    pincode = Label(condisplay, text="PINCODE : 400097", font="lucida 11 bold ", bg="white", fg="black")
    pincode.place(x="530", y="340")

    emaildis = Label(condisplay, text="harikrishnansathyan2001@gmail.com", font="lucida 11 bold ", bg="white",fg="black")
    emaildis.place(x="530", y="400")

    aadhardis = Label(condisplay, text="682938721393", font="lucida 11 bold ", bg="white", fg="black")
    aadhardis.place(x="530", y="450")

    pandis = Label(condisplay, text="PB938092", font="lucida 11 bold ", bg="white", fg="black")
    pandis.place(x="530", y="500")

    supplytypedis = Label(condisplay, text="SINGLE PHASE (10 - 15 kW)", font="lucida 11 bold ", bg="white", fg="black")
    supplytypedis.place(x="530", y="550")

    usagedis = Label(condisplay, text="DOMESTIC", font="lucida 11 bold ", bg="white", fg="black")
    usagedis.place(x="530", y="600")

    meterdis = Label(condisplay, text="2342355", font="lucida 11 bold ", bg="white", fg="black")
    meterdis.place(x="530", y="650")

    stcharge = Label(condisplay, text="50", font="lucida 11 bold ", bg="goldenrod1", fg="black")
    stcharge.place(x="185", y="303")

    cc = Label(condisplay, text="2000", font="lucida 11 bold ", bg="goldenrod1", fg="black")
    cc.place(x="185", y="354")

    cctotal = Label(condisplay, text="250075", font="lucida 11 bold ", bg="goldenrod1", fg="black")
    cctotal.place(x="185", y="393")




    printbtn = Image.open("Images/print_btn.png")
    printbtn = ImageTk.PhotoImage(printbtn)
    condisplay.photo3 = printbtn
    submit_receipt = Button(condisplay, image=printbtn, bg="white", bd="0", activebackground='green')
    submit_receipt.place(x="370", y="850")

    mailbtn = Image.open("Images/mail_btn.png")
    mailbtn = ImageTk.PhotoImage(mailbtn)
    condisplay.photo3 = mailbtn
    submit_receipt = Button(condisplay, image=mailbtn, bg="white", bd="0", activebackground='green')
    submit_receipt.place(x="530", y="850")

    condisplay.mainloop()



# homeWindow()
displayentry()
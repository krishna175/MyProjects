import pyautogui
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox


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

    con_name = Label(conentry, text="Name : ", font="lucida 12 bold ", bg="white", fg="blue4")
    con_name.place(x="300", y="150")
    conname_entry = Entry(conentry, width="40", font="lucida 12", bd="3", bg="grey94")
    conname_entry.place(x="530", y="150")

    conphone = Label(conentry, text="Phone No : ", font="lucida 12 bold ", bg="white", fg="blue4")
    conphone.place(x="300", y="200")
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
    address1_entry = Entry(conentry, width="35", font="lucida 11", bd="3", bg="grey94")
    address1_entry.place(x="530", y="330")

    address3_label = Label(conentry, text="Landmark, Town/City         :", font="lucida 10 bold", bg="white", fg="blue4")
    address3_label.place(x="300", y="370")
    address1_entry = Entry(conentry, width="35", font="lucida 11", bd="3", bg="grey94")
    address1_entry.place(x="530", y="370")

    pincode_label = Label(conentry, text="Pincode                              :", font="lucida 10 bold", bg="white", fg="blue4")
    pincode_label.place(x="300", y="410")
    address1_entry = Entry(conentry, width="15", font="lucida 11", bd="3", bg="grey94")
    address1_entry.place(x="530", y="410")

    email_label = Label(conentry, text="Email :",font="lucida 12 bold" ,bg="white",fg="blue4")
    email_label.place(x="300",y="460")
    email_entry = Entry(conentry, width="30", font="lucida 12", bd="3", bg="grey94")
    email_entry.place(x="530", y="460")

    aadhar_label = Label(conentry, text="Aadhar No:",font="lucida 12 bold", bg="white",fg="blue4")
    aadhar_label.place(x="300",y="510")
    aadhar_entry = Entry(conentry, width="13", font="lucida 12", bd="3", bg="grey94")
    aadhar_entry.place(x="530", y="510")

    pan_label = Label(conentry, text="PAN : ", font="lucida 12 bold", bg="white", fg="blue4")
    pan_label.place(x="300", y="560")
    pan_entry = Entry(conentry, width="13", font="lucida 12", bd="3", bg="grey94")
    pan_entry.place(x="530", y="560")

    supplytype_label = Label(conentry, text="Supply Type :", font="lucida 12 bold", bg="white", fg="blue4")
    supplytype_label.place(x="300", y="610")
    list1 = ['SINGLE PHASE','TWO PHASE','THREE PHASE']
    click = StringVar()
    click.set("Select Type")
    test_dropdown = OptionMenu(conentry, click, *list1)
    test_dropdown.config(bg="blue4", fg="white", width="12", activebackground="dodger blue", activeforeground="black")
    test_dropdown.place(x="530", y="610")

    usage_label = Label(conentry, text="Purpose of Supply :", font="lucida 12 bold", bg="white", fg="blue4")
    usage_label.place(x="300", y="660")
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

    meter_label = Label(conentry, text="Meter No: ", font="lucida 12 bold", bg="white", fg="blue4")
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
    submit_receipt.place(x="855", y="780")


    conentry.mainloop()

def submit():
    declaration = declare.get()
    if(declaration==0):
        messagebox.showinfo("Message", "Please select the declaration Checkbox")
    else:
        print("inserting to db")

homeWindow()
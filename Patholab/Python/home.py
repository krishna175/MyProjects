from tkinter import *
import os
from PIL import ImageTk,Image
import tkinter as tk
import sqlite3
from tkinter import messagebox
import pyautogui
import pygetwindow
from datetime import datetime
import webbrowser
from plyer import notification
import time

import requests
from pygame import mixer
from datetime import datetime, timedelta
import webbrowser
import tkinter as tk
from tkinter import filedialog





def notifyrecmail():
    messagebox.showinfo("Mail", "Mail sent successfully!.")

def showError():
    messagebox.showerror("Message", "Entry field should not be empty.")



def homewindow():
    home = Tk()
    home.configure(bg="white")
    home.title('Patholab')
    home.resizable(False,False)
    home.iconbitmap("Images/icon4.ico")
    window_width, window_height = 885, 650

    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    home.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    temp_size = Image.open("Images/home_template2.png")
    temp_resized = temp_size.resize((395,655), Image.ANTIALIAS)
    template = ImageTk.PhotoImage(temp_resized)
    template_image = Label(home,image=template,borderwidth="0")
    template_image.place(x="-1",y="-3")

    backtemplate_size = Image.open("Images/back1.jpg")
    backtemplate_resized = backtemplate_size.resize((410,700), Image.ANTIALIAS)
    backtemplate = ImageTk.PhotoImage(backtemplate_resized)
    backtemplate_image = Label(home,image=backtemplate,borderwidth="0")
    backtemplate_image.place(x="430",y="0")


    receipt_size = Image.open("Images/receipt_button.png")
    receipt_resized = receipt_size.resize((220,50), Image.ANTIALIAS)
    receipt_image = ImageTk.PhotoImage(receipt_resized)
    Label(image=receipt_image)
    button_receipt = Button(home,image=receipt_image,borderwidth="0",activebackground='blue',command=receiptEntry)
    button_receipt.place(x=530,y=30)

    editreceipt_size = Image.open("Images/editreceipt_button.png")
    editreceipt_resized = editreceipt_size.resize((220,50), Image.ANTIALIAS)
    editreceipt_image = ImageTk.PhotoImage(editreceipt_resized)
    Label(image=editreceipt_image)
    button_editreceipt = Button(home,image=editreceipt_image,borderwidth="0",activebackground='blue',command=editReceipt)
    button_editreceipt.place(x=530,y=100)

    taketest_size = Image.open("Images/taketest_button.png")
    taketest_resized = taketest_size.resize((220,50), Image.ANTIALIAS)
    taketest_image = ImageTk.PhotoImage(taketest_resized)
    Label(image=taketest_image)
    button_taketest = Button(home,image=taketest_image,borderwidth="0",command=takeTest)
    button_taketest.place(x=530,y=170)



    covtest_size = Image.open("Images/covidtest_button.png")
    covtest_resized = covtest_size.resize((220,50), Image.ANTIALIAS)
    covtest_image = ImageTk.PhotoImage(covtest_resized)
    Label(image=covtest_image)
    button_covtest = Button(home,image=covtest_image,borderwidth="0")
    button_covtest.place(x=530,y=240)

    sendreport_size = Image.open("Images/sendreport_button.png")
    sendreport_resized = sendreport_size.resize((220,50), Image.ANTIALIAS)
    sendreport_image = ImageTk.PhotoImage(sendreport_resized)
    Label(image=sendreport_image)
    button_sendreport = Button(home,image=sendreport_image,borderwidth="0")
    button_sendreport.place(x=530,y=310)

    deletereport_size = Image.open("Images/deletereport_button.png")
    deletereport_resized = deletereport_size.resize((220,50), Image.ANTIALIAS)
    deletereport_image = ImageTk.PhotoImage(deletereport_resized)
    Label(image=deletereport_image)
    button_deletereport = Button(home,image=deletereport_image,borderwidth="0")
    button_deletereport.place(x=530,y=380)

    vcard_size = Image.open("Images/vcard_button.png")
    vcard_resized = vcard_size.resize((220,50), Image.ANTIALIAS)
    vcard_image = ImageTk.PhotoImage(vcard_resized)
    Label(image=vcard_image)
    button_vcard = Button(home,image=vcard_image,borderwidth="0",command=vcard_entry)
    button_vcard.place(x=530,y=450)

    vaccineslot_size = Image.open("Images/vaccineslot_button.png")
    vaccineslot_resized = vaccineslot_size.resize((220,50), Image.ANTIALIAS)
    vaccineslot_image = ImageTk.PhotoImage(vaccineslot_resized)
    Label(image=vaccineslot_image)
    button_vaccineslot = Button(home,image=vaccineslot_image,borderwidth="0",command=age_pin)
    button_vaccineslot.place(x=530,y=520)

    exit_size = Image.open("Images/Exit_buttons.png")
    exit_resized = exit_size.resize((60,25), Image.ANTIALIAS)
    exit_image = ImageTk.PhotoImage(exit_resized)
    Label(image=exit_image)
    button_exit = Button(home,image=exit_image,borderwidth="0",activebackground='red',command=home.destroy)
    button_exit.place(x=818,y=620)

    home.mainloop()

def receiptEntry():
    global recname_entry,recage_entry,var,recphone_entry,recemail_entry,click,rentry,recrefdr_entry
    rentry = Toplevel()

    window_width, window_height = 1000, 570
    screen_width = rentry.winfo_screenwidth()
    screen_height = rentry.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    rentry.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    rentry.title("RECEIPT ENTRY")
    rentry.configure(bg="white")
    rentry.resizable(width=False, height=False)
    rentry.iconbitmap('C:/gui/icon4.ico')

    rentry_top = Image.open("Images/receipt_temp.png")
    rephoto = ImageTk.PhotoImage(rentry_top)
    rentry.photo = rephoto  # solution for bug in `PhotoImage`
    receipt_toplogo = Label(rentry, image=rephoto, borderwidth="0")
    receipt_toplogo.place(x="37",y="15")

    rentry_down = Image.open("Images/Receipt_temp_ss_down.png")
    rephoto2 = ImageTk.PhotoImage(rentry_down)
    rentry.photo2 = rephoto2  # solution for bug in `PhotoImage`
    receipt_downlogo = Label(rentry, image=rephoto2, borderwidth="0")
    receipt_downlogo.place(x="37", y="450")

    gpay_logo = Image.open("Images/payment_image.png")
    gpay_logo = ImageTk.PhotoImage(gpay_logo)
    rentry.photo2 = gpay_logo  # solution for bug in `PhotoImage`
    rec_gpay_logo = Label(rentry, image=gpay_logo, borderwidth="0",bg="white")
    rec_gpay_logo.place(x="100", y="230")


    rec_name = Label(rentry,text="Name : ",font="lucida 12 bold ",bg="white",fg="blue4")
    rec_name.place(x="300",y="150")
    recname_entry = Entry(rentry,width="40",font="lucida 12",bd="3")
    recname_entry.place(x="380",y="150")

    rec_age = Label(rentry,text="Age : ",font="lucida 12 bold",bg="white",fg="blue4")
    rec_age.place(x="300",y="200")
    recage_entry = Entry(rentry,width="5",font="lucida 12",bd="3")
    recage_entry.place(x="370",y="200")

    var=StringVar()
    rec_gender = Label(rentry, text="Gender : ", font="lucida 12 bold", bg="white", fg="blue4")
    rec_gender.place(x="470", y="200")

    msymbol = Image.open("Images/male.png")
    msymbol = ImageTk.PhotoImage(msymbol)
    rentry.photo = msymbol  # solution for bug in `PhotoImage`
    mgender_radio = Radiobutton(rentry,image=msymbol,variable=var,bg="white",fg="blue",font="2",value="MALE")
    mgender_radio.place(x="560",y="198")

    fsymbol = Image.open("Images/femenine.png")
    fsymbol = ImageTk.PhotoImage(fsymbol)
    rentry.photo = fsymbol  # solution for bug in `PhotoImage`
    fgender_radio = Radiobutton(rentry,image=fsymbol,variable=var,bg="white",fg="blue",font="2",value="FEMALE")
    fgender_radio.place(x="630",y="198")

    rec_phone = Label(rentry, text="Mobile no : ", font="lucida 12 bold", bg="white", fg="blue4")
    rec_phone.place(x="300", y="250")
    recphone_entry = Entry(rentry, width="15", font="lucida 12", bd="3")
    recphone_entry.place(x="420", y="250")

    rec_refdr = Label(rentry, text="Ref.By Dr : ", font="lucida 12 bold", bg="white", fg="blue4")
    rec_refdr.place(x="300", y="300")
    recrefdr_entry = Entry(rentry, width="19", font="lucida 12", bd="3")
    recrefdr_entry.place(x="420", y="300")


    rec_test = Label(rentry, text="Test : ", font="lucida 12 bold", bg="white", fg="blue4")
    rec_test.place(x="300", y="350")
    list1 = ['Complete Blood Count','RT-PCR','Prothrobin Time', 'Basic Metabolic Panel', 'Comprehensive Metabolic Panel', 'Lipid Panel', 'Liver Panel', 'Thyroid Stimulating Hormone', 'Hemoglobin A1C', 'Urinalysis', 'Cultures']
    click=StringVar()
    click.set("Select Test")
    test_dropdown = OptionMenu(rentry,click,*list1)
    test_dropdown.config(bg="blue4",fg="white",width="26",activebackground="dodger blue",activeforeground="black")
    test_dropdown.place(x="370",y="345")

    rec_email = Label(rentry, text="e-mail id : ", font="lucida 12 bold", bg="white", fg="blue4")
    rec_email.place(x="300", y="400")
    recemail_entry = Entry(rentry, width="30",font="lucida 12", bd="3")
    recemail_entry.place(x="420", y="400")

    submitsymbol = Image.open("Images/submit_button.png")
    submitsymbol = ImageTk.PhotoImage(submitsymbol)
    rentry.photo3 = submitsymbol
    submit_receipt = Button(rentry,image=submitsymbol,bg="white",bd="0",activebackground='green',command=receiptInsertdb)
    submit_receipt.place(x="800",y="400")

    rentry.mainloop()

def receiptInsertdb():
    # global recname_entry, recage_entry, var, recphone_entry, recemail_entry, click
    name = str(recname_entry.get())
    age = recage_entry.get()
    gender = var.get()
    phone = recphone_entry.get()
    doc =  recrefdr_entry.get()
    test = str(click.get())
    email = str(recemail_entry.get())
    timenow  =(datetime.today().strftime("%I:%M %p"))

    # testamt = 750
    if (test == "Complete Blood Count"):
        testamt=700
    elif(test=="RT-PCR"):
        testamt=500
    elif(test == "Prothrobin Time"):
        testamt = 750
    elif(test=="Basic Metabolic Panel"):
        testamt=800
    elif(test=="Comprehensive Metabolic Panel"):
        testamt=900
    elif(test=="Lipid Panel"):
        testamt=500
    elif(test=="Liver Panel"):
        testamt=950
    elif(test=="Thyroid Stimulating Hormone"):
        testamt=750
    elif(test=="Hemoglobin A1C"):
        testamt=1200
    elif(test=="Urinalysis"):
        testamt=600
    elif(test=="Cultures"):
        testamt=1100
    else:
        testamt=500

    try:
        conn = sqlite3.connect('Labdb.db')
        cur = conn.cursor()
        cur.execute(f"INSERT INTO Receipt values((SELECT max (REC_ID)+1 from Receipt),'{name}',{age},'{gender}',{phone},'{email}','{test}','{doc}',{testamt},STRFTIME('%d/%m/%Y'),'{timenow}')")  # get method gets values from the variable
        cur.close()
        conn.commit()
        conn.close()
        showmessage()
    except Exception as e:
        showError()

def receiptDisplay():
    redisp = Tk()
    label_name = Label(redisp,text=str(f"{var.get()}"))
    label_name.pack()
    redisp.mainloop()

def showmessage():
    messagebox.showinfo("Message", "Receipt created successfully!")
    rentry.destroy()
    displayReceipt()

def printrec():
    path = "Receipt_i.png"
    titles =pygetwindow.getAllTitles()

    # x1, y1 = width, height = pygetwindow.getWindowsWithTitle('Patholab')
    window = pygetwindow.getWindowsWithTitle('RECEIPT')[0]
    x1 = window.left+10
    y1 = window.top+50
    height = window.height-110
    width = window.width-20
    x2 = x1 + width
    y2 = y1 + height

    pyautogui.screenshot(path)

    im = Image.open(path)
    im = im.crop((x1,y1,x2,y2))
    im.save(path)
    # im.show(path)
    pdfconv()

def pdfconv():
    filename = "Receipt_i.png"
    image = Image.open(filename)

    if image.mode == "RGBA":
        image = image.convert("RGB")
    output = "Receipt.pdf"
    image.save(output, "PDF", resolution=100.0)
    sendmail()

def sendmail():
    from pdf_mail import sendpdf
    conn = sqlite3.connect('Labdb.db')
    cur = conn.cursor()
    rvalue = cur.execute("SELECT NAME,EMAIL_ID,TEST FROM Receipt WHERE REC_ID = (SELECT max (REC_ID) FROM Receipt) ")
    emaildetails = rvalue.fetchall()
    for i in emaildetails:
        recepent_name = str(i[0])
        recepent_email = str(i[1])
        recepent_test = str(i[2])


    # Create an object of sendpdf function
        k = sendpdf("patholabsreport@gmail.com",
                    f"{recepent_email}",
                    "Patho@175",
                    "Patholab Receipt",
                    f"Dear {recepent_name},\nThis is the receipt for your {recepent_test} test.\nTest report will be sent to you before 6:00 PM. \n\nRegards,\nPatholab",
                    "Receipt",
                    f"{os.getcwd()}"
                    )
        print(os.getcwd())
    # sending an email
        k.email_send()
        # showmailmessage()
        notifyrecmail()


def eprintrec():
    path = "Receipt_i.png"
    titles =pygetwindow.getAllTitles()

    # x1, y1 = width, height = pygetwindow.getWindowsWithTitle('Patholab')
    window = pygetwindow.getWindowsWithTitle('RECEIPT')[0]
    x1 = window.left+10
    y1 = window.top+50
    height = window.height-110
    width = window.width-20
    x2 = x1 + width
    y2 = y1 + height

    pyautogui.screenshot(path)

    im = Image.open(path)
    im = im.crop((x1,y1,x2,y2))
    im.save(path)
    # im.show(path)
    epdfconv()

def epdfconv():
    filename = "Receipt_i.png"
    image = Image.open(filename)

    if image.mode == "RGBA":
        image = image.convert("RGB")
    output = "Receipt.pdf"
    image.save(output, "PDF", resolution=100.0)
    sendeditmail()


def sendeditmail():
    from pdf_mail import sendpdf
    conn = sqlite3.connect('Labdb.db')
    cur = conn.cursor()
    rvalue = cur.execute(f"SELECT NAME,EMAIL_ID,TEST FROM Receipt WHERE REC_ID = {recid} ")
    emaildetails = rvalue.fetchall()
    for i in emaildetails:
        recepent_name = str(i[0])
        recepent_email = str(i[1])
        recepent_test = str(i[2])


    # Create an object of sendpdf function
        k = sendpdf("patholabsreport@gmail.com",
                    f"{recepent_email}",
                    "Patho@175",
                    "Patholab Receipt",
                    f"Dear {recepent_name},\nThis is the receipt for your {recepent_test} test.\nTest report will be sent to you before 6:00 PM. \n\nRegards,\nPatholab",
                    "Receipt",
                    f"{os.getcwd()}"
                    )
        print(os.getcwd())
    # sending an email
        k.email_send()
        # showmailmessage()
        notifyrecmail()

def displayReceipt():
    rdisplay = Toplevel()

    window_width, window_height = 1000, 630
    screen_width = rdisplay.winfo_screenwidth()
    screen_height = rdisplay.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    rdisplay.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    rdisplay.title("RECEIPT")
    rdisplay.configure(bg="white")
    rdisplay.resizable(width=False, height=False)
    rdisplay.iconbitmap('C:/gui/icon4.ico')

    rdisplay_top = Image.open("Images/receipt_temp.png")
    rephoto = ImageTk.PhotoImage(rdisplay_top)
    rdisplay.photo = rephoto  # solution for bug in `PhotoImage`
    receipt_toplogo = Label(rdisplay, image=rephoto, borderwidth="0")
    receipt_toplogo.place(x="37", y="15")

    rdisplay_down = Image.open("Images/Receipt_temp_ss_down.png")
    rephoto2 = ImageTk.PhotoImage(rdisplay_down)
    rdisplay.photo2 = rephoto2  # solution for bug in `PhotoImage`
    receipt_downlogo = Label(rdisplay, image=rephoto2, borderwidth="0")
    receipt_downlogo.place(x="37", y="450")

    gpay_logo = Image.open("Images/payment_image.png")
    gpay_logo = ImageTk.PhotoImage(gpay_logo)
    rdisplay.photo2 = gpay_logo  # solution for bug in `PhotoImage`
    rec_gpay_logo = Label(rdisplay, image=gpay_logo, borderwidth="0", bg="white")
    rec_gpay_logo.place(x="100", y="225")

    emailsymbol = Image.open("Images/mail_button.png")
    emailsymbol = ImageTk.PhotoImage(emailsymbol)
    rdisplay.photo = emailsymbol  # solution for bug in `PhotoImage`
    email_button = Button(rdisplay, image=emailsymbol, bg="white", bd="0",activebackground='blue',command=printrec)
    email_button.place(x="350", y="580")

    printsymbol = Image.open("Images/print_button_size.png")
    printsymbol = ImageTk.PhotoImage(printsymbol)
    rdisplay.photo = printsymbol  # solution for bug in `PhotoImage`
    print_button = Button(rdisplay, image=printsymbol, bg="white", bd="0",activebackground='blue',command=priss)
    print_button.place(x="550", y="580")

    rec_amt = Label(rdisplay, text="Amount : ", font="lucida 8 bold", bg="white", fg="black")
    rec_amt.place(x="100", y="400")

    rec_amt = Label(rdisplay, text="Amount : ", font="lucida 11 bold", bg="white", fg="black")
    rec_amt.place(x="750", y="410")

    rec_id=Label(rdisplay,text="Rec_ID : ",font="lucida 13 bold",bg="white",fg="black")
    rec_id.place(x="300",y="150")

    rec_name = Label(rdisplay, text="Name : ", font="lucida 11 bold ", bg="white", fg="black")
    rec_name.place(x="300", y="205")

    rec_age = Label(rdisplay, text="Age : ", font="lucida 11 bold", bg="white", fg="black")
    rec_age.place(x="300", y="255")

    rec_gender = Label(rdisplay, text="Gender : ", font="lucida 11 bold", bg="white", fg="black")
    rec_gender.place(x="420", y="255")

    rec_phone = Label(rdisplay, text="Mobile no : ", font="lucida 11 bold", bg="white", fg="black")
    rec_phone.place(x="300", y="305")

    rec_date = Label(rdisplay, text="Date : ", font="lucida 11 bold", bg="white", fg="black")
    rec_date.place(x="300", y="350")

    rec_refdr = Label(rdisplay, text="Ref.By Dr:  ", font="lucida 11 bold", bg="white", fg="black")
    rec_refdr.place(x="500", y="350")



    rec_test = Label(rdisplay, text="Test : ", font="lucida 11 bold", bg="white", fg="black")
    rec_test.place(x="300", y="395")



    # display name on receipt from db

    conn = sqlite3.connect('Labdb.db')
    cur = conn.cursor()
    rvalue = cur.execute("SELECT * FROM Receipt WHERE REC_ID = (SELECT max (REC_ID) FROM Receipt) ")
    detaillist = rvalue.fetchall()

    for i in detaillist:
        rec_id = Label(rdisplay, text=str(i[0]), font="lucida 14 bold", bg="white", fg="royalblue4")
        rec_id.place(x="390", y="150")

        dis_name = Label(rdisplay,text=str(i[1]),font="lucida 11 ",bg="white",fg="black")
        dis_name.place(x="370",y="205")

        dis_age = Label(rdisplay,text=str(i[2]),font="lucida 11 ",bg="white",fg="black")
        dis_age.place(x="360", y="255")

        dis_gender = Label(rdisplay,text=str(i[3]), font="lucida 11 ", bg="white", fg="black")
        dis_gender.place(x="510", y="255")

        dis_phone = Label(rdisplay, text=str(i[4]), font="lucida 11 ", bg="white", fg="black")
        dis_phone.place(x="410", y="305")

        dis_test = Label(rdisplay,text=str(i[6]), font="lucida 11 ", bg="white", fg="black")
        dis_test.place(x="360", y="395")

        dis_doc = Label(rdisplay, text=str(i[7]), font="lucida 11 ", bg="white", fg="black")
        dis_doc.place(x="600", y="350")

        rec_amt = Label(rdisplay,text=str(i[8])+"/- Rs", font="lucida 11 bold", bg="white", fg="black")
        rec_amt.place(x="845", y="410")
        rec_amt2 = Label(rdisplay,text=str(i[8])+"/- Rs", font="lucida 8 bold", bg="white", fg="black")
        rec_amt2.place(x="165", y="400")

        dis_date = Label(rdisplay,text=str(i[9]), font="lucida 11 ", bg="white", fg="black")
        dis_date.place(x="360", y="350")

        rec_time = Label(rdisplay,text=str("Time: "+i[10]), font="lucida 9 bold", bg="white", fg="black")
        rec_time.place(x="820", y="120")

        cur.close()
        conn.close()

    rdisplay.mainloop()


def priss():
    path = "Receipt_i.png"
    titles =pygetwindow.getAllTitles()

    # x1, y1 = width, height = pygetwindow.getWindowsWithTitle('Patholab')
    window = pygetwindow.getWindowsWithTitle('RECEIPT')[0]
    x1 = window.left+10
    y1 = window.top+50
    height = window.height-110
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
    filename = "Receipt_i.png"
    image = Image.open(filename)

    if image.mode == "RGBA":
        image = image.convert("RGB")
    output = "Receipt.pdf"
    image.save(output, "PDF", resolution=100.0)
    printreceipt()

def printreceipt():
    webbrowser.open_new(r'Receipt.pdf')
def showmailmessage():
    messagebox.showinfo("Message", "Mail sent successfully!")

def editReceipt():
    global select_rec_entry, edrecwin, select_rec_id
    edrecwin = Toplevel()
    edrecwin.configure(bg="white")
    window_width, window_height = 570,360
    screen_width = edrecwin.winfo_screenwidth()
    screen_height = edrecwin.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    edrecwin.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    reditselectionimg = Image.open("Images/backnew_3.png")
    rebg = ImageTk.PhotoImage(reditselectionimg)
    edrecwin.photo = rebg  # solution for bug in `PhotoImage`
    receipt_editlogo = Label(edrecwin, image=rebg, borderwidth="0")
    receipt_editlogo.place(x="0", y="0")

    select_rec_id = Label(edrecwin,text="Rec_Id : ",bg="white",font="lucida 12 bold")
    select_rec_id.place(x="170",y="95")
    select_rec_entry = Entry(edrecwin,font="lucida 13 bold",width="14",bg="grey93",bd="3")
    select_rec_entry.place(x="270",y="95")

    showreceiptbtn = Image.open("Images/showReceipt.png")
    showreceiptbtn = ImageTk.PhotoImage(showreceiptbtn)
    edrecwin.photo = showreceiptbtn  # solution for bug in `PhotoImage`
    showrecbtn = Button(edrecwin, image=showreceiptbtn, bg="white", bd="0", activebackground='blue',command=showReceipt)
    showrecbtn.place(x="190", y="160")

    editrecimg = Image.open("Images/editReceipt.png")
    editrecimg = ImageTk.PhotoImage(editrecimg)
    edrecwin.photo = editrecimg  # solution for bug in `PhotoImage`
    editrecbtn = Button(edrecwin, image=editrecimg, bg="white", bd="0", activebackground='blue',command=recUpdate)
    editrecbtn.place(x="191", y="220")

    edrecwin.mainloop()

def showReceipt():
    global rdisplay,recid
    recid = int(select_rec_entry.get())
    rdisplay = Toplevel()

    window_width, window_height = 1000, 630
    screen_width = rdisplay.winfo_screenwidth()
    screen_height = rdisplay.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    rdisplay.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    rdisplay.title("RECEIPT")
    rdisplay.configure(bg="white")
    rdisplay.resizable(width=False, height=False)
    rdisplay.iconbitmap('C:/gui/icon4.ico')

    rdisplay_top = Image.open("Images/receipt_temp.png")
    rephoto = ImageTk.PhotoImage(rdisplay_top)
    rdisplay.photo = rephoto  # solution for bug in `PhotoImage`
    receipt_toplogo = Label(rdisplay, image=rephoto, borderwidth="0")
    receipt_toplogo.place(x="37", y="15")

    rdisplay_down = Image.open("Images/Receipt_temp_ss_down.png")
    rephoto2 = ImageTk.PhotoImage(rdisplay_down)
    rdisplay.photo2 = rephoto2  # solution for bug in `PhotoImage`
    receipt_downlogo = Label(rdisplay, image=rephoto2, borderwidth="0")
    receipt_downlogo.place(x="37", y="450")

    gpay_logo = Image.open("Images/payment_image.png")
    gpay_logo = ImageTk.PhotoImage(gpay_logo)
    rdisplay.photo2 = gpay_logo  # solution for bug in `PhotoImage`
    rec_gpay_logo = Label(rdisplay, image=gpay_logo, borderwidth="0", bg="white")
    rec_gpay_logo.place(x="100", y="225")

    emailsymbol = Image.open("Images/mail_button.png")
    emailsymbol = ImageTk.PhotoImage(emailsymbol)
    rdisplay.photo = emailsymbol  # solution for bug in `PhotoImage`
    email_button = Button(rdisplay, image=emailsymbol, bg="white", bd="0", activebackground='blue', command=eprintrec)
    email_button.place(x="350", y="580")

    printsymbol = Image.open("Images/print_button_size.png")
    printsymbol = ImageTk.PhotoImage(printsymbol)
    rdisplay.photo = printsymbol  # solution for bug in `PhotoImage`
    print_button = Button(rdisplay, image=printsymbol, bg="white", bd="0", activebackground='blue',command=priss)
    print_button.place(x="550", y="580")

    rec_amt = Label(rdisplay, text="Amount : ", font="lucida 8 bold", bg="white", fg="black")
    rec_amt.place(x="100", y="400")

    rec_amt = Label(rdisplay, text="Amount : ", font="lucida 11 bold", bg="white", fg="black")
    rec_amt.place(x="750", y="410")

    rec_id = Label(rdisplay, text="Rec_ID : ", font="lucida 13 bold", bg="white", fg="black")
    rec_id.place(x="300", y="150")

    rec_name = Label(rdisplay, text="Name : ", font="lucida 11 bold ", bg="white", fg="black")
    rec_name.place(x="300", y="205")

    rec_age = Label(rdisplay, text="Age : ", font="lucida 11 bold", bg="white", fg="black")
    rec_age.place(x="300", y="255")

    rec_gender = Label(rdisplay, text="Gender : ", font="lucida 11 bold", bg="white", fg="black")
    rec_gender.place(x="420", y="255")

    rec_phone = Label(rdisplay, text="Mobile no : ", font="lucida 11 bold", bg="white", fg="black")
    rec_phone.place(x="300", y="305")

    rec_date = Label(rdisplay, text="Date : ", font="lucida 11 bold", bg="white", fg="black")
    rec_date.place(x="300", y="350")

    rec_refdr = Label(rdisplay, text="Ref.By Dr:  ", font="lucida 11 bold", bg="white", fg="black")
    rec_refdr.place(x="500", y="350")

    rec_test = Label(rdisplay, text="Test : ", font="lucida 11 bold", bg="white", fg="black")
    rec_test.place(x="300", y="395")

    # display name on receipt from db

    conn = sqlite3.connect('Labdb.db')
    cur = conn.cursor()
    rvalue = cur.execute(f"SELECT * FROM Receipt WHERE REC_ID = {recid}")
    detaillist = rvalue.fetchall()

    for i in detaillist:
        rec_id = Label(rdisplay, text=str(i[0]), font="lucida 14 bold", bg="white", fg="royalblue4")
        rec_id.place(x="390", y="150")

        dis_name = Label(rdisplay, text=str(i[1]), font="lucida 11 ", bg="white", fg="black")
        dis_name.place(x="370", y="205")

        dis_age = Label(rdisplay, text=str(i[2]), font="lucida 11 ", bg="white", fg="black")
        dis_age.place(x="360", y="255")

        dis_gender = Label(rdisplay, text=str(i[3]), font="lucida 11 ", bg="white", fg="black")
        dis_gender.place(x="510", y="255")

        dis_phone = Label(rdisplay, text=str(i[4]), font="lucida 11 ", bg="white", fg="black")
        dis_phone.place(x="410", y="305")

        dis_test = Label(rdisplay, text=str(i[6]), font="lucida 11 ", bg="white", fg="black")
        dis_test.place(x="360", y="395")

        dis_doc = Label(rdisplay, text=str(i[7]), font="lucida 11 ", bg="white", fg="black")
        dis_doc.place(x="600", y="350")

        rec_amt = Label(rdisplay, text=str(i[8]) + "/- Rs", font="lucida 11 bold", bg="white", fg="black")
        rec_amt.place(x="845", y="410")
        rec_amt2 = Label(rdisplay, text=str(i[8]) + "/- Rs", font="lucida 8 bold", bg="white", fg="black")
        rec_amt2.place(x="165", y="400")

        dis_date = Label(rdisplay, text=str(i[9]), font="lucida 11 ", bg="white", fg="black")
        dis_date.place(x="360", y="350")

        rec_time = Label(rdisplay, text=str("Time: " + i[10]), font="lucida 9 bold", bg="white", fg="black")
        rec_time.place(x="820", y="120")

        cur.close()
        conn.close()

    rdisplay.mainloop()

def recUpdate():
    global recname_uentry, recage_uentry, uvar, recphone_uentry, recrefdr_uentry, uclick, recemail_uentry,rentry
    rentry = Toplevel()

    window_width, window_height = 1000, 570
    screen_width = rentry.winfo_screenwidth()
    screen_height = rentry.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    rentry.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    rentry.title("RECEIPT ENTRY")
    rentry.configure(bg="white")
    rentry.resizable(width=False, height=False)
    rentry.iconbitmap('C:/gui/icon4.ico')

    rentry_top = Image.open("Images/receipt_temp.png")
    rephoto = ImageTk.PhotoImage(rentry_top)
    rentry.photo = rephoto  # solution for bug in `PhotoImage`
    receipt_toplogo = Label(rentry, image=rephoto, borderwidth="0")
    receipt_toplogo.place(x="37", y="15")

    rentry_down = Image.open("Images/Receipt_temp_ss_down.png")
    rephoto2 = ImageTk.PhotoImage(rentry_down)
    rentry.photo2 = rephoto2  # solution for bug in `PhotoImage`
    receipt_downlogo = Label(rentry, image=rephoto2, borderwidth="0")
    receipt_downlogo.place(x="37", y="450")

    gpay_logo = Image.open("Images/payment_image.png")
    gpay_logo = ImageTk.PhotoImage(gpay_logo)
    rentry.photo2 = gpay_logo  # solution for bug in `PhotoImage`
    rec_gpay_logo = Label(rentry, image=gpay_logo, borderwidth="0", bg="white")
    rec_gpay_logo.place(x="100", y="230")

    rec_name = Label(rentry, text="Name : ", font="lucida 12 bold ", bg="white", fg="blue4")
    rec_name.place(x="300", y="150")
    recname_uentry = Entry(rentry, width="40", font="lucida 12", bd="3")
    recname_uentry.place(x="380", y="150")

    rec_age = Label(rentry, text="Age : ", font="lucida 12 bold", bg="white", fg="blue4")
    rec_age.place(x="300", y="200")
    recage_uentry = Entry(rentry, width="5", font="lucida 12", bd="3")
    recage_uentry.place(x="370", y="200")

    uvar = StringVar()
    rec_gender = Label(rentry, text="Gender : ", font="lucida 12 bold", bg="white", fg="blue4")
    rec_gender.place(x="470", y="200")

    msymbol = Image.open("Images/male.png")
    msymbol = ImageTk.PhotoImage(msymbol)
    rentry.photo = msymbol  # solution for bug in `PhotoImage`
    mgender_radio = Radiobutton(rentry, image=msymbol, variable=uvar, bg="white", fg="blue", font="2", value="MALE")
    mgender_radio.place(x="560", y="198")

    fsymbol = Image.open("Images/femenine.png")
    fsymbol = ImageTk.PhotoImage(fsymbol)
    rentry.photo = fsymbol  # solution for bug in `PhotoImage`
    fgender_radio = Radiobutton(rentry, image=fsymbol, variable=uvar, bg="white", fg="blue", font="2", value="FEMALE")
    fgender_radio.place(x="630", y="198")

    rec_phone = Label(rentry, text="Mobile no : ", font="lucida 12 bold", bg="white", fg="blue4")
    rec_phone.place(x="300", y="250")
    recphone_uentry = Entry(rentry, width="15", font="lucida 12", bd="3")
    recphone_uentry.place(x="420", y="250")

    rec_refdr = Label(rentry, text="Ref.By Dr : ", font="lucida 12 bold", bg="white", fg="blue4")
    rec_refdr.place(x="300", y="300")
    recrefdr_uentry = Entry(rentry, width="15", font="lucida 12", bd="3")
    recrefdr_uentry.place(x="420", y="300")

    rec_test = Label(rentry, text="Test : ", font="lucida 12 bold", bg="white", fg="blue4")
    rec_test.place(x="300", y="350")
    list1 = ['Complete Blood Count', 'Prothrobin Time', 'Basic Metabolic Panel', 'Comprehensive Metabolic Panel','Lipid Panel', 'Liver Panel', 'Thyroid Stimulating Hormone', 'Hemoglobin A1C', 'Urinalysis', 'Cultures']
    uclick = StringVar()
    uclick.set("Select Test")
    test_dropdown = OptionMenu(rentry, uclick, *list1)
    test_dropdown.config(bg="blue4", fg="white", width="25", activebackground="dodger blue", activeforeground="black")
    test_dropdown.place(x="370", y="345")

    rec_email = Label(rentry, text="e-mail id : ", font="lucida 12 bold", bg="white", fg="blue4")
    rec_email.place(x="300", y="400")
    recemail_uentry = Entry(rentry, width="30", font="lucida 12", bd="3")
    recemail_uentry.place(x="420", y="400")

    submitsymbol = Image.open("Images/save_changes_button.png")
    submitsymbol = ImageTk.PhotoImage(submitsymbol)
    rentry.photo3 = submitsymbol
    submit_receipt = Button(rentry, image=submitsymbol, bg="white", bd="0", activebackground='green', command=receiptUpdatedb)
    submit_receipt.place(x="775", y="410")

    # insert the values in the entry box
    recid = int(select_rec_entry.get())
    conn = sqlite3.connect('Labdb.db')
    cur = conn.cursor()
    rvalue = cur.execute(f"SELECT * FROM Receipt WHERE REC_ID = {recid}")
    detaillist = rvalue.fetchall()
    for i in detaillist:
        recname_uentry.insert(0, i[1])
        recage_uentry.insert(0, i[2])
        uvar.set(i[3])
        recphone_uentry.insert(0, i[4])
        recemail_uentry.insert(0, i[5])
        uclick.set(i[6])
        recrefdr_uentry.insert(0, i[7])
    cur.close()
    conn.close()

    rentry.mainloop()

def receiptUpdatedb():
    updatename = recname_uentry.get()
    updateage = recage_uentry.get()
    updategender = uvar.get()
    updatephone = recphone_uentry.get()
    updaterefdr = recrefdr_uentry.get()
    updatetest = uclick.get()
    updatemail = recemail_uentry.get()
    recid =  select_rec_entry.get()

    if (updatetest == "Complete Blood Count"):
        newamt=700
    elif(updatetest=="Prothrobin Time"):
        newamt=700
    elif(updatetest=="Basic Metabolic Panel"):
        newamt=800
    elif(updatetest=="Comprehensive Metabolic Panel"):
        newamt=900
    elif(updatetest=="Lipid Panel"):
        newamt=500
    elif(updatetest=="Liver Panel"):
        newamt=950
    elif(updatetest=="Thyroid Stimulating Hormone"):
        newamt=750
    elif(updatetest=="Hemoglobin A1C"):
        newamt=1200
    elif(updatetest=="Urinalysis"):
        newamt=600
    elif(updatetest=="Cultures"):
        newamt=1100
    else:
        newamt=500


    conn = sqlite3.connect('Labdb.db')
    cur = conn.cursor()
    cur.execute(f"""UPDATE Receipt set
                NAME = '{updatename}',
                AGE = {updateage},
                GENDER = '{updategender}',
                PHONE_NO = {updatephone},
                REF_DR = '{updaterefdr}',
                TEST = '{updatetest}',
                EMAIL_ID = '{updatemail}',
                AMOUNT = {newamt}
                WHERE REC_ID = {recid}
                
                """)
    cur.close()
    conn.commit()
    showupdatemessage()
    conn.close()

def showupdatemessage():
    messagebox.showinfo("Message", "Receipt updated successfully!")
    rentry.destroy()
    showReceipt()

def takeTest():
    tktest = Toplevel()

    window_width, window_height = 850, 750
    screen_width = tktest.winfo_screenwidth()
    screen_height = tktest.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    tktest.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    tktest.title("REPORT ENTRY")
    tktest.configure(bg="white")
    tktest.resizable(width=False, height=False)
    tktest.iconbitmap('C:/gui/icon4.ico')

    taketest_temp = Image.open("Images/taketest_template.png")
    tktesttemp = ImageTk.PhotoImage(taketest_temp)
    tktest.photo = tktesttemp  # solution for bug in `PhotoImage`
    receipt_toplogo = Label(tktest, image=tktesttemp, borderwidth="0")
    receipt_toplogo.place(x="-3", y="0")

    splashframe = Frame(tktest, highlightbackground="blue4", highlightthickness=3, width=490, height=625, bd="0",bg="white")
    splashframe.place(x="350", y="110")

    tt_recid = Label(tktest, text="REC_ID : ", font="lucida 12 bold", bg='white', fg="blue4")
    tt_recid.place(x="350", y="25")
    tt_recid_entry = Entry(tktest, width="15", font="lucida 12 bold", bd="5",bg="grey94")
    tt_recid_entry.place(x="440", y="22")

    tt_testentry = Label(tktest, text="TEST ENTRY ", font="lucida 11 bold", bg='white',fg="blue3")
    tt_testentry.place(x="520", y="80")

    tt_hemoglobin = Label(tktest, text="HEMOGLOBIN                            : ", font="lucida 10 bold", bg='white', fg="blue4")
    tt_hemoglobin.place(x="370", y="120")
    tt_hemo_entry = Entry(tktest, width="10", font="lucida 10 bold", bd="3", bg="grey94")
    tt_hemo_entry.place(x="700", y="120")

    tt_RBC = Label(tktest, text="RBC                                           : ", font="lucida 10 bold", bg='white', fg="blue4")
    tt_RBC.place(x="370", y="170")
    tt_rbc_entry = Entry(tktest, width="10", font="lucida 10 bold", bd="3", bg="grey94")
    tt_rbc_entry.place(x="700", y="170")

    tt_PCV = Label(tktest, text="PCV                                            : ", font="lucida 10 bold", bg='white', fg="blue4")
    tt_PCV.place(x="370", y="220")
    tt_pcv_entry = Entry(tktest, width="10", font="lucida 10 bold", bd="3", bg="grey94")
    tt_pcv_entry.place(x="700", y="220")

    tt_MCV = Label(tktest, text="MCV_FL                                      : ", font="lucida 10 bold", bg='white', fg="blue4")
    tt_MCV.place(x="370", y="270")
    tt_mcv_entry = Entry(tktest, width="10", font="lucida 10 bold", bd="3", bg="grey94")
    tt_mcv_entry.place(x="700", y="270")

    tt_MCH = Label(tktest, text="MCH                                           : ", font="lucida 10 bold", bg='white', fg="blue4")
    tt_MCH.place(x="370", y="320")
    tt_mch_entry = Entry(tktest, width="10", font="lucida 10 bold", bd="3", bg="grey94")
    tt_mch_entry.place(x="700", y="320")

    tt_WBC = Label(tktest, text="TOTAL WBC                               : ", font="lucida 10 bold", bg='white', fg="blue4")
    tt_WBC.place(x="370", y="370")
    tt_wbc_entry = Entry(tktest, width="10", font="lucida 10 bold", bd="3", bg="grey94")
    tt_wbc_entry.place(x="700", y="370")

    tt_NEURO = Label(tktest, text="NEUROPHILES                           : ", font="lucida 10 bold", bg='white', fg="blue4")
    tt_NEURO.place(x="370", y="420")
    tt_neuro_entry = Entry(tktest, width="10", font="lucida 10 bold", bd="3", bg="grey94")
    tt_neuro_entry.place(x="700", y="420")


    tt_EOSINO = Label(tktest, text="EOSINOPHILES                          : ", font="lucida 10 bold", bg='white', fg="blue4")
    tt_EOSINO.place(x="370", y="470")
    tt_eosino_entry = Entry(tktest, width="10", font="lucida 10 bold", bd="3", bg="grey94")
    tt_eosino_entry.place(x="700", y="470")

    tt_BASO = Label(tktest, text="BASOPHILS                                : ", font="lucida 10 bold", bg='white', fg="blue4")
    tt_BASO.place(x="370", y="520")
    tt_baso_entry = Entry(tktest, width="10", font="lucida 10 bold", bd="3", bg="grey94")
    tt_baso_entry.place(x="700", y="520")

    tt_LYMPHO = Label(tktest, text="LYMPHOCYTES                          : ", font="lucida 10 bold", bg='white', fg="blue4")
    tt_LYMPHO.place(x="370", y="570")
    tt_lympho_entry = Entry(tktest, width="10", font="lucida 10 bold", bd="3", bg="grey94")
    tt_lympho_entry.place(x="700", y="570")

    tt_MANO = Label(tktest, text="MANOCYTES                              : ", font="lucida 10 bold", bg='white', fg="blue4")
    tt_MANO.place(x="370", y="620")
    tt_mano_entry = Entry(tktest, width="10", font="lucida 10 bold", bd="3", bg="grey94")
    tt_mano_entry.place(x="700", y="620")

    tt_PLATELET = Label(tktest, text="PLATELET                                  : ", font="lucida 10 bold", bg='white', fg="blue4")
    tt_PLATELET.place(x="370", y="670")
    tt_platelet_entry = Entry(tktest, width="10", font="lucida 10 bold", bd="3", bg="grey94")
    tt_platelet_entry.place(x="700", y="670")


    tktest.mainloop()















def age_pin():
    global entry_age, entry_pin, agpin
    agpin = Tk()

    window_width, window_height = 410, 170

    screen_width = agpin.winfo_screenwidth()
    screen_height = agpin.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    agpin.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    agpin.title("Pincode and age")
    # agpin.wm_attributes("-transparentcolor", "white")

    label_age = Label(agpin, text="Enter Age: ", font="5")
    label_age.place(x=10, y=10)
    label_pin = Label(agpin, text="Enter Pincode: ", font="5")
    label_pin.place(x=10, y=60)

    entry_age = Entry(agpin, font="5")
    entry_age.place(x=170, y=10)
    entry_pin = Entry(agpin, font="5")
    entry_pin.place(x=170, y=60)


    button_booking = Button(agpin, text="Search", bg="green3", fg="black", height="1", width="30", command=slotbook)
    button_booking.place(x=90, y=120)





    agpin.mainloop()

def loading():
    global load
    load = Tk()
    load.title("")
    load.configure(bg="white")
    window_width, window_height = 400, 120

    screen_width = load.winfo_screenwidth()
    screen_height = load.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    load.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    Label(load, text="No vaccine slots are available at this moment\nPlease try again after sometime.", bg="white",
          fg="black").pack(pady=10)
    Button(load, text="OK", height="1", width="5", bg="white", fg="black", borderwidth="5", command=load.destroy).pack(
        pady=14)
    load.mainloop()

def back():
    slot.destroy()
    age_pin()


def open_site():
    webbrowser.open("https://selfregistration.cowin.gov.in/")

def slotbook():
    age = int(entry_age.get())
    pincodes = [f"{entry_pin.get()}"]  # 680570
    agpin.destroy()
    num_days = 2
    print(age)
    print(pincodes)
    print_flag = 'Y'

    print("Starting search for Covid vaccine slots!")
    actual = datetime.today()
    list_format = [actual + timedelta(days=i) for i in range(num_days)]
    actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]
    global slot
    slot = Tk()

    window_width, window_height = 650, 850

    screen_width = slot.winfo_screenwidth()
    screen_height = slot.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    slot.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    slot.configure(bg="white")
    slot.title("Vaccine slot")

    Label(slot, text=f"VACCINE SLOTS ", fg="blue", bg="white", font="5").pack(pady="2")
    Button(slot, text="Book Now", bg="green", fg="white", borderwidth="2", height="1", width="13",command=open_site).place(x=512, y=800)
    Button(slot, text="Back", bg="blue", fg="white", borderwidth="2", height="1", width="13", command=back).place(x=25,y=800)

    while True:
        counter = 0

        for pincode in pincodes:
            for given_date in actual_dates:

                URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(
                    pincode, given_date)
                header = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

                result = requests.get(URL, headers=header)

                if result.ok:
                    response_json = result.json()
                    if response_json["centers"]:
                        if (print_flag.lower() == 'y'):
                            for center in response_json["centers"]:
                                for session in center["sessions"]:
                                    if (session["min_age_limit"] <= age and session["available_capacity"] > 0):
                                        tk_pincode = 'Pincode : ' + pincode

                                        tk_data = ("Available on: {}".format(given_date))

                                        tk_centername = center["name"]

                                        tk_blockname = center["block_name"]

                                        tk_price = "Type : " + center["fee_type"]

                                        tk_available = (" Availablity : " + str(session["available_capacity"]))

                                        if (session["vaccine"] != ''):
                                            tk_vacctype = " Vaccine name : " + session["vaccine"]

                                            label_show = Label(slot,
                                                               text=tk_pincode + "\n" + tk_data + "\n" + tk_centername + "\n" + tk_blockname + "\n" + tk_price + "\n" + tk_available + "\n" + tk_vacctype + "\n",bg="white", fg="black")
                                            label_show.pack()

                                        counter = counter + 1

                else:
                    print("No Response!")

        if counter:
            print("Search complete!")
            break
        else:
            mixer.init()
            mixer.music.load('Images/beep.wav')
            mixer.music.play()
            slot.destroy()
            loading()
            slot.destroy()


        dt = datetime.now() + timedelta(minutes=3)
        slot.mainloop()
        while datetime.now() < dt:
            time.sleep(0)

# VCARD

def vcard_entry():
    global ventry
    ventry = Toplevel()
    ventry.iconbitmap("Images/icon4.ico")
    ventry.config(bg="white")
    window_width, window_height = 700, 400

    screen_width = ventry.winfo_screenwidth()
    screen_height = ventry.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    ventry.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    ventry.title("V-CARD")


    global v_name_entry,v_age_entry,v_aadhar_entry,v_phone_entry,click,v_vaccinator_entry,image_name
    rentry_top = Image.open("Images/vcard_bg.png")
    rephoto = ImageTk.PhotoImage(rentry_top)
    ventry.photo = rephoto  # solution for bug in `PhotoImage`
    receipt_toplogo = Label(ventry, image=rephoto, borderwidth="0")
    receipt_toplogo.place(x="25", y="10")


    choose_size = Image.open("Images/Choose_file_btn.png")
    choose_resized = choose_size.resize((100, 30), Image.ANTIALIAS)
    choose_image = ImageTk.PhotoImage(choose_resized)
    Label(image=choose_image)
    button_choose = Button(ventry, image=choose_image, borderwidth="0", activebackground='blue', command=browseImage)
    button_choose.place(x=87, y=195)

    generate_size = Image.open("Images/generateid.png")
    generate_resized = generate_size.resize((130, 40), Image.ANTIALIAS)
    generate_image = ImageTk.PhotoImage(generate_resized)
    Label(image=generate_image)
    button_generate = Button(ventry, image=generate_image, borderwidth="0", activebackground='blue', command=vcard_db)
    button_generate.place(x=280, y=310)

    v_name = Label(ventry, text="NAME                :  ", font="lucida 9 bold", bg= 'white', fg="blue4")
    v_name.place(x="260", y="100")
    v_name_entry = Entry(ventry, width="35", font="lucida 8 bold", bd="3")
    v_name_entry.place(x="380", y="100")

    v_age = Label(ventry, text="AGE                   :  ", font="lucida 9 bold", bg='white', fg="blue4")
    v_age.place(x="260", y="130")
    v_age_entry = Entry(ventry, width="7", font="lucida 8 bold", bd="3")
    v_age_entry.place(x="380", y="130")

    v_aadhar = Label(ventry, text="AADHAAR NO   : 682981917161 ", font="lucida 9 bold", bg='white', fg="blue4")
    v_aadhar.place(x="260", y="160")
    v_aadhar_entry = Entry(ventry, width="15", font="lucida 8 bold", bd="3")
    v_aadhar_entry.place(x="380", y="160")

    v_vaccine = Label(ventry, text="VACCINE           : COVISHIELD ", font="lucida 9 bold", bg='white', fg="blue4")
    v_vaccine.place(x="260", y="190")

    vaccine_names = ['COVISHIELD','COVAXIN','PFIZER','SPUTNIK V']
    click = StringVar()
    click.set("Select Test")
    test_dropdown = OptionMenu(ventry, click, *vaccine_names)
    test_dropdown.config(bg="blue4", fg="white",height="0", width="15",font='lucida 5 bold', activebackground="dodger blue", activeforeground="black")
    test_dropdown.place(x="379", y="187")

    v_phone = Label(ventry, text="PHONE NO       :", font="lucida 9 bold", bg='white', fg="blue4")
    v_phone.place(x="260", y="220")
    v_phone_entry = Entry(ventry, width="15", font="lucida 8 bold", bd="3")
    v_phone_entry.place(x="380", y="220")

    v_vaccinator = Label(ventry, text="VACCINATOR'S NAME  :", font="lucida 9 bold", bg='white', fg="blue4")
    v_vaccinator.place(x="260", y="250")
    v_vaccinator_entry = Entry(ventry, width="25", font="lucida 8 bold", bd="3")
    v_vaccinator_entry.place(x="440", y="250")

    global label_file_explorer
    label_file_explorer = Label(ventry,
                                text="",font="lucida 5 bold",
                                width=23, height=3,
                                fg="black",bg="white",)
    label_file_explorer.place(x="77",y="230")

    ventry.mainloop()


def browseImage():
    global filename,image_name
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Image files",
                                                      "*.png*"),
                                                     ("all files",
                                                      "*.*")))

    # Change label contentsx
    imagelocation_count = filename.rfind("/")
    global image_name,label_file_explorer
    image_name = filename[(imagelocation_count + 1):]
    label_file_explorer.configure(text=image_name)



def vcard_db():
    name = v_name_entry.get()
    age = v_age_entry.get()
    aadhar = v_aadhar_entry.get()
    phone = v_phone_entry.get()
    vaccine = click.get()
    vaccinator = v_vaccinator_entry.get()



    try:

        conn = sqlite3.connect('Labdb.db')
        cur = conn.cursor()
        cur.execute(f"INSERT INTO VCARD VALUES((SELECT max (VID)+1 from VCARD),'{name}',{age},{aadhar},'{vaccine}',{phone},'{vaccinator}','{image_name}',STRFTIME('%d/%m/%Y'))")  # get method gets values from the variable
        cur.close()
        conn.commit()
        conn.close()
        messagebox.showinfo("Message", "Card created successfully!")
        generateid()

    except Exception as e:
        messagebox.showerror("Error", "Some Error Occured \n\n ⭕ Entry field should not be Empty.\n ⭕ Please select the profile image.")
        print(e)


def cardss():
    path = "card_i.png"
    titles =pygetwindow.getAllTitles()

    # x1, y1 = width, height = pygetwindow.getWindowsWithTitle('Patholab')
    window = pygetwindow.getWindowsWithTitle('V-CARD')[0]
    x1 = window.left+30
    y1 = window.top+43
    height = window.height-123
    width = window.width-60
    x2 = x1 + width
    y2 = y1 + height

    pyautogui.screenshot(path)

    im = Image.open(path)
    im = im.crop((x1,y1,x2,y2))
    im.save(path)
    # im.show(path)
    cardtopdf()

def cardtopdf():
    filename = "card_i.png"
    image = Image.open(filename)

    if image.mode == "RGBA":
        image = image.convert("RGB")
    output = "Vcard.pdf"
    image.save(output, "PDF", resolution=100.0)
    webbrowser.open_new(r'Vcard.pdf')



def generateid():
    try:
        ventry.destroy()
        global myid
        myid = Toplevel()
        myid.iconbitmap("Images/icon4.ico")
        myid.config(bg="white")
        window_width, window_height = 700, 450

        screen_width = myid.winfo_screenwidth()
        screen_height = myid.winfo_screenheight()

        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        myid.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        myid.title("V-CARD")

        rentry_top = Image.open("Images/vcard_bg.png")
        rephoto = ImageTk.PhotoImage(rentry_top)
        myid.photo = rephoto  # solution for bug in `PhotoImage`
        receipt_toplogo = Label(myid, image=rephoto, borderwidth="0")
        receipt_toplogo.place(x="25", y="10")

        conentry_top = Image.open(f"{filename}")
        # conentry_top = Image.open(f"Images/Harikrishnan.png")
        imagesize = conentry_top.resize((136, 176), Image.ANTIALIAS)
        entrytop = ImageTk.PhotoImage(imagesize)
        myid.photo = entrytop  # solution for bug in `PhotoImage`
        receipt = Label(myid, image=entrytop, borderwidth="0")
        receipt.place(x="70", y="91.5")
        conn = sqlite3.connect('Labdb.db')
        cur = conn.cursor()
        vvalue = cur.execute("SELECT * FROM VCARD WHERE VID = (SELECT max (VID) FROM VCARD) ")
        carddetails = vvalue.fetchall()
        for i in carddetails:
            vid = str(i[0])
            v_name = str(i[1])
            v_age = str(i[2])
            v_aadhar = str(i[3])
            v_vaccine = str(i[4])
            v_phone = str(i[5])
            v_vaccinator = str(i[6])
            v_date = str(i[8])

            v_id = Label(myid, text=f"VID : {vid}", font="lucida 13 bold", bg='white', fg="black")
            v_id.place(x="515", y="50")

            v_date = Label(myid, text=f"DATE : {v_date}", font="lucida 9 bold", bg='white',fg="blue4")
            v_date.place(x="515", y="30")

            v_name = Label(myid, text=f"NAME                : {v_name} ", font="lucida 9 bold", bg='white', fg="blue4")
            v_name.place(x="260", y="100")


            v_age = Label(myid, text=f"AGE                   : {v_age}  ", font="lucida 9 bold", bg='white', fg="blue4")
            v_age.place(x="260", y="130")


            v_aadhar = Label(myid, text=f"AADHAAR NO   : {v_aadhar} ", font="lucida 9 bold", bg='white', fg="blue4")
            v_aadhar.place(x="260", y="160")


            v_vaccine = Label(myid, text=f"VACCINE           : {v_vaccine} ", font="lucida 9 bold", bg='white', fg="blue4")
            v_vaccine.place(x="260", y="190")


            v_phone = Label(myid, text=f"PHONE NO       : {v_phone}", font="lucida 9 bold", bg='white', fg="blue4")
            v_phone.place(x="260", y="220")


            v_vaccinator = Label(myid, text=f"VACCINATOR'S NAME  : {v_vaccinator}", font="lucida 9 bold", bg='white', fg="blue4")
            v_vaccinator.place(x="260", y="250")


            signature = Image.open("Images/signature.png")
            labsignature = ImageTk.PhotoImage(signature)
            myid.photo = labsignature  # solution for bug in `PhotoImage`
            labsignature = Label(myid, image=labsignature, borderwidth="0")
            labsignature.place(x="400", y="290")

            v_vaccinator = Label(myid, text="Pathologist", font="lucida 7 bold", bg='white',fg="blue4")
            v_vaccinator.place(x="420", y="335")

            printcard = Image.open("Images/print_button_size.png")
            printcard = ImageTk.PhotoImage(printcard)
            myid.photo3 = printcard
            printcard = Button(myid, image=printcard, bg="white", bd="0", activebackground='green',command=cardss)
            printcard.place(x="300", y="400")

        myid.mainloop()




    except Exception as e:
        messagebox.showerror("Error","Some Error Occured \n\n ⭕ Entry field should not be Empty.\n ⭕ Please select the profile image.")
        print(e)
        myid.destroy()



# def displayid():
#     try:
#
#
#     except Exception as e:
#

# vcard_entry()
# generateid()
# receiptEntry()
# displayReceipt()


# homewindow()
takeTest()
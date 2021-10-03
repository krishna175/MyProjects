import cx_Oracle
from fpdf import FPDF
import webbrowser

# create FPDF object
# Layout ('P','L')
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150))
pdf = FPDF('P', 'mm',(210,297))

# Add a page
pdf.add_page()

# specify font
# fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., ('BU'))
pdf.set_font('helvetica', 'B', 8)
pdf.set_text_color(0,0,0)
# Add text
# w = width
# h = height
# txt = your text
# ln (0 False; 1 True - move cursor down to next line)

# border (0 False; 1 True - add border around cell)
# pdf.cell(20, 10, 'Hello World!', ln=True)
pdf.image('Images/bill_toptemplate.png',5,5,200,47)
pdf.image("Images/bill_nametemplate.png",20,55,80,80)
pdf.image("Images/bill_amounttemplate.png",17,135,85,65)
pdf.image("Images/bill_contacttemplate.png",115,60,75,37)
pdf.image("Images/bill_consuptiontemplate.png",113,103,75,50)
pdf.image("Images/bill_impmsgtemplate.png",114,155,72,35)
pdf.image("Images/bill_protocoltemplate.png",114,195,72,35)
pdf.image("Images/bill_cuttemplate.png",5,240,200,8)


name = "HARIKRISHNAN SATHYAN"
phone = 9820767941
pdf.text(30,79,'NAME          : ')
pdf.text(29.9,84,'PHONE NO  :')
pdf.text(30,89,'ADDRESS   :')
pdf.text(30,104,'PINCODE    :')
pdf.text(30,109,'EMAIL         :')
pdf.text(30,114,'AADHAR     :')
pdf.text(30,119,'CL in kW     :')

pdf.set_font('helvetica', 'B', 8)
pdf.set_text_color(0,0,0)
pdf.text(116,103,"YOUR CURRENT CONSUMPTION")

pdf.set_font('helvetica', 'B', 7)
pdf.text(120,114,"BILL NO                                  :")
pdf.text(120,120,"BILL DATE                             :")
pdf.text(120,126,"TYPE OF SUPPLY                 :")
pdf.text(120,132,"PRESENT READING             :")
pdf.text(120,138,"PREVIOUS READING           :")
pdf.text(120,144,"CONSUPTION (UNIT kWh)   :")

pdf.set_font('helvetica', 'B', 10)
pdf.text(46,209,"JOIN US ON")

pdf.image("Images/bill_fbtemplate.png",30,213,10,10,link="https://www.facebook.com/")
pdf.image("Images/bill_instatemplate.png",45,213,10,10,link="https://www.instagram.com/?hl=en")
pdf.image("Images/bill_youtubetemplate.png",60,213,10,10,link="https://www.youtube.com/")
pdf.image("Images/bill_linkedintemplate.png",75,213,10,10,link="https://in.linkedin.com/")


#Check slip
pdf.image("Images/bill_paysliptemplate.png",7,248,8,40)
pdf.image("Images/bill_barcodetemplate.png",20,264,100,10)
pdf.image("Images/bill_payslip2template.png",20,276,145,10)

pdf.set_font('helvetica','', 7)
pdf.text(20,250,"If paying by cheque, please remember:")
pdf.text(20,254,"- Cheque should be Account payee of local clearing and not post-dated")
pdf.text(20,258,"- Always attach payment slip. Do not staple         - Make cheque payable to Electrica Electricity Mumbai Ltd. A/C No.:152191709")
pdf.text(20,262,"- Mention A/c No. and respective amount on back of the cheque,when making multiple bill payments by single cheque")
pdf.set_font('helvetica','B', 7)
pdf.text(25,280,"BILL DATE : ")
pdf.text(96,280,"BILL AMOUNT : ")
pdf.text(25,284.5,"DUE DATE : ")
pdf.text(96,284.5,"AMOUNT AFTER DUE DATE : ")


#VALUES OF THE FIELDS

con = cx_Oracle.connect('system/12345@localhost:1521/xe')
cursor = con.cursor()
consumer_details = cursor.execute(f"""
                               SELECT CON_NAME,PHONE_NO,ADDRESS1,ADDRESS2,ADDRESS3,PIN_CODE,EMAILID,AADHAR,
                               SUPPLY_TYPE,REQUIREMENT FROM ADD_CONSUMER WHERE CON_ID=111116
                                """)
details_list = consumer_details.fetchall()
for con_values in details_list:
    emailid = con_values[6]
    encpt_emailid = emailid[0:3]+"******"+emailid[-10:]

    aadhar = str(con_values[7])
    encpt_aadhar = aadhar[0:3]+"******"+aadhar[-3:]

    pdf.set_font('helvetica','', 7)
    pdf.text(50,79,f"{con_values[0]}")
    pdf.text(50,84,f"{con_values[1]}")
    pdf.text(50,89,f"{con_values[2]}")
    pdf.text(50,94,f"{con_values[3]}")
    pdf.text(50,99,f"{con_values[4]}")
    pdf.text(50,104,f"{con_values[5]}")
    pdf.text(50,109,f"{encpt_emailid}")
    pdf.text(50,114,f"{encpt_aadhar}")
    pdf.text(50,119,f"{con_values[9]}")
    pdf.set_font('helvetica', 'B', 7)
    pdf.text(63, 62, f"{con_values[8]}")

bill_details = cursor.execute(f"""
                               SELECT *  FROM CHARGE_MASTER_TRACK WHERE CON_ID = 111116
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
    pdf.text(131, 284.5,f"{bill_amt_aftdue}{o}/- Rs")
    pdf.set_font('helvetica', 'B', 14)
    pdf.text(51.5, 191.5, f"{bill_amt}{o}")




    pdf.set_font('helvetica', 'B', 8)

    pdf.text(65, 148, f"{details[0]}")
    pdf.text(65, 159, f"{details[15]}")











pdf.add_page()

pdf.image("Images/bill_howtemplate.png",7,10,110,100)
pdf.image("Images/bill_protocol2template.png",135,11,60,94)
pdf.image("Images/bill_triff2template.png",68,120,130,35)
pdf.image("Images/bill_trifftoptemplate.png",66,113,135,6)
pdf.image("Images/bill_billsumtemplate.png",6,109,60,50)


pdf.set_font('helvetica','B', 10)
pdf.text(13,20,"HOW BILL WAS CALCULATED ")
pdf.set_font('helvetica','B', 7)

pdf.text(13,33,"FIXED CHARGE ")
pdf.text(13,38.5,"WHEELING CHARGE")
pdf.text(13,43.8,"REGULATORY ASSET CHARGE (RAC)")
pdf.text(13,49.2,"ENERGY CHARGE")
pdf.text(13,54.4,"FUEL ADJUSTMENT CHARGE (FAC)")
pdf.text(13,60,"GOVERNMENT ELECTRICITY DUTY                                       16%")
pdf.text(13,65.2,"MAHARASHTRA GOVT. TAX ON SALE OF ELECTRICITY     26.04 p/unit")
pdf.text(13,70.5,"CURRENT MONTHS BILL AMOUNT (A)")
pdf.text(13,75.8,"PREVIOUS MONTHS BILL AMOUNT")
pdf.text(13,81.3,"PROMPT PAYMENT DISCOUNT")
pdf.text(13,86.8,"NET PREVIOUS BALANCE (B)")
pdf.text(13,91.9,"TOTAL BILL AMOUNT (A+B)")
pdf.text(69,116,"KEEP A WATCH TO MANAGE YOUR ELECTRICITY CONSUPTION")

pdf.set_font('helvetica','', 5)
pdf.text(69,118,"YOUR TRIFF STRUCTURE")

pdf.set_font('helvetica','B', 9)
pdf.text(11,123,"ROUND SUM")
pdf.text(11,128,"PAYABLE")
pdf.text(11,133,"FOR THIS BILL")

pdf.set_font('helvetica','B', 6)
pdf.text(10,143,"METER READING DATE")
pdf.text(10,149,"PREVIOUS METER")
pdf.text(10,151,"READING DATE")







pdf.output('C:/Users/Vandana/Documents/Clg Doc/OneDrive/ProjectGit/Electrica/pdf_1.pdf')
webbrowser.open_new(r'file://C:/Users/Vandana/Documents/Clg Doc/OneDrive/ProjectGit/Electrica/pdf_1.pdf')

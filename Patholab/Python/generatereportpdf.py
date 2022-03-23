import sqlite3
from fpdf import FPDF
import webbrowser
from pdf_mail import sendpdf


pdf = FPDF('P', 'mm',(210,297))

pdf.add_page()

pdf.set_font('helvetica', 'B', 8)
pdf.set_text_color(0,0,0)


# Images
pdf.image('Images/Report_toptemp.png',5,15,200,40)
pdf.image('Images/pdf_report_down.png',5,260,200,23)
pdf.image('Images/pdf_backtemp2.png',54,130,100,70)
pdf.image('Images/signature2.jpg',155,241,25,12)
pdf.image('Images/rtpcrback.png',17,92,175,12)

pdf.set_font('helvetica', 'B', 6)
pdf.text(162,253,'Consultant')
pdf.text(153,257,'(Microbiologist/Pathologist)')

conn = sqlite3.connect('Labdb.db')
cur = conn.cursor()
details = cur.execute(f"SELECT * FROM RECEIPT WHERE REC_ID = 1111114")
pdetails = details.fetchall()
for i in pdetails:
    pdf.set_font('helvetica', 'B', 10)
    pdf.set_text_color(0,0,96)
    pdf.text(50,50,f'NAME      : {i[1]}')
    pdf.text(150,50,f'AGE       : {i[2]}')
    pdf.text(50,58,f'GENDER : {i[3]}')
    pdf.text(50,66,f'TEST       : {i[6]}')
    pdf.text(50,74,f'DOCTOR : {i[7]}')
    pdf.text(150,74,f'REC ID   : {i[0]}')
    pdf.text(150,58,f'DATE     : {i[9]}')
    pdf.text(150,66,f'TIME      : {i[10]}')


pdf.set_font('helvetica', 'BU', 10)
pdf.text(80,85,'RT-PCR TEST RESULT')

pdf.set_font('helvetica', 'B', 9)
pdf.set_text_color(0,0,0)
pdf.text(40,97,'REC ID')
pdf.text(92,97,'SAMPLE TYPE')
pdf.text(155,97,'RESULT')
conn = sqlite3.connect('Labdb.db')
cur = conn.cursor()
rtpcrt = cur.execute(f"SELECT * FROM RTPCR WHERE REC_ID = 1111144")
rtpcrresult = rtpcrt.fetchall()
for i in rtpcrresult:
    if i[2] == 'NEGATIVE':
        pdf.set_text_color(0,128,0)
        pdf.text(153.5,102,f'{i[2]}')
    else:
        pdf.set_text_color(255,0,0)
        pdf.text(153.5, 102, f'{i[2]}')
    pdf.set_font('helvetica', '', 9)
    pdf.set_text_color(0, 0, 0)
    pdf.text(40,102,f'{i[0]}')
    pdf.text(93,102,f'{i[1]}')


pdf.set_font('helvetica', '', 8)
pdf.text(20,120,'The performance of this test has been validated & evaluated by National Institute of Virology/ICMR.')
pdf.set_font('helvetica', 'B', 8)
pdf.text(20,125,'Indications')
pdf.text(20,142,'Methodology')
pdf.text(20,155,'Clinical Significance')
pdf.text(20,164,'Limitation of the assay')
pdf.text(20,181,'Disclaimer')
pdf.set_font('helvetica', '', 8)
pdf.text(20,129,'COVID-19 is an infectious disease caused by the virus strain "severe acute respiratory syndrome coronavirus 2" (SARS-CoV-2),')
pdf.text(20,133,'Common signs of infection include respiratory symptoms,fever,cough,shortness of breath and breathing difficulties.')
pdf.text(20,137,'In more severe cases,infection can causes pneumonia ,severe acture respiratory syndrome and kidney failure.')

pdf.text(20,146,'COVID19 detection by polymerase chain reaction (PCR) is based on the amplification of specific regions of the SARS-CoV-2')
pdf.text(20,150,'In real Time PCR the amplified product is detected via fluorescent dyes.')

pdf.text(20,159,'Detection of COVID-19 RNA in patients with COVID-19 infection.')

pdf.text(20,168,'1.Presence of PCR inhibitors may interfere with PCR amplification.')
pdf.text(20,172,'2.Undetected result does not rule out the possibility of infection.Presence of inhibitors,mutations & insufficient')
pdf.text(23,176,'organism RNA can influence the result.')

pdf.text(23,185,'1.This test is intended for use in conjunction with clinical presentation and other laboratory markers.')
pdf.text(23,189,'2.Improper specimen collection, handling, storage and transportation may results in false negative results.')
pdf.text(23,193,'3.The report represents only the specimen received in laboratory.')














#TESTS





pdf.set_font('helvetica', 'B', 10)

pdf.text(16,79,'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
pdf.text(16,233,'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')








pdf.output('Patient Report.pdf')
webbrowser.open_new(r'Patient Report.pdf')




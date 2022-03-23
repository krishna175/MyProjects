import sqlite3
from fpdf import FPDF
import webbrowser


pdf = FPDF('P', 'mm',(210,297))

pdf.add_page()

pdf.set_font('helvetica', 'B', 8)
pdf.set_text_color(0,0,0)


# Images
pdf.image('Images/Report_toptemp.png',5,15,200,40)
pdf.image('Images/pdf_report_down.png',5,260,200,23)
pdf.image('Images/pdf_backtemp2.png',54,130,100,70)
pdf.image('Images/signature2.jpg',155,241,25,12)

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




#TESTS
pdf.set_text_color(0,0,0)
pdf.text(20,93,'TEST NAME')
pdf.text(95,93,'RESULT')
pdf.text(155,93,'NORMAL RANGE')




pdf.set_font('helvetica', 'B', 10)

pdf.text(16,79,'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
pdf.text(16,233,'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')

pdf.set_font('helvetica', 'BU', 12,)
pdf.text(76,85,'COMPLETE BLOOD TEST')
pdf.text(80,170,'DIFFERENTIAL COUNT')


conn = sqlite3.connect('Labdb.db')
cur = conn.cursor()
details = cur.execute(f"SELECT * FROM Report WHERE REC_ID = 1111118")
pdetails = details.fetchall()
for i in pdetails:
    #RESULT
    pdf.set_font('helvetica', '', 8)
    pdf.text(95,110,f'{i[1]}')
    pdf.text(95,120,f'{i[2]}')
    pdf.text(95,130,f'{i[3]}')
    pdf.text(95,140,f'{i[4]}')
    pdf.text(95,150,f'{i[5]}')
    pdf.text(95,160,f'{i[6]}')
    pdf.text(95,181,f'{i[7]}')
    pdf.text(95,191,f'{i[8]}')
    pdf.text(95,201,f'{i[9]}')
    pdf.text(95,211,f'{i[10]}')
    pdf.text(95,221,f'{i[11]}')
    pdf.text(95,231,f'{i[12]}')


#NORMAL VALUES

pdf.set_font('helvetica', '', 8)
pdf.text(155,110,'11.00 - 16.00')
pdf.text(155,120,'3.5 - 5.50')
pdf.text(155,130,'42 - 50')
pdf.text(155,140,'82 - 95')
pdf.text(155,150,'27 - 31')
pdf.text(155,160,'4.5 - 11')
pdf.text(155,181,'40 - 70')
pdf.text(155,191,'1 - 6')
pdf.text(155,201,'0 - 2')
pdf.text(155,211,'20 - 45')
pdf.text(155,221,'2 - 10')
pdf.text(155,231,'150 - 450')


#TEST NAME
pdf.set_font('helvetica', 'B', 8)
pdf.text(20,110,'HEMOGLOBIN')
pdf.text(20,120,'RBC')
pdf.text(20,130,'PCV %')
pdf.text(20,140,'MCV FL')
pdf.text(20,150,'MCH')
pdf.text(20,160,'TOTAL WBC')
pdf.text(20,181,'NEUROPHILES %')
pdf.text(20,191,'EOSINOPHILES %')
pdf.text(20,201,'BASOPHILES %')
pdf.text(20,211,'LYMPHOCYTES %')
pdf.text(20,221,'MONOCYTES %')
pdf.text(20,231,'PLATELET')






pdf.output('Patient Report.pdf')
webbrowser.open_new(r'Patient Report.pdf')


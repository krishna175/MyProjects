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


pdf.set_font('helvetica', 'B', 10)
pdf.text(50,50,'NAME      : HARIKRISHNAN SATHYAN')
pdf.text(150,50,'AGE    : 20')
pdf.text(50,58,'GENDER : MALE')
pdf.text(50,66,'TEST       : COMPLETE BLOOD TEST')
pdf.text(50,74,'REC_ID   : 1111117')
pdf.text(150,58,'DATE  : 09/01/2022')
pdf.text(150,66,'TIME   : 12:00 PM')



pdf.set_font('helvetica', 'B', 10)
pdf.text(16,79,'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')

pdf.output('Patient Report.pdf')
webbrowser.open_new(r'Patient Report.pdf')
from fpdf import FPDF

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
pdf.set_text_color(220,50,50)
# Add text
# w = width
# h = height
# txt = your text
# ln (0 False; 1 True - move cursor down to next line)

# border (0 False; 1 True - add border around cell)
# pdf.cell(20, 10, 'Hello World!', ln=True)
pdf.image('Images/adcon_toptemp.png',5,5,200,47)
pdf.image("Images/bill_nametemplate.png",5,60,80,80)
name = "HARIKRISHNAN SATHYAN"
phone = 9820767941
pdf.text(10,79,f'NAME : {name}')
pdf.text(10,84,f'PHONE NO : {phone}')

pdf.add_page()

pdf.set_font('times', '', 12)
pdf.cell(80, 0, 'Good Bye World!')

pdf.output('C:/Users/Vandana/Documents/Clg Doc/OneDrive/ProjectGit/Electrica/pdf_1.pdf')

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
pdf.set_text_color(220,50,50)
# Add text
# w = width
# h = height
# txt = your text
# ln (0 False; 1 True - move cursor down to next line)

# border (0 False; 1 True - add border around cell)
# pdf.cell(20, 10, 'Hello World!', ln=True)
pdf.image('Images/adcon_toptemp.png',5,5,200,47)
pdf.image("Images/bill_nametemplate.png",20,55,80,80)
pdf.image("Images/bill_amounttemplate.png",17,135,85,65)
pdf.image("Images/bill_contacttemplate.png",115,60,75,37)
pdf.image("Images/bill_consuptiontemplate.png",113,103,75,50)
pdf.image("Images/bill_impmsgtemplate.png",114,155,72,35)
pdf.image("Images/bill_protocoltemplate.png",114,195,72,35,link="https://www.facebook.com/")
pdf.image("Images/bill_cuttemplate.png",5,240,200,8)


name = "HARIKRISHNAN SATHYAN"
phone = 9820767941
pdf.text(30,79,f'NAME : {name}')
pdf.text(30,84,f'PHONE NO : {phone}')

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


pdf.add_page()

pdf.set_font('times', '', 12)
pdf.cell(80, 0, 'Good Bye World!')

pdf.output('C:/Users/Vandana/Documents/Clg Doc/OneDrive/ProjectGit/Electrica/pdf_1.pdf')
webbrowser.open_new(r'file://C:/Users/Vandana/Documents/Clg Doc/OneDrive/ProjectGit/Electrica/pdf_1.pdf')

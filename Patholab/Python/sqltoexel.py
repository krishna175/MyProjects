import sqlite3
from xlsxwriter.workbook import Workbook
workbook = Workbook('output3.xlsx')
worksheet = workbook.add_worksheet()

conn=sqlite3.connect('Labdb.db')
c=conn.cursor()
c.execute("select * from RECEIPT")
mysel=c.execute("select * from RECEIPT ")
for row in mysel:
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i, j, row[j])
workbook.close()
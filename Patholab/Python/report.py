def defaulters(query):
    global viewreport
    viewreport = tk.Toplevel()
    viewreport.title("Report")
    viewreport.configure(bg="white")

    window_width, window_height = 850, 300
    screen_width = viewreport.winfo_screenwidth()
    screen_height = viewreport.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    viewreport.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    viewreport.resizable(width=False, height=False)
    viewreport.iconbitmap('Images/icon2.ico')


    con = cx_Oracle.connect('system/12345@localhost:1521/xe')

    cursor = con.cursor()
    cursor.execute(f"""{query}
                    """)

    tree= ttk.Treeview(viewreport)
    tree['show']='headings'

    tabtheme = ttk.Style(viewreport)
    tabtheme.theme_use("clam")

    tabtheme.configure(".",font=('lucida',10))
    tabtheme.configure("Treeview.Heading",foreground="blue",font=('lucida',9,'bold'))


    # defining the number of columns
    tree["columns"]=("CON_ID","CON_NAME","SUPPLY_TYPE","CHARGE_AMT","BILL_STATUS","BILL_MONTH")

    #assigning the width minwidth and anchor to the specified columns
    tree.column("CON_ID",width=80,minwidth=80,anchor=tk.CENTER)
    tree.column("CON_NAME",width=220,minwidth=220,anchor=tk.CENTER)
    tree.column("SUPPLY_TYPE",width=150,minwidth=150,anchor=tk.CENTER)
    tree.column("CHARGE_AMT",width=100,minwidth=100,anchor=tk.CENTER)
    tree.column("BILL_STATUS",width=100,minwidth=100,anchor=tk.CENTER)
    tree.column("BILL_MONTH",width=100,minwidth=100,anchor=tk.CENTER)

    #assigning the heading of the columns
    tree.heading("CON_ID",text="CON_ID",anchor=tk.CENTER)
    tree.heading("CON_NAME",text="NAME",anchor=tk.CENTER)
    tree.heading("SUPPLY_TYPE",text="TYPE",anchor=tk.CENTER)
    tree.heading("CHARGE_AMT",text="AMOUNT",anchor=tk.CENTER)
    tree.heading("BILL_STATUS",text="STATUS",anchor=tk.CENTER)
    tree.heading("BILL_MONTH",text="MONTH",anchor=tk.CENTER)



    i = 0
    rupee_symbol = u"\u20B9"

    for ro in  cursor:
        tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],rupee_symbol+" "+str(ro[3]),ro[4],ro[5]))
        i+=1

    # VERTICAL SCROLLBAR
    scroll = ttk.Scrollbar(viewreport,orient="vertical")
    scroll.configure(command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)
    scroll.pack(fill="y",side="right")

    tree.place(x=45,y=20)

    viewreport.mainloop()


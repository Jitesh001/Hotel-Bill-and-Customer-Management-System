from tkinter import *
import sqlite3
from datetime import datetime

# database connection and customer table creation
db = sqlite3.connect('Hotel.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS customer(cust_fname TEXT NOT NULL,cust_lname TEXT,\
items TEXT, date INTEGER, bill INTEGER, contact NUMERIC)")
db.commit()
cursor.close()

# create tkinter instance
window = Tk()
window.geometry("700x550")

# canvas for hotel title
c = Canvas(window, bg = 'blue', height = 50, width = 680)
label1 = Label(window, text = "The Indiana Hotel", font = "times 20 bold")
label1.place(x= 220, y= 10)
c.pack()

# 2nd canvas for Menu and Input
lg = ('times',12)
d = Canvas(window, bg = 'pink', height = 530, width = 680)

# name input
label2 = Label(window, text = "Name", font = "times 12 bold", bg = 'pink')
label2.place(x= 60, y= 80)
name = Entry(window,width = 20, font = lg)
name.place(x = 110, y = 80)

# contact input
label = Label(window, text = "Contact", font = "times 12 bold", bg = 'pink')
label.place(x= 300, y= 80)
contact = Entry(window, width = 15, font = lg)
contact.place(x = 380, y = 80)

# menu label
label3 = Label(window, text = "|| Menu ||", font = "times 25 bold", bg = 'pink')
label3.place(x= 260, y= 120)

# menucard in rectangular box
d.create_rectangle(140, 110, 500,400, fill = '#40dae6')

# headings
item = Label(window, text = "Items", font = "times 15",bg = '#40dae6')
item.place(x = 200,y = 170)
price = Label(window, text = "Price(Rs.)", font = "times 15",bg = '#40dae6')
price.place(x = 320,y = 170)
nitems = Label(window, text = "No. items", font = "times 15",bg = '#40dae6')
nitems.place(x = 420,y = 170)

# menu items and price label and entry options from user
lg1 = ('times',14)
i11= Label(window, text = "Aloo Paratha", font = "times 15",bg = '#40dae6')
i11.place(x = 170,y = 200)
i12= Label(window, text = "30", font = "times 15",bg = '#40dae6')
i12.place(x = 320,y = 200)
i13 = Entry(window, width = 6, font = lg1)
i13.place(x = 420, y = 200)

i21= Label(window, text = "Samosa", font = "times 15",bg = '#40dae6')
i21.place(x = 170,y = 220)
i22= Label(window, text = "10", font = "times 15",bg = '#40dae6')
i22.place(x = 320,y = 220)
i23 = Entry(window, width = 6, font = lg1)
i23.place(x = 420, y = 220)

i31= Label(window, text = "Vada-Pav", font = "times 15",bg = '#40dae6')
i31.place(x = 170,y = 240)
i32= Label(window, text = "15", font = "times 15",bg = '#40dae6')
i32.place(x = 320,y = 240)
i33 = Entry(window, width = 6, font = lg1)
i33.place(x = 420, y = 240)

i41= Label(window, text = "Misal", font = "times 15",bg = '#40dae6')
i41.place(x = 170,y = 260)
i42= Label(window, text = "50", font = "times 15",bg = '#40dae6')
i42.place(x = 320,y = 260)
i43 = Entry(window, width = 6, font = lg1)
i43.place(x = 420, y = 260)

i51= Label(window, text = "Paneer-Tikka", font = "times 15",bg = '#40dae6')
i51.place(x = 170,y = 280)
i52= Label(window, text = "150", font = "times 15",bg = '#40dae6')
i52.place(x = 320,y = 280)
i53 = Entry(window, width = 6, font = lg1)
i53.place(x = 420, y = 280)

i61= Label(window, text = "Idali", font = "times 15",bg = '#40dae6')
i61.place(x = 170,y = 300)
i62= Label(window, text = "170", font = "times 15",bg = '#40dae6')
i62.place(x = 320,y = 300)
i63 = Entry(window, width = 6, font = lg1)
i63.place(x = 420, y = 300)

i71= Label(window, text = "Mendu-Vada", font = "times 15",bg = '#40dae6')
i71.place(x = 170,y = 320)
i72= Label(window, text = "60", font = "times 15",bg = '#40dae6')
i72.place(x = 320,y = 320)
i73 = Entry(window, width = 6, font = lg1)
i73.place(x = 420, y = 320)

i81= Label(window, text = "Tea", font = "times 15",bg = '#40dae6')
i81.place(x = 170,y = 340)
i82= Label(window, text = "10", font = "times 15",bg = '#40dae6')
i82.place(x = 320,y = 340)
i83 = Entry(window, width = 6, font = lg1)
i83.place(x = 420, y = 340)

# bill calculation function
def bill():
    lis = ''
    total = 0
    
    # adding prices to total bill and 
    # creating purchased food list 
    if i13.get() != '' : 
        lis += "Aloo Paratha-"+i13.get()+' '
        total += int(i13.get())*30 
    if i23.get() != '' : 
        lis += "Samosa-"+i23.get()+' '
        total += int(i23.get())*10
    if i33.get() != '' : 
        lis += "Vada-pav-"+i33.get()+' '
        total += int(i33.get())*15
    if i43.get() != '' : 
        lis += "Misal-"+i43.get()+' '
        total += int(i43.get())*50
    if i53.get() != '' : 
        lis += "Paneer tikka-"+i53.get()+' '
        total += int(i53.get())*150
    if i63.get() != '' : 
        lis += "Idali-"+i63.get()+' '
        total += int(i63.get())*170
    if i73.get() != '' : 
        lis += "Mendu-Vada-"+i73.get()+' '
        total += int(i73.get())*60
    if i83.get() != '' : 
        lis += "Tea-"+i83.get()+' '
        total += int(i83.get())*10
    
    # label to show bill and total display
    tot1 = Label(window, text = "Total Bill : ", font = "times 15",bg = '#40dae6')
    tot1.place(x = 250,y = 390)
    tot2 = Label(window, text = total, font = "times 15",bg = '#40dae6')
    tot2.place(x = 340,y = 390)
    
    # fetching name and contact and creating date and time
    now = datetime.now()
    dat, tim = now.strftime("%d-%m-%Y %H:%M-%p").split()
    nam, cont = name.get().split(), contact.get()
    
    # inserting data into daatbase
    conn = sqlite3.connect('Hotel.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO customer(cust_fname,cust_lname,items,bill,date,contact,time)\
        VALUES(?,?,?,?,?,?,?)",(nam[0], nam[1], lis, total, dat, cont, tim))
        db.close()

# button to calculate bill and inserting data in database
b1= Button(window, text = "Bill", width = 7, height = 1,bg = '#f21b13', command = bill)
b1.place(x = 170,y = 390)

# function to fetching data from databse and creation of another window to view list of record
def getList():
    # 2nd window creation
    t = Tk()
    t.geometry("600x500")
    
    # 1st canvas for our work
    c1 = Canvas(t, bg = 'maroon', height = 700, width = 600)
    
    # getting date which is being use in where clause
    date1 = str(b21.get())
    
    # connecting data
    conn = sqlite3.connect('Hotel.db')
    cur = conn.cursor()
    cur.execute("SELECT cust_fname, cust_lname, time, bill, contact FROM customer\
    WHERE date = ?",(date1,))
    rows = cur.fetchall()
    
    # heading canvas 
    c2 = Canvas(t, bg = 'blue', height = 50, width = 600) 
    info = Label(t, text = "Customers Visited On date : {}".format(date1), font = "times 15",bg = 'yellow')
    info.place(x = 80,y = 20)
    c2.pack()
    
    #  record heading
    thead = Label(t, text = 'Name' + ' '*10 + 'Surname' + ' '*10 + 'time'  + ' '*14 +\
              'bill'+ ' '*15+'contact', font =  "times 15 bold",bg = 'grey')
    thead.place(x = 30,y = 70)
    
    # displaying records
    m = 100
    for r in rows:
        lis = list(r)
        n = 20
        for item in lis:
            record = Label(t, text = str(item) , font = "times 15 bold", fg = 'yellow', bg = 'maroon')
            record.place(x = n,y = m)
            n += 110
        m += 30
    c1.pack()
    
    # end of record window
    t.mainloop()
    
# entry and button to check reocrds on particular date

#default value for entry and entry box to enter date
v = StringVar(window, value='Enter Date ') 
b21 = Entry(window, width = 10, font = lg1, textvariable=v)
b21.place(x = 150, y = 470)

# date format to enter
b22 = Label(window, text = 'dd-mm-yyyy', font = "times 10",bg = 'pink')
b22.place(x = 150,y = 495)

# button to check records on particular date
b23= Button(window, text = "Get Customer List"\
            , width = 20, height = 1,bg = '#11f515', command = getList)
b23.place(x = 250,y = 470)

d.pack()

# end of main window
window.mainloop()

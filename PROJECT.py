from tkinter import *
from tkinter import ttk
win=Tk()

win.title("STAFF PROFILE PAGE ")

label1=Label(win,text="STAFF PROFILE PAGE AND PATIENT INFORMATION",font=("Arial",20,"bold"),border=10,relief=GROOVE,bg="lightgrey",fg="blue")
label1.grid(row=0,column=0,columnspan=4)

#-------ENTRIES------#

patient_name=Label(win,text="PATIENT NAME :",font=('Arial',17,"bold"),bg="lightgrey",fg="blue")
patient_name.grid(row=1,column=0,pady=15)

patient_ent=Entry(win,bd=12,font=("Arial",12),width=25)
patient_ent.grid(row=1,column=1)
#just get how to post a dateonce
date=Label(win,text="DATE WHEN ADMITTED :",font=('Arial',17,'bold'),bg='lightgrey',fg='blue')
date.grid(row=1,column=2,pady=15)

date_ent=Entry(win,bd=12,font=("Arial",12),width=25)
date_ent.grid(row=1,column=3)

condition=Label(win,text="CONDITION ON ARRIVAL",font=('Arial',17,'bold'),bg='lightgrey',fg='blue')
condition.grid(row=2,column=0,pady=15)

cond=[
    "NORMAL",
    "MILD",
    "MODERATE",
    "CRITICAL",
    "HIGHLY CRITICAL"
]

clicked=StringVar()
clicked.set(cond[0])

condition_box=OptionMenu(win,clicked,*cond)
condition_box.grid(row=2,column=1)

department=Label(win,text='DEPARTMENT ASSIGNED',font=('Arial',17,'bold'),bg='lightgrey',fg='blue')
department.grid(row=4,column=0,pady=15)

options=[
    "OPD UNIT",
    "ORTHO UNIT",
    "PEDIATRATIC UNIT",
    "CARDIOLOGY UNIT",
    "ENT UNIT",
    "SURGERY UNIT",
    "BURN UNIT",
    "OPTHALOMOGY UNIT",
    "NEUROLOGY UNIT",
    "LABOR UNIT"
]
click=StringVar()
click.set(options[0])

department_box=OptionMenu(win,click,*options)
department_box.grid(row=4,column=1)

age=Label(win,text='AGE OF THE PATIENT',font=('Arial',17,'bold'),bg='lightgrey',fg='blue')
age.grid(row=2,column=2,pady=15)

cond=[
    "0-3",
    "3-12",
    "12-18",
    "18-45",
    "45-60",
    ">60"
]

sup=StringVar()
sup.set(cond[0])

age_box=OptionMenu(win,sup,*cond)
age_box.grid(row=2,column=3)

bed=Label(win,text="BED ASSIGNED TO PATIENT",font=('Arial',17,"bold"),bg="lightgrey",fg="blue")
bed.grid(row=3,column=0,pady=15)

bed_ent=Entry(win,bd=12,font=("Arial",12),width=25)
bed_ent.grid(row=3,column=1)

name=Label(win,text="DOCTOR ASSIGNED",font=('Arial',17,"bold"),bg="lightgrey",fg="blue")
name.grid(row=3,column=2,pady=15)

name_ent=Entry(win,bd=12,font=("Arial",12),width=25)
name_ent.grid(row=3,column=3)

phone=Label(win,text="PATIENT PHONE NUM",font=('Arial',17,"bold"),bg="lightgrey",fg="blue")
phone.grid(row=5,column=0,pady=15)

phone_ent=Entry(win,bd=12,font=("Arial",12),width=25)
phone_ent.grid(row=5,column=1)

guard=Label(win,text="GUARDIAN PHONE NUM",font=('Arial',17,"bold"),bg="lightgrey",fg="blue")
guard.grid(row=5,column=2,pady=15)

guard_ent=Entry(win,bd=12,font=("Arial",12),width=25)
guard_ent.grid(row=5,column=3)

address=Label(win,text="ADDRESS OF THE PATIENT",font=('Arial',17,"bold"),bg="lightgrey",fg="blue")
address.grid(row=6,column=0,pady=15)

address_ent=Entry(win,bd=12,font=("Arial",12),width=25)
address_ent.grid(row=6,column=1)

insurance=Label(win,text="INSURANCE APPLICABLE",font=('Arial',17,"bold"),bg="lightgrey",fg="blue")
insurance.grid(row=6,column=2,pady=15)

insur=[
    "STATE BANK OF INDIA",
    "HDFC BANK",
    "CANARA BANK",
    "PUNJAB BANK",
    "WORLD BANK",
    "ICICI BANK",
    "YES BANK",
    "UICOO BANK",
    "NONE"
]
insuran=StringVar()
insuran.set(insur[0])

insurance_box=OptionMenu(win,insuran,*insur)
insurance_box.grid(row=6,column=3)

gender=Label(win,text='GENDER OF PATIENT',font=('Arial',17,'bold'),bg='lightgrey',fg='blue')
gender.grid(row=4,column=2,pady=15)

email=Label(win,text="EMAIL OF THE PATIENT",font=('Arial',17,"bold"),bg="lightgrey",fg="blue")
email.grid(row=7,column=0,pady=15)

email_ent=Entry(win,bd=12,font=("Arial",12),width=25)
email_ent.grid(row=7,column=1)

email1=Label(win,text="EMAIL OF THE GUARDIAN",font=('Arial',17,"bold"),bg="lightgrey",fg="blue")
email1.grid(row=7,column=2,pady=15)

email_ent1=Entry(win,bd=12,font=("Arial",12),width=25)
email_ent1.grid(row=7,column=3)

gend=[
    "MALE",
    "FEMALE",
    "TRANSGENDER",
    "OTHERS"
]

holo=StringVar()
holo.set(gend[0])

gend_box=OptionMenu(win,holo,*gend)
gend_box.grid(row=4,column=3)

def submit():
    return

def update():
    return

def cancel():
    return

button1=Button(win,text="SUBMIT AND SAVE",bg="green",fg="white",padx=0,pady=0,font=("Arial",20,"bold"),command=submit)
button2=Button(win,text="UPDATE AND SAVE",bg="green",fg="white",padx=0,pady=0,font=("Arial",20,"bold"),command=update)
button3=Button(win,text="CANCEL",bg="green",fg="white",padx=0,pady=0,font=("Arial",23,"bold"),command=cancel)

button1.grid(row=12,column=0,pady=30)
button2.grid(row=12,column=1,pady=30,padx=100)
button3.grid(row=12,column=2,pady=30,padx=50)

#-------ENTRIES------#

label10=Label(win,text="FOR ANY QUERIES PLZ CONTACT THE PHONE NUMBER 9877238478,9876532863",font=("Arial",19,"bold"),bg="lightgrey",fg="blue")
label10.grid(row=13,column=0,columnspan=3)

win.mainloop()

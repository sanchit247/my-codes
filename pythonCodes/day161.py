import csv
choice=1
def check(regno,value): # value = 0/1 0 to check 1 to edit record
    data=[]
    with open('student.csv','r') as f:  # r+ for reading and writing
        myreader = csv.reader(f)
        for row in myreader:
            if(row[1]== regno):
                if(value==0):return 1
                if(value==1):
                    print("Record found:\n")
                    print(row)
                    option = input("\n press y to edit n to go back\n ")
                    if(option=='n'):return 0
                    if(option=='y'):
                        row[0] = input("enter the student's name\n")
                        row[1] = input("enter the registration number\n")
                        print("enter the marks")
                        row[2] = float(input("Physics : "))
                        row[3] = float(input("Chemistry : "))
                        row[4] = float(input("Maths : "))
                        row[5] = float(input("Percentage in intermediate: \n"))
                        row[6] = input("enter the course opted\n")
                        row[7]= input("flag active/inactve\n")
                        newlist = open('student.csv', 'a', newline = '')
                        writer = csv.writer(newlist)
                        if(writer.writerow(row)):
                            print("Student record edit successful\n")
                            newlist.close()
                        else:
                            print("Error occured\n")
                            return 0
                        return 1
    return 0
def add():
    name = input("enter the student's name\n")
    regno = input("enter the registration number\n")
    print("enter the marks")
    phy = float(input("Physics : "))
    chem = float(input("Chemistry : "))
    maths = float(input("Maths : "))
    per = float(input("Percentage in intrmediate : \n"))
    course = input("enter the course opted\n")
    flag= input("flag active/inactve\n")
    file = open('student.csv','a',newline='') # a for append so that not overwrites also newline='' so that it does not insert a new line after each record
    mywriter = csv.writer(file)
    mywriter.writerow([name,regno,phy,chem,maths,per,course,flag])
    file.close()
    return
def edit():
    regno = input("enter the registration number of the student\n")
    name = check(regno,1) # 1 because to check and record for record
    print(name)
    return
def fetch():
    with open('student.csv','r') as f:
        myreader = csv.reader(f)
        for row in myreader:
            print(row)
    return
while(choice==1):
    print("choose your option\n1.) Add new Student\n2.) Edit student data\n3.) Fetch student data\n4.) Make data active/inactive\n5.) close")
    opt = int(input())
    if(opt==1): add()
    if(opt==2):edit()
    if(opt==3):fetch()
    if(opt==5):
        print("Thank you ! Have a nice day\n")
        choice=2

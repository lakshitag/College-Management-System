import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
curr = mysql.connector.connect(user="root",passwd="vinod",host="localhost")

myc = curr.cursor()
myc.execute("create database college_result")
myc.execute("use college_result")
myc.execute("create table students(roll_no int(5) not null,name varchar(25) not null,enroll_no int (7),gender varchar(2), DOB date, contact_no decimal(10),primary key(roll_no))")
myc.execute("create table phy01(roll_no int(5) not null,grade varchar(2),gradep int,credits int (3) DEFAULT 88,foreign key(roll_no) references students(roll_no)ON DELETE CASCADE)")
myc.execute("create table mth01(roll_no int(5) not null,grade varchar(2),gradep int,credits int (3)DEFAULT 88,foreign key(roll_no) references students(roll_no)ON DELETE CASCADE)")
myc.execute("create table pe01 (roll_no int(5) not null,grade varchar(2),credits int (3) DEFAULT 25,foreign key(roll_no) references students(roll_no)ON DELETE CASCADE)")
myc.execute("create table esc01(roll_no int(5) not null,grade varchar(2),gradep int,credits int (3) DEFAULT 124,foreign key(roll_no) references students(roll_no)ON DELETE CASCADE)")
myc.execute("create table ta01 (roll_no int(5) not null,grade varchar(2),gradep int,credits int (3) DEFAULT 25,foreign key(roll_no) references students(roll_no)ON DELETE CASCADE)")
myc.execute("create table subject_info(course varchar(50), course_code varchar(15), credits int (3))") 



myc.execute("insert into students values(10958, 'Aarya Gupta', 20195495, 'F', '2001-09-25', 9658741234)")
myc.execute("insert into students values(10959, 'Dhruv Sethi', 20195496, 'M', '2001-12-12', 9741256983)")
myc.execute("insert into students values(10960, 'Ishaan Yadav', 20195497, 'M', '2001-10-28', 7456321789)")
myc.execute("insert into students values(10961, 'Manan Sharma', 20195498, 'M', '2001-01-21', 9612389654)")
myc.execute("insert into students values(10962, 'Pulkit Arora', 20195499, 'M', '2001-02-17', 9741253691)")
myc.execute("insert into students values(10963, 'Riddhi Vyas', 20195500, 'F', '2001-04-07', 8749321654)")
myc.execute("insert into students values(10964, 'Riya Jain', 20195501, 'F', '2001-07-18', 9998563214)")
myc.execute("insert into students values(10965, 'Sakshi Gupta', 20195502, 'F', '2001-09-22', 9741236587)")
myc.execute("insert into students values(10966, 'Saksham Singh', 20195503, 'M', '2001-05-15', 7896541233)")
myc.execute("insert into students values(10967, 'Vikas Meena', 20195504, 'M', '2001-11-05', 9885532114)")
curr.commit()

myc.execute("insert into esc01 values(10958,'B',8,124)")
myc.execute("insert into esc01 values(10959,'B',8,124)")
myc.execute("insert into esc01 values(10960,'C',6,124)")
myc.execute("insert into esc01 values(10961,'A',10,124)")
myc.execute("insert into esc01 values(10962,'B',8,124)")
myc.execute("insert into esc01 values(10963,'C',6,124)")
myc.execute("insert into esc01 values(10964,'B',8,124)")
myc.execute("insert into esc01 values(10965,'B',8,124)")
myc.execute("insert into esc01 values(10966,'B',8,124)")
myc.execute("insert into esc01 values(10967,'C',6,124)")
curr.commit()


myc.execute("insert into mth01 values(10958, 'B',8,88)")
myc.execute("insert into mth01 values(10959, 'C',6,88)")
myc.execute("insert into mth01 values(10960, 'C',6,88)")
myc.execute("insert into mth01 values(10961, 'B',8,88)")
myc.execute("insert into mth01 values(10962, 'A',10,88)")
myc.execute("insert into mth01 values(10963, 'C',6,88)")
myc.execute("insert into mth01 values(10964, 'B',8,88)")
myc.execute("insert into mth01 values(10965, 'A',10,88)")
myc.execute("insert into mth01 values(10966, 'B',8,88)")
myc.execute("insert into mth01 values(10967, 'B',8,88)")
curr.commit()

myc.execute("insert into phy01 values(10958, 'C',6,88)")
myc.execute("insert into phy01 values(10959,'A',10,88)")
myc.execute("insert into phy01 values(10960, 'B',8,88)")
myc.execute("insert into phy01 values(10961, 'B',8,88)")
myc.execute("insert into phy01 values(10962, 'C',6,88)")
myc.execute("insert into phy01 values(10963, 'B',8,88)")
myc.execute("insert into phy01 values(10964, 'A',10,88)")
myc.execute("insert into phy01 values(10965, 'C',6,88)")
myc.execute("insert into phy01 values(10966, 'B',8,88)")
myc.execute("insert into phy01 values(10967, 'D',4,88)")
curr.commit()


myc.execute("insert into ta01 values(10958,'C',6,25)")
myc.execute("insert into ta01 values(10959,'D',4,25)")
myc.execute("insert into ta01 values(10960,'B',8,25)")
myc.execute("insert into ta01 values(10961,'B',8,25)")
myc.execute("insert into ta01 values(10962,'C',6,25)")
myc.execute("insert into ta01 values(10963,'A',10,25)")
myc.execute("insert into ta01 values(10964,'A',10,25)")
myc.execute("insert into ta01 values(10965,'B',8,25)")
myc.execute("insert into ta01 values(10966,'B',8,25)")
myc.execute("insert into ta01 values(10967,'B',8,25)")
curr.commit()

myc.execute("insert into pe01 values(10958,'P',25)")
myc.execute("insert into pe01 values(10959,'P',25)")
myc.execute("insert into pe01 values(10960,'P',25)")
myc.execute("insert into pe01 values(10961,'P',25)")
myc.execute("insert into pe01 values(10962,'P',25)")
myc.execute("insert into pe01 values(10963,'P',25)")
myc.execute("insert into pe01 values(10964,'P',25)")
myc.execute("insert into pe01 values(10965,'P',25)")
myc.execute("insert into pe01 values(10966,'P',25)")
myc.execute("insert into pe01 values(10967,'P',25)")
curr.commit()

myc.execute("insert into subject_info values('INTRODUCTION TO PROGRAMMING', 'ESC01',124)")
myc.execute("insert into subject_info values('MATHEMATICS', 'MTH01', 88)")
myc.execute("insert into subject_info values('PHYSICS', 'PHY01', 88)")
myc.execute("insert into subject_info values('TECHNICAL ARTS', 'TA01', 25)")
myc.execute("insert into subject_info values('PHYSICAL EDUCATION', 'PE01',25)")
curr.commit()

myc.execute("create table grades AS select students.roll_no as roll_no, students.name as name,esc01.grade as esc01, mth01.grade as mth01, phy01.grade as phy01, ta01.grade as ta01,  pe01.grade as pe01 from students INNER JOIN mth01 on students.roll_no = mth01.roll_no INNER JOIN phy01 ON mth01.roll_no = phy01.roll_no INNER JOIN ta01 ON phy01.roll_no = ta01.roll_no INNER JOIN esc01 ON ta01.roll_no = esc01.roll_no INNER JOIN pe01 ON esc01.roll_no = pe01.roll_no")

myc.execute("create table gradepoints AS select students.roll_no as roll_no,students.name as name,esc01.gradep as esc01g, mth01.gradep as mth01g, phy01.gradep as phy01g, ta01.gradep as ta01g from students INNER JOIN mth01 on students.roll_no = mth01.roll_no INNER JOIN phy01 ON mth01.roll_no = phy01.roll_no INNER JOIN ta01 ON phy01.roll_no = ta01.roll_no INNER JOIN esc01 ON ta01.roll_no = esc01.roll_no ")
    
myc.execute("create table cpi AS select roll_no, name, (ta01g*25 + esc01g*124 + mth01g*88 + phy01g*88) /325 as cpi from gradepoints")


myc.close()
curr.close()
'''


def show_data(choice):

    curr = mysql.connector.connect(user="root",passwd="vinod",host="localhost",database="college_result")
    myc = curr.cursor()
    myc.execute("select roll_no from students")
    stu=myc.fetchall()
    rolllist=[list(i) for i in stu]
    
    if choice == "1":
        
        dic={"A":10,"B":8,"C":6,"D":4,"E":2,"F":0}
        roll = int(input("5-digit Roll Number: "))
        
        if [roll] in rolllist:
            myc.execute("select * from students where roll_no= " +str(roll))
            s=pd.DataFrame(myc.fetchall(),columns=['Roll No','Name','Enrollment No','Gender','Date Of Birth','Contact Number'])
            print("Data Already exists:")
            print(s)
        
        elif roll < 10000 or roll > 99999:
            print("Invalid Input")

        else:
            name = input("Name:")
            enroll_no = int(input("Enrollment no: "))
            gender = input("Gender(M/F): ")
            dob = input("DOB(yyyy-mm-dd format): ")
            contact = input("Contact Number: ")
            
            escgrade = input("ESC01 Grade: ")
            mthgrade = input("MTH01 Grade: ")
            phygrade= input("PHY01 Grade: ")
            tagrade = input("TA01 Grade: ")
            pegrade = input("PE garde(P/F): ")
            escgp = dic[escgrade]
            mthgp = dic[mthgrade]
            phygp = dic[phygrade]
            tagp = dic[phygrade]
            
            myc.execute("""insert into students values(%s,%s,%s,%s,%s,%s)""",(roll,name,enroll_no,gender,dob,contact))
            myc.execute("""insert into esc01(roll_no,grade,gradep) values(%s,%s,%s)""",(roll,escgrade,escgp))
            myc.execute("""insert into mth01(roll_no,grade,gradep) values(%s,%s,%s)""",(roll,mthgrade,mthgp))
            myc.execute("""insert into phy01(roll_no,grade,gradep) values(%s,%s,%s)""",(roll,phygrade,phygp))
            myc.execute("""insert into ta01(roll_no,grade,gradep) values(%s,%s,%s)""",(roll,tagrade,tagp))
            myc.execute("""insert into pe01(roll_no,grade) values(%s,%s)""",(roll,pegrade))
            myc.execute("""insert into grades values(%s,%s,%s,%s,%s,%s,%s)""",(roll,name,escgrade,mthgrade,phygrade,tagrade,pegrade))
            myc.execute("""insert into gradepoints values(%s,%s,%s,%s,%s,%s)""",(roll,name,escgp,mthgp,phygp,tagp))
            myc.execute("""insert into cpi values(%s,%s,%s)""",(roll,name,(tagp*25 + escgp*124 + mthgp*88 + phygp*88) /325))

            curr.commit()
            myc.close()
            print("Data Entered Successfully")
            
    elif choice == "2":
        rno = int(input("Enter roll number of the student whose data is to be deleted: "))
        if[rno] in rolllist:
            comm = "delete from students where roll_no =" + str(rno)
            myc.execute(comm)
            comm2 = "delete from grades where roll_no =" + str(rno)
            myc.execute(comm2)
            comm3 = "delete from gradepoints where roll_no =" + str(rno)
            myc.execute(comm3)              
            comm4 = "delete from cpi where roll_no =" + str(rno)
            myc.execute(comm4)

            curr.commit()
            myc.close()
            print("Data deleted successfully")
        else:
            print("Data not found!")

    elif choice == "3":
        comm= "select * from students"
        myc.execute(comm)
        students=pd.DataFrame(myc.fetchall(), columns=['Roll No','Name','Enrollment No','Gender','Date Of Birth','Contact Number'])
        print(students)

    elif choice == "4":
        next_choice = int(input("Type the Roll Number to see display report card\n"))

        if [next_choice] in rolllist:
            comm = "select students.roll_no, students.name, students.enroll_no, esc01.grade, mth01.grade, phy01.grade, ta01.grade, pe01.grade, cpi.cpi from students INNER JOIN mth01 ON students.roll_no = mth01.roll_no INNER JOIN phy01 ON mth01.roll_no = phy01.roll_no INNER JOIN ta01 ON phy01.roll_no = ta01.roll_no INNER JOIN esc01 ON ta01.roll_no = esc01.roll_no INNER JOIN pe01 on esc01.roll_no = pe01.roll_no INNER JOIN cpi ON pe01.roll_no=cpi.roll_no where students.roll_no=" +str(next_choice)
            myc.execute(comm)
            report= pd.DataFrame(myc.fetchall(), columns=['ROLL NO','NAME','ENROLLMENT NO','ESC01','MTH01','PHY01','TA01','PE01','CPI'])
            print(" ")
            print("-----------------------------")
            print("Roll No: " + report['ROLL NO'].to_string(index=False))
            print(" ")
            print("Name: " + report['NAME'].to_string(index=False))
            print(" ")
            print("Enrollment Number: " + report['ENROLLMENT NO'].to_string(index=False))
            print("-----------------------------")
            print(" ")
            print(report[['ESC01','MTH01','PHY01','TA01','PE01']].to_string(index=False))
            print(" ")
            print("---------------------------------------------")
            print("Cumulative Performance Index(CPI) = " + report['CPI'].to_string(index=False))
            print("---------------------------------------------")
            print(" ")
        else:
            print("No data found for the entered Roll No\n")

    elif choice == "5":

        next_choice = input("Type 0 to see grades of all students in all subjects\n"
                            "Type 1 to see ESC01 Grades\n"
                            "Type 2 to see MTH01 Grades\n"
                            "Type 3 to see PHY01 Grades\n"
                            "Type 4 to see TA01 Grades\n"
                            "Type 5 to see PE01 Grades\n")

        if next_choice == "0":
           comm = "select * from grades"
           myc.execute(comm)
           grades_all = pd.DataFrame(myc.fetchall(),columns=['roll_no','name','mth01','phy01','ta01','esc01','pe01'])
           print(grades_all)
        
        elif next_choice == "1":
           comm1 = "select roll_no, grade from esc01"
           myc.execute(comm1)
           esc = pd.DataFrame(myc.fetchall(),columns=['Roll No','Grade'])
           print(esc) 

        elif next_choice == "2":
            myc.execute("select roll_no, grade from mth01")
            mth=pd.DataFrame(myc.fetchall(),columns=["Roll No","Grade"])
            print("The grades of students in Mathematics(MTH01) are as follows:\n")
            print(mth)
        
        elif next_choice == "3":
            myc.execute("select roll_no, grade from phy01")
            phy=pd.DataFrame(myc.fetchall(),columns=["Roll No","Grade"])
            print(phy)

        elif next_choice == "4":
            myc.execute("select roll_no, grade from ta01")
            ta=pd.DataFrame(myc.fetchall(),columns=["Roll No","Grade"])
            print(ta)

        elif next_choice == "5":
            myc.execute("select roll_no, grade from pe01")
            pe=pd.DataFrame(myc.fetchall(),columns=["Roll No","Grade"])
            print(pe)


    elif choice == "6":
	
        next_choice = int(input("Type 0 to see CPI of all students\n"
                                "Type the Roll Number to see CPI of that student\n"))
    
        if next_choice == 0:
            comm = "select * from cpi"
            myc.execute(comm)
            cpi_all = pd.DataFrame(myc.fetchall(),columns=['roll_no','name','cpi'])
            print(cpi_all)
            

        elif [next_choice] in rolllist:
            comm = "select * from cpi where roll_no = " + str(next_choice)
            myc.execute(comm)
            cpi_indiv = pd.DataFrame(myc.fetchall(),columns=['roll_no','name','cpi'])
            print("Roll No. {} {} has CPI = {}".format(next_choice, cpi_indiv.loc[0,'name'] , cpi_indiv.loc[0,'cpi']))
        
        else:
            print("No data found for the entered Roll Number\n")

                              
    elif choice == "7":
        next_choice = input("Type 1 for ESC01 Bar Chart\n"
                            "Type 2 for MTH01 Bar Chart\n"
                            "Type 3 for PHY01 Bar Chart\n"
                            "Type 4 for TA01 Bar Chart\n"
                            "Type 5 for AVERAGE GRADEPOINTS Line Chart\n")
        
        x=np.arange(6)
        g=['A','B','C','D','E','F']
        
        if next_choice == "1":
            comm4 = "select grade from esc01"
            myc.execute(comm4) 
            p = [i[0] for i in myc.fetchall()]
            gl=[p.count('A'),p.count('B'),p.count('C'),p.count('D'),p.count('E'),p.count('F')]
            plt.bar(x,gl,color='c')
            plt.xticks(x,g)
            plt.xlabel('Grades')
            plt.ylabel('Number of students')
            plt.title('Analysis of Grades in ESC01')
            plt.show()

        elif next_choice == "2":
            comm5 = "select grade from mth01"
            myc.execute(comm5) 
            p = [i[0] for i in myc.fetchall()]
            gl=[p.count('A'),p.count('B'),p.count('C'),p.count('D'),p.count('E'),p.count('F')]
            plt.bar(x,gl,color='k')
            plt.xticks(x,g)
            plt.xlabel('Grades')
            plt.ylabel('Number of students')
            plt.title('Analysis of Grades in MTH01')
            plt.savefig('MTH')
            plt.show()

        elif next_choice == "3":
            comm6 = "select grade from phy01"
            myc.execute(comm6) 
            p = [i[0] for i in myc.fetchall()]
            gl=[p.count('A'),p.count('B'),p.count('C'),p.count('D'),p.count('E'),p.count('F')]
            plt.bar(x,gl,color='r')
            plt.xticks(x,g)
            plt.xlabel('Grades')
            plt.ylabel('Number of students')
            plt.title('Analysis of Grades in PHY01')
            plt.savefig('PHY')
            plt.show()

        elif next_choice == "4":
            comm7 = "select grade from ta01"
            myc.execute(comm7) 
            p = [i[0] for i in myc.fetchall()]
            gl=[p.count('A'),p.count('B'),p.count('C'),p.count('D'),p.count('E'),p.count('F')]
            plt.bar(x,gl,color='k')
            plt.xticks(x,g)
            plt.xlabel('Grades')
            plt.ylabel('Number of students')
            plt.title('Analysis of Grades in TA01')
            plt.savefig('TA')
            plt.show()

        elif next_choice =="5":
            comm3= "select avg(esc01g), avg(mth01g), avg(phy01g), avg(ta01g) from gradepoints"
            myc.execute(comm3)
            avg_gradepoints = pd.DataFrame(myc.fetchall())
            avg = avg_gradepoints.iloc[0]
            col = ['ESC01','MTH01','PHY01','TA01']
            plt.plot(col,avg,color='y',marker='H')
            plt.ylim(0,11)
            plt.ylabel('AVERAGE GRADEPOINT')
            plt.xlabel('SUBJECTS')
            plt.title('Average gradepoints of students in various subjects')
            plt.show()
        
        else:
            print("INVALID INPUT\n")
                  
    elif choice == "8":
         co = pd.read_csv("C:\\Users\\Vinod Gopalani\\Desktop\\courses.csv")        
         gr=pd.read_csv("C:\\Users\\Vinod Gopalani\\Desktop\\grades.csv")
         print("\n"
         "ABC ENGINEERING COLLEGE GRADING SYSTEM\n"
         " \n"
         "DESCRIPTION OF GRADES:\n"
         "There are six letter grades: A, B, C, D, E and F.In some courses such as projects, physical education etc.\n"
         "Satisfactory (P) / Unsatisfactory (F) grade is awarded. Grade ‘F’ implies that the student has failed the course.\n"
         "P/F grades are not used for the calculation of CPI.\n"
         "The letter grades, their descriptions, and their Grade Points are as follows:\n")
         print(gr)
         print(" \n"
         "COURSES OFFERED:\n"
         "The courses offered and their respective credits are as follows:\n")
         print(co)
         print(" \n")
         print("CUMULATIVE PERFORMANCE INDEX:\n"
         "The Cumulative Performance Index (CPI) is the average of the grade points earned by a student in all the courses:-\n"
         " \n"
         "CPI = (C1*G1+ C2*G2+ C3*G3+ . . . + Cn*Gn)/(C1+ C2+ C3+ . . . + Cn)\n"
         " \n"
         "where n is the number of courses registered during the semester,\n"
         "Ci is the number of credits allotted to a particular course,\n"
         "and Gi is the grade points to the grade awarded for the course.\n")


    else:
        print("INVALID ENTRY, PLEASE ENTER ACCORDING TO OPTIONS \n")


if __name__=="__main__":

    choice = input("                                \n"
                   "--------------------------------\n"
                   "ABC ENGINEERING COLLEGE, DELHI\n"
                   "--------------------------------\n"
                   "                                \n"
                   "Please enter your choice:\n"
                   "                         \n"
                   "Type 1 to add details of new student\n"
                   "Type 2 to delete the details of a student\n"
                   "Type 3 to display details of all students\n"
                   "\n"
                   "Type 4 to print the Report Card of a student\n"
                   "Type 5 to display subjectwise Grades\n"
                   "Type 6 to display Cumulative Performance Index (CPI) of students\n"
                   "Type 7 to display Graphical Analysis of grades\n"
                   "Type 8 to view description of the grading system\n")

    show_data(choice)
    

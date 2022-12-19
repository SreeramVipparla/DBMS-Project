import mysql.connector as Hospital_Management
# Connect to server
Con=Hospital_Management.connect(port=3306,host="localhost", user="root", passwd="root",database="Hospital_Management")

if Con.is_connected():
    print("s")
# Get a cursor
cur = Con.cursor(buffered=True)

#Create the table
command1 = "CREATE TABLE IF NOT EXISTS patientassigned(Id VARCHAR(10) NOT NULL PRIMARY KEY,Age INT(2) NOT NULL , sex VARCHAR(1) NOT NULL, city VARCHAR(20) NOT NULL , state VARCHAR(20) NOT NULL ,h_no VARCHAR(20) NOT NULL , Name VARCHAR(20) NOT NULL , Discharge_date DATE NOT NULL , Date_admitted DATE NOT NULL , Room_id VARCHAR(10) NOT NULL) ;"
command2 = "CREATE TABLE IF NOT EXISTS Attends(Patient_Id VARCHAR(10) NOT NULL  PRIMARY KEY, doctor_id VARCHAR(10) NOT NULL) ;"
command3 = "CREATE TABLE IF NOT EXISTS Treatment(Patient_Id VARCHAR(10) NOT NULL PRIMARY KEY , treated_for VARCHAR(200) NOT NULL ) ;"
command4 = "CREATE TABLE IF NOT EXISTS Medicines(Patient_Id VARCHAR(10) NOT NULL PRIMARY KEY, Code VARCHAR(10) NOT NULL , Price INT  ,Description TEXT) ;"
command5 = "CREATE TABLE IF NOT EXISTS Equipment(Patient_Id VARCHAR(10) NOT NULL PRIMARY KEY , Price INT  ,Description TEXT);"
command6 = "CREATE TABLE IF NOT EXISTS Room(room_id VARCHAR(10) NOT NULL PRIMARY KEY , room_type TEXT  , Extension BOOLEAN) ;"
command7 = "CREATE TABLE IF NOT EXISTS Nurse(Id VARCHAR(10) NOT NULL PRIMARY KEY , sex VARCHAR(1) ,Name VARCHAR(20) NOT NULL ,Salary INT,qualification VARCHAR(20) ,experience INT ,room_id VARCHAR(10) NOT NULL) ;"
command8 = "CREATE TABLE IF NOT EXISTS Receptionist(id VARCHAR(10) NOT NULL PRIMARY KEY , sex VARCHAR(1) ,Name VARCHAR(20) NOT NULL ,Salary INT,qualification VARCHAR(20) ,experience INT) ;"
command9 = "CREATE TABLE  IF NOT EXISTS Maintains(id VARCHAR(10) NOT NULL PRIMARY KEY , record_no VARCHAR(10) NOT NULL ) ;"
command10 = "CREATE TABLE IF NOT EXISTS Record(Appointment DATETIME NOT NULL , record_no VARCHAR(10) NOT NULL PRIMARY KEY) ;"
command11 = "CREATE TABLE IF NOT EXISTS PatientInfo(record_no VARCHAR(10) NOT NULL PRIMARY KEY,Patient_info VARCHAR(10) NOT NULL);"
command12 = "CREATE TABLE IF NOT EXISTS Doctor (Id VARCHAR(10) NOT NULL PRIMARY KEY , sex VARCHAR(1)  ,salary INT(20) NOT NULL , Name VARCHAR(20) NOT NULL ,qualification VARCHAR(20) ,experience INT) ;"
cur.execute(command1)
cur.execute(command2)
cur.execute(command3)
cur.execute(command4)
cur.execute(command5)
cur.execute(command6)
cur.execute(command7)
cur.execute(command8)
cur.execute(command9)
cur.execute(command10)
cur.execute(command11)
cur.execute(command12)

#Insert Foreign keys
command13="Alter TABLE patientassigned ADD FOREIGN KEY(room_id) references Room(room_id);"
command14="Alter TABLE Attends ADD FOREIGN KEY(Patient_Id) references patientassigned(id);"
command15="Alter TABLE Attends ADD FOREIGN KEY(doctor_id) references Doctor(id);"
command16="Alter TABLE Treatment ADD FOREIGN KEY(Patient_Id) references patientassigned(id);"
command17="Alter TABLE Medicines ADD FOREIGN KEY(Patient_Id) references patientassigned(id);"
command18="Alter TABLE Equipment ADD FOREIGN KEY(Patient_Id) references patientassigned(id);"
command19="Alter TABLE Nurse ADD FOREIGN KEY(room_id) references Room(room_id);"
command20="Alter TABLE Maintains ADD FOREIGN KEY(id) references Receptionist(id);"
command21="Alter TABLE Maintains ADD FOREIGN KEY(record_no) references Record(record_no);"
command22="Alter TABLE PatientInfo ADD FOREIGN KEY(record_no) references Record(record_no);"
command23="Alter TABLE PatientInfo ADD FOREIGN KEY(Patient_info) references patientassigned(id);"
cur.execute(command13)
cur.execute(command14)
cur.execute(command15)
cur.execute(command16)
cur.execute(command17)
cur.execute(command18)
cur.execute(command19)
cur.execute(command20)
cur.execute(command21)
cur.execute(command22)
cur.execute(command23)

#Insert values in tables
"""
command24="INSERT INTO doctor VALUES  ('AC123', 'M', 100000, 'Dr. V Sreeram', 'MBBS', 10),('AP785', 'M', 120000, 'Dr. Harsh Kumar', 'M.D.', 8),('AF465', 'M', 80000, 'Dt. Kunal Nehra', 'BDS', 13),('AE412', 'M', 75000, 'Dr. Ankit Kumar', 'BAMS', 14),('AC142', 'M', 100000, 'Dr. A Poonewala', 'MBBS', 5),('AP153', 'M', 120000, 'Dr. M Chauhan', 'M.D.', 15),('AC563', 'F', 100000, 'Dr. Ruchi Chaudhry', 'MBBS', 12);"
command25="INSERT INTO Room VALUES('S-43','Single','0'),('M-23','Double Sharing','1'),('K-33','Single','1'),('S-44','Triple Sharing','0'),('N-43','Single','1');"
command26="INSERT INTO patientassigned VALUES('23AB546',34,'M','Powai','Mumbai','109A','Andrew','2022-09-06','2022-08-06','M-23'),('24CD756',27,'F','Dwarka','Delhi','589','Mrinal','2022-09-16','2022-08-06','M-23'),('50AB100',36,'M','Powai','Mumbai','264A','Rohit','2022-08-06','2022-07-09','N-43'),('99AC999',19,'M','Hisar','Haryana','142','Kunal','2022-02-08','2022-01-29','K-33'),('33AB333',20,'M','Dwarka','Delhi','333A','Harsh','2022-08-06','2022-08-06','S-44');"
command27="INSERT INTO attends VALUES('23AB546','AC123'),('24CD756','AC142'),('50AB100','AC123'),('99AC999','AC563'),('33AB333','AF465');"
command28="INSERT INTO Nurse VALUES('NP543','F','Mary',43000,'RN',8,'M-23'),('NP544','F','Lily',44000,'RN BSN',9,'N-43'),('NP545','F','Rylee',45000,'RN BSN',10,'M-23'),('NP546','F','Anei',46000,'RN BSN',11,'S-44'),('NP547','F','Emmy',47000,'RN BSN',12,'K-33');"
command29="INSERT INTO Receptionist VALUES('RA432','F','Katy',18600,'BA',3),('RA433','F','Annie',19600,'BA',4),('RA434','F','Taylor',20600,'BA',5),('RA435','M','Ed',21600,'BA',6),('RA436','M','Ryle',22600,'BA',7);"
command30="INSERT INTO Treatment VALUES('23AB546','Pneumothorax'),('24CD756','Cancer'),('50AB100','TB'),('99AC999','Anemia'),('33AB333','Dengue');"
command31="INSERT INTO Medicines VALUES('23AB546','MZ988',2424,'Helps in reducing inflammation'),('24CD756','MZ976',200,'Helps in reding acidity'),('33AB333','MZ987',2423,'Acts as a painkiller'),('50AB100','MZ9543',2978,'Anesthetic'),('99AC999','MZ654',634,'helps with chemotheraphy');"
command32="INSERT INTO Equipment VALUES('23AB546',456700,'Ventilator used for helping people breath '),('24CD756',4670,'Tubes'),('50AB100',5567,'Oxygen Cylinder'),('99AC999',5567,'Oxygen Cylinder '),('33AB333',4170,'Blood Tester');"
command33="INSERT INTO Record VALUES('2022-11-20 13:20:00','RE1009'),('2022-11-21 14:30:00','RE1087'),('2022-11-22 15:40:00','RE1065'),('2022-11-23 15:50:00','RE1066'),('2022-11-24 16:10:00','RE1067');"
command34="INSERT INTO PatientInfo VALUES('RE1009','23AB546'),('RE1087','50AB100'),('RE1065','24CD756'),('RE1066','33AB333'),('RE1067','99AC999');"
command35="INSERT INTO Maintains VALUES('RA432','RE1009'),('RA433','RE1087'),('RA434','RE1065'),('RA435','RE1066'),('RA436','RE1067');"

cur.execute(command24)
cur.execute(command25)
cur.execute(command26)
cur.execute(command27)
cur.execute(command28)
cur.execute(command29)
cur.execute(command30)
cur.execute(command31)
cur.execute(command32)
cur.execute(command33)
cur.execute(command34)
cur.execute(command35)
Con.commit()
"""
############################################################################################################################
#                                            MENU                                                                          #       
#                                                                                                                          #
############################################################################################################################

def Menu():
      print("                                                                              NSUT HOSPITAL ")
      print("Dear Esteemed User,Please fell free to explore our hospital and learn how we function and how everything correlate ")
      print("To proceed further please select 'ONE' of the option from the menu given below")
      print("Menu")
      print("------------------")
      print("1)VIEW")
      print("2)UPDATE")
      print("3)DELETE")
      print("4)AGGREGATE")
      print("5)JOIN")
      print("6)MISCELLANEOUS")
      print("7)QUIT")
      Output1()

############################################################################################################################
#                                           VIEW FUNCTION                                                                  #       
#                                                                                                                          #
############################################################################################################################

def View_Table_function():
    print("Dear user, proceed further by choosing 'ONE' of the option given below ")
    print("1)View Complete table")
    print("2)Select some specific information")
    print("3)Quit")
    Output3()

def View_function():
       print("Dear user, proceed further by choosing 'ONE' of the option given below ")
       print("1)View Table")
       print("2)Create View")
       print("3)View Table Description")
       print("4)Quit")
       Output2()

def Complete_table_function():
    print("These are all the tables in our database")
    print("These are the Tables Present")
    cur.execute("SHOW TABLES")
    tables=cur.fetchall()
    print(tables)
    print("Please Type below the name of the table(CAPS or LOWERCASE) that you wish to see")
    Table_name =input("input table name:")
    command1="SELECT * FROM "+ Table_name
    command2=command1
    cur.execute(command2)
    result = cur.fetchall()
    for row in result:
        print(row)
        print("\n")
    print("Select 'YES' to view other tables,'NO' for returning to the menu")
    Output4()

def Specific_info_function():
    print("These are all the tables in our database")
    print("These are the Tables Present")
    cur.execute("SHOW TABLES")
    tables=cur.fetchall()
    print(tables)
    print("Please Type below the name of the table(CAPS or LOWERCASE) that you wish to see")
    Table_name=input()
    print("Given below is the complete view of the table")
    command2="SELECT * FROM "+Table_name
    cur.execute(command2)
    result = cur.fetchall()
    for row in result:
        print(row)
        print("\n")
    print("Please type the name of the Selector")
    Selector=input()
    command111="DESC "+Table_name
    command112=command111
    print("This is what you have executed")
    print(command112)
    cur.execute(command112)
    result = cur.fetchall()
    print(result)
    print("Please type the name of the Column")
    Coloumn_name=input()
    print("Please select the type of comparision operation you would like to perfrom")
    Operator=input()
    print("Please type any additional information")
    Misc=input()
    command3="SELECT"+" "+Selector+" "+"FROM"+" "+Table_name+" "+"WHERE"+" "+Coloumn_name+" "+Operator+" "+Misc
    command4=command3
    cur.execute(command4)
    result = cur.fetchall()
    print(result)
    print("Select 'YES' to view more information,'NO' for returning to the menu")
    Output5()

def Create_View_function():
    print("Dear User,Please input the command for viewing the 'create view' command.Please enclose the whole statement in double quotes")
    #CREATE VIEW [Brazil Customers] AS SELECT CustomerName, ContactName FROM Customers WHERE Country = 'Brazil';
    print("These are all the tables that are present")
    cur.execute("SHOW TABLES")
    tables=cur.fetchall()
    print(tables)
    print("Please enter the name of the Table ")
    table_name=input()
    print("Please enter the name of the view that you want to create ")
    view_name=input()
    print("Given below is the description of the table 1 ")
    command5="DESC "+table_name
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Please insert the values in the tables according to the table description.")
    print("Eg-CREATE VIEW [Brazil Customers] AS SELECT CustomerName, ContactName FROM Customers WHERE Country = 'Brazil';")
    print("Please use the above given TABLE DESCRIPTION to fill the column name")
    print("Please enter a column name from table 1 ")
    print("LIKE EG- Id or Country")
    print("You can choose multiple columns,just put a ',' when writing it")
    print("eg-Customername, contactname")
    column_name=input()
    print("Please enter the condition that you want to view in the table")
    print("Eg-city='Brazil'")
    condition=input()
    command="CREATE VIEW "+ view_name +" AS SELECT "+column_name+" FROM "+table_name+" WHERE "+condition
    cur.execute(command)
    Con.commit()
    result = cur.fetchall()
    print(result)
    print("Select 'YES' to view more information,'NO' for returning to the menu")
    Output6() 
    
def View_Table_Description_function():
    cur.execute("SHOW TABLES")
    tables=cur.fetchall()
    result = cur.fetchall()
    print(tables)
    for row in result:
        print(row)
        print("\n")
    print("Please Type below the name of the table(CAPS or LOWERCASE) that you wish to see")
    Table_name=input()
    command5="DESC "+Table_name
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Select 'YES' to view more information,'NO' for returning to the menu")
    Output7()

def Output1():
    Output=input()
    if(Output=='1'):
        View_function()
    elif(Output=='2'):
        Update_function()
    elif(Output=='3'):
        Delete_function()
    elif(Output=='4'):
        Aggregate_function()
    elif(Output=='5'):
        Join()
    elif(Output=='6'):
        Miscellaneous_function()
    elif(Output=='7'):
        Quit()
    else:
        print("Please select a number given in the options ")
        Output1()

def Output2():
    Output=input()
    if (Output=='1'):
        View_Table_function()
    elif(Output=='2'):
        Create_View_function()
    elif(Output=='3'):
        View_Table_Description_function()
    elif(Output=='4'):
        Quit()
    else:
        print("Please select a number given in the options")
        Output2()

def Output3():
    Output=input()
    if (Output=='1'):
        Complete_table_function()
    elif(Output=='2'):
        Specific_info_function()
    elif(Output=='3'):
        Quit()
    else:
        print("Please select a number given in the options")
        Output3()
    print()

def Output4():
    Output=input()
    if (Output=='YES'):
        Complete_table_function()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options")
        Output4()

def Output5():
    Output=input()
    if (Output=='YES'):
        Specific_info_function()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options")
        Output5()

def Output6():
    Output=input()
    if (Output=='YES'):
        View_Table_Description_function()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options")
        Output6()

def Output7():
    Output=input()
    if (Output=='YES'):
        Create_View_function()
    elif(Output=='NO'):
        Quit()
    else:
        print("Please select a number given in the options")
        Output7()
       
def Quit():
    Menu()

############################################################################################################################
#                                            UPDATE FUNCTION                                                               #       
#                                                                                                                          #
############################################################################################################################

def Update_function():
    print("Please choose an option from the following")
    print("1)CREATE TABLE")
    print("2)INSERT ADDITIONAL DATA")
    print("3)UPDATE DATA")
    print("4)ALTER 'ADD' TABLE")
    print("5)QUIT")
    Output8()

def Output8():
    Output=input()
    if(Output=='1'):
        Create_table()
    elif(Output=='2'):
        Insert_data()
    elif(Output=='3'):
        Update_Data()
    elif(Output=='4'):
        Alter_Add_Table()
    elif(Output=='5'):
        Quit()
    else:
        print("Please select a number given in the options ")
        Output8()

def Output9():
    Output=input()
    if(Output=='YES'):
        Create_table()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options ")
        Output9()

def Create_table():
    print("Please enter the name of the Table you want to add")
    table_name=input()
    print("Enter the name of the columns and the data types that you want to add")
    column_info=input()
    column_info1=(column_info)
    command="CREATE TABLE "+table_name+column_info1
    cur.execute(command)
    Con.commit()
    print("Below is the table that you have just created")
    command1="SELECT * FROM "+ table_name
    command2=command1
    cur.execute(command2)
    result = cur.fetchall()
    for row in result:
        print(row)
        print("\n")
    print("Select 'YES' to add a new table,'NO' for returning to the menu")
    Output9()
    
def Output10():
    Output=input()
    if(Output=='YES'):
       Insert_data()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options ")
        Output10()
##"INSERT INTO Maintains VALUES('RA432','RE1009'),('RA433','RE1087'),('RA434','RE1065'),('RA435','RE1066'),('RA436','RE1067');"
def Insert_data():
    print("Please enter the name of the Table")
    table_name=input()
    print("Given below is the description of the table,Insert values accordingly")
    command5="DESC "+table_name
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Please insert the values in the tables according to the table description")
    print("The given statement is an example")
    print("INSERT INTO Maintains VALUES('RA432','RE1009'),('RA433','RE1087'),('RA434','RE1065'),('RA435','RE1066')")
    column_info=input()
    column_info1=(column_info)
    command="INSERT INTO "+table_name+ " VALUES"+(column_info1)
    cur.execute(command)
    Con.commit()
    print("Below is the table that you have just inserted the values into")
    command2="SELECT * FROM "+table_name
    cur.execute(command2)
    result = cur.fetchall()
    for row in result:
        print(row)
        print("\n")
    print("Select 'YES' to add a new data,'NO' for returning to the menu")
    Output10()

def Output11():
    Output=input()
    if(Output=='YES'):
       Update_Data()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options ")
        Output11()

def Update_Data():
    print("Please enter the name of the Table")
    table_name=input()
    print("Given below is the description of the table,Insert values accordingly")
    command5="DESC "+table_name
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Please insert the values in the tables according to the table description.Eg-UPDATE Customers SET ContactName='Juan' WHERE Country='Mexico';")
    column_info=input()
    command="UPDATE "+table_name+" SET "+column_info
    cur.execute(command)
    Con.commit()
    print("Below is the table that you have just updated the values into")
    command2="SELECT * FROM "+table_name
    cur.execute(command2)
    result = cur.fetchall()
    for row in result:
        print(row)
        print("\n")
    Con.commit()
    print("Select 'YES' to update more data,'NO' for returning to the menu")
    Output11()

def Alter_Add_Table():
    print("Please enter the name of the Table")  
    table_name=input()
    print("Given below is the description of the table,Insert values accordingly")
    command5="DESC "+table_name
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    Con.commit()
    print("Please insert the COLUMN_INFO values that are to be 'ADDED' according to the table description.Eg-ALTER TABLE Customers ADD Email varchar(55);")
    print("Please enter the commands as 'EMAIL Varchar(55)")
    column_info=input()
    command="ALTER TABLE "+table_name+" ADD "+column_info
    cur.execute(command)
    Con.commit()
    print("Below is the table that you have just updated the values into")
    command2="SELECT * FROM "+table_name
    cur.execute(command2)
    result = cur.fetchall()
    for row in result:
        print(row)
        print("\n")
    Con.commit()
    print("Select 'YES' to update more data,'NO' for returning to the menu")
    Output12()

def Output12():
    Output=input()
    if(Output=='YES'):
       Alter_Add_Table()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options ")
        Output12()

############################################################################################################################
#                                           DELETE FUNCTION                                                                #       
#                                                                                                                          #
############################################################################################################################

def Delete_function():
    print("Please choose an option from the following")
    print("1)DROP TABLE")
    print("2)ALTER 'DROP' TABLE")
    print("3)TRUNCATE ")
    print("4)Quit ")
    Output14()

def Output14():
    Output=input()
    if(Output=='1'):
        Drop_table()
    elif(Output=='2'):
        Alter_Drop_data()
    elif(Output=='3'):
        Truncate()
    elif(Output=='4'):
        Quit()
    else:
        print("Please select a number given in the options ")
        Delete_function()

def Drop_table():
    print("Please enter the name of the Table")  
    table_name=input()
    command="DROP TABLE"+table_name
    cur.execute(command)
    Con.commit()
    print("Below is the overall tables left after deletion")
    cur.execute("SHOW TABLES")
    tables=cur.fetchall()
    print(tables)
    Con.commit()
    print("Select 'YES' to drop tables,'NO' for returning to the menu")
    Output13()

def Output13():
    Output=input()
    if(Output=='YES'):
       Drop_table()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options ")
        Output13()

def Alter_Drop_data():
    print("Please enter the name of the Table")  
    table_name=input()
    command="DROP TABLE "+table_name
    cur.execute(command)
    Con.commit()
    print("Below is the overall tables left after deletion")
    cur.execute("SHOW TABLES")
    tables=cur.fetchall()
    print(tables)
    Con.commit()
    print("Select 'YES' to drop tables,'NO' for returning to the menu")
    Output13()

def Output14():
    Output=input()
    if(Output=='YES'):
       Truncate()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options ")
        Output14()

def Truncate():
    print("Please enter the name of the Table you want to truncate")  
    print("The difference between TRUNCATE and DROP is that DROP deletes everything whereas")
    print("TRUNCATE only deletes the data and restores the stucture of the table")
    table_name=input()
    #TRUNCATE TABLE  TableName;
    command="TRUNCATE TABLE "+table_name
    cur.execute(command)
    Con.commit()
    print("Below is the overall tables left after TRUNCATION")
    cur.execute("SHOW TABLES")
    tables=cur.fetchall()
    print(tables)
    Con.commit()
    print("Select 'YES' to TRUNCATE tables,'NO' for returning to the menu")
    Output14()

def Output15():
    Output=input()
    if (Output=='1'):
        Count()
    elif(Output=='2'):
        Sum()
    elif(Output=='3'):
        Avg()
    elif(Output=='4'):
        Min()
    elif(Output=='5'):
        Max()
    elif(Output=='6'):
        Quit()
    else:
        print("Please select a number given in the options")
        Output15()

############################################################################################################################
#                                        AGGREGATE FUNCTION                                                                #       
#                                                                                                                          #
############################################################################################################################

def Aggregate_function():
    print("Please choose an option from the following")
    print("1)COUNT")
    print("2)SUM")
    print("3)AVG")
    print("4)MAX")
    print("5)MIN")
    print("6)QUIT")
    Output15()

def Count():
    print("These are all the tables that are present")
    cur.execute("SHOW TABLES")
    tables=cur.fetchall()
    print(tables)
    print("Please enter the name of the Table where you want to Count")
    table_name=input()
    print("Given below is the description of the table")
    command5="DESC "+table_name
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Please insert the values in the tables according to the table description.Eg-SELECT COUNT(column_name) FROM table_name WHERE condition;")
    print("Please use the above given TABLE DESCRIPTION to fill the column name")
    column_name=input()
    print("Please enter the condition part of the SQL QUERY")
    condition=input()
    command="SELECT COUNT("+column_name+") FROM "+table_name+" WHERE "+ condition
    cur.execute(command)
    Con.commit()
    print("Select 'YES' to manipulate more data,'NO' for returning to the menu")
    Output16()

def Output16():
    Output=input()
    if(Output=='YES'):
       Count()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options ")
        Output16()

def Sum():
    print("These are all the tables that are present")
    cur.execute("SHOW TABLES")
    tables=cur.fetchall()
    print(tables)
    print("Please enter the name of the Table where you want to ADD")
    table_name=input()
    print("Given below is the description of the table")
    command5="DESC "+table_name
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Please insert the values in the tables according to the table description.Eg-SELECT SUM(column_name) FROM table_name WHERE condition;")
    print("Please use the above given TABLE DESCRIPTION to fill the column name")
    column_name=input()
    print("Please enter the condition part of the SQL QUERY")
    print("LIKE EG- VALUE>8")
    condition=input()
    command="SELECT SUM("+column_name+") FROM "+table_name+" WHERE "+ condition
    cur.execute(command)
    Con.commit()
    print("Select 'YES' to manipulate more data,'NO' for returning to the menu")
    Output17()

def Output17():
    Output=input()
    if(Output=='YES'):
       Sum()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options ")
        Output17()

def Avg():
    print("These are all the tables that are present")
    cur.execute("SHOW TABLES")
    tables=cur.fetchall()
    print(tables)
    print("Please enter the name of the Table where you want to find AVERAGE")
    table_name=input()
    print("Given below is the description of the table")
    command5="DESC "+table_name
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Please insert the values in the tables according to the table description.Eg-SELECT AVG(column_name) FROM table_name WHERE condition;")
    print("Please use the above given TABLE DESCRIPTION to fill the column name")
    column_name=input()
    print("Please enter the condition part of the SQL QUERY")
    print("LIKE EG- VALUE>8")
    condition=input()
    command="SELECT AVG("+column_name+") FROM "+table_name+" WHERE "+ condition
    cur.execute(command)
    Con.commit()
    print("Select 'YES' to manipulate more data,'NO' for returning to the menu")
    Output18()

def Output18():
    Output=input()
    if(Output=='YES'):
       Avg()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options ")
        Output18()

def Max():
    print("These are all the tables that are present")
    cur.execute("SHOW TABLES")
    tables=cur.fetchall()
    print(tables)
    print("Please enter the name of the Table where you want to find MAX")
    table_name=input()
    print("Given below is the description of the table")
    command5="DESC "+table_name
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Please insert the values in the tables according to the table description.Eg-SELECT MAX(column_name) FROM table_name WHERE condition;")
    print("Please use the above given TABLE DESCRIPTION to fill the column name")
    column_name=input()
    print("Please enter the condition part of the SQL QUERY")
    print("LIKE EG- VALUE>8")
    condition=input()
    command="SELECT MAX("+column_name+") FROM "+table_name+" WHERE "+ condition
    cur.execute(command)
    Con.commit()
    print("Select 'YES' to manipulate more data,'NO' for returning to the menu")
    Output19()

def Output19():
    Output=input()
    if(Output=='YES'):
       Max()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options ")
        Output19()

def Min():
    print("These are all the tables that are present")
    cur.execute("SHOW TABLES")
    tables=cur.fetchall()
    print(tables)
    print("Please enter the name of the Table where you want to find MIN")
    table_name=input()
    print("Given below is the description of the table")
    command5="DESC "+table_name
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Please insert the values in the tables according to the table description.Eg-SELECT MIN(column_name) FROM table_name WHERE condition;")
    print("Please use the above given TABLE DESCRIPTION to fill the column name")
    column_name=input()
    print("Please enter the condition part of the SQL QUERY")
    print("LIKE EG- VALUE>8")
    condition=input()
    command="SELECT MIN("+column_name+") FROM "+table_name+" WHERE "+ condition
    cur.execute(command)
    Con.commit()
    print("Select 'YES' to manipulate more data,'NO' for returning to the menu")
    Output20()

def Output20():
    Output=input()
    if(Output=='YES'):
       Min()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options ")
        Output20()

############################################################################################################################
#                                            JOIN FUNCTION                                                                 #       
#                                                                                                                          #
############################################################################################################################

def Join():
    print("Please choose an option from the following")
    print("1)INNER JOIN")
    print("2)LEFT JOIN")
    print("3)RIGHT JOIN")
    print("4)OUTER JOIN")
    print("5)UNION")
    print("6)ALIASES")
    print("7)QUIT")
    Output21()

def Output21():
    Output=input()
    if (Output=='1'):
        Inner_Join()
    elif(Output=='2'):
        Left_Join()
    elif(Output=='3'):
        Right_Join()
    elif(Output=='4'):
        Outer_Join()
    elif(Output=='5'):
        Union()
    elif(Output=='6'):
        Aliases()
    elif(Output=='7'):
        Quit()
    else:
        print("Please select a number given in the options")
        Output21()

def Inner_Join():
    #SELECT column_name(s) FROM table1 INNER JOIN table2 ON table1.column_name = table2.column_name;
    print("These are all the tables that are present")
    cur.execute("SHOW TABLES")
    tables=cur.fetchall()
    print(tables)
    print("Please enter the name of the Table 1")
    table_name=input()
    print("Please enter the name of the Table 2")
    table_name1=input()
    print("Given below is the description of the table 1 ")
    command5="DESC "+table_name
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Given below is the description of the table 2 ")
    command5="DESC "+table_name1
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Please insert the values in the tables according to the table description.")
    print("Eg-SELECT column_name(s) FROM table1 INNER JOIN table2 ON table1.column_name = table2.column_name;")
    print("Please use the above given TABLE DESCRIPTION to fill the column name")
    print("Please enter a common column name ")
    print("LIKE EG- Id")
    column_name=input()
    command="SELECT "+ column_name +" FROM "+table_name+" INNER JOIN "+table_name1+" ON "+ table_name+"."+column_name +" = "+table_name1+"."+column_name
    #SELECT Orders.OrderID, Customers.CustomerName FROM Orders INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
    cur.execute(command)
    Con.commit()
    result = cur.fetchall()
    print(result)
    print("Select 'YES' to manipulate more data,'NO' for returning to the menu")
    Output22()

def Output22():
    Output=input()
    if(Output=='YES'):
        Inner_Join()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options ")
        Output22()

def Left_Join():
    #SELECT column_name(s) FROM table1 LEFT JOIN table2 ON table1.column_name = table2.column_name;
    print("These are all the tables that are present")
    cur.execute("SHOW TABLES")
    tables=cur.fetchall()
    print(tables)
    print("Please enter the name of the Table 1")
    table_name=input()
    print("Please enter the name of the Table 2")
    table_name1=input()
    print("Given below is the description of the table 1 ")
    command5="DESC "+table_name
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Given below is the description of the table 2 ")
    command5="DESC "+table_name1
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Please insert the values in the tables according to the table description.")
    print("Eg-SELECT column_name(s) FROM table1 LEFT JOIN table2 ON table1.column_name = table2.column_name;")
    print("Please use the above given TABLE DESCRIPTION to fill the column name")
    print("Please enter a common column name ")
    print("LIKE EG- Id")
    column_name=input()
    command="SELECT "+ column_name +" FROM "+table_name+" LEFT JOIN "+table_name1+" ON "+ table_name+"."+column_name +" = "+table_name1+"."+column_name
    #SELECT Orders.OrderID, Customers.CustomerName FROM Orders LEFT JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
    cur.execute(command)
    Con.commit()
    result = cur.fetchall()
    print(result)
    print("Select 'YES' to manipulate more data,'NO' for returning to the menu")
    Output23()

def Output23():
    Output=input()
    if(Output=='YES'):
        Left_Join()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options ")
        Output23()

def Right_Join():
     #SELECT column_name(s) FROM table1 RIGHT JOIN table2 ON table1.column_name = table2.column_name;
    print("These are all the tables that are present")
    cur.execute("SHOW TABLES")
    tables=cur.fetchall()
    print(tables)
    print("Please enter the name of the Table 1")
    table_name=input()
    print("Please enter the name of the Table 2")
    table_name1=input()
    print("Given below is the description of the table 1 ")
    command5="DESC "+table_name
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Given below is the description of the table 2 ")
    command5="DESC "+table_name1
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Please insert the values in the tables according to the table description.")
    print("Eg-SELECT column_name(s) FROM table1 RIGHT JOIN table2 ON table1.column_name = table2.column_name;")
    print("Please use the above given TABLE DESCRIPTION to fill the column name")
    print("Please enter a common column name ")
    print("LIKE EG- Id")
    column_name=input()
    command="SELECT "+ column_name +" FROM "+table_name+" RIGHT JOIN "+table_name1+" ON "+ table_name+"."+column_name +" = "+table_name1+"."+column_name
    #SELECT Orders.OrderID, Customers.CustomerName FROM Orders RIGHT JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
    cur.execute(command)
    Con.commit()
    result = cur.fetchall()
    print(result)
    print("Select 'YES' to manipulate more data,'NO' for returning to the menu")
    Output24()

def Output24():
    Output=input()
    if(Output=='YES'):
        Right_Join()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options ")
        Output24()

def Outer_Join():
     #SELECT column_name(s) FROM table1 FULL OUTER JOIN table2 ON table1.column_name = table2.column_name WHERE condition;
    print("These are all the tables that are present")
    cur.execute("SHOW TABLES")
    tables=cur.fetchall()
    print(tables)
    print("Please enter the name of the Table 1")
    table_name=input()
    print("Please enter the name of the Table 2")
    table_name1=input()
    print("Given below is the description of the table 1 ")
    command5="DESC "+table_name
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Given below is the description of the table 2 ")
    command5="DESC "+table_name1
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Please insert the values in the tables according to the table description.")
    print("Eg-SELECT column_name(s) FROM table1 LEFT JOIN table2 ON table1.column_name = table2.column_name;")
    print("Please use the above given TABLE DESCRIPTION to fill the column name")
    print("Please enter a common column name ")
    print("LIKE EG- Id")
    column_name=input()
    print("Please enter a condition that you would like to impose")
    print("Eg-value>8")
    condition=input()
    command="SELECT "+ column_name +" FROM "+table_name+" FULL OUTER JOIN "+table_name1+" ON "+ table_name+"."+column_name +" = "+table_name1+"."+column_name+" WHERE "+condition
    #SELECT column_name(s) FROM table1 FULL OUTER JOIN table2 ON table1.column_name = table2.column_name WHERE condition;
    cur.execute(command)
    Con.commit()
    result = cur.fetchall()
    print(result)
    print("Select 'YES' to manipulate more data,'NO' for returning to the menu")
    Output25()

def Output25():
    Output=input()
    if(Output=='YES'):
        Outer_Join()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options ")
        Output25()

def Union():
     #SELECT column_name(s) FROM table1 UNION ALL SELECT column_name(s) FROM table2;
    cur.execute("SHOW TABLES")
    tables=cur.fetchall()
    print(tables)
    print("Please enter the name of the Table 1")
    table_name=input()
    print("Please enter the name of the Table 2")
    table_name1=input()
    print("Given below is the description of the table 1 ")
    command5="DESC "+table_name
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Given below is the description of the table 2 ")
    command5="DESC "+table_name1
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Please insert the values in the tables according to the table description.")
    print("Eg-SELECT City FROM Customers UNION ALL SELECT City FROM Suppliers ORDER BY City;")
    print("Please use the above given TABLE DESCRIPTION to fill the column name")
    print("Please enter a column name from table 1 ")
    print("LIKE EG- Id")
    column_name=input()
    print("Please enter a column name from table 2 ")
    print("LIKE EG- Id")
    column_name1=input()
    print("Please enter the coloumn name in which you want to view the data")
    print("Eg-city")
    condition=input()
    command="SELECT "+ column_name +" FROM "+table_name+" UNION ALL SELECT "+column_name1+" FROM "+table_name1+" ORDER BY "+condition
    #SELECT City FROM Customers UNION ALL SELECT City FROM Suppliers ORDER BY City;
    cur.execute(command)
    Con.commit()
    result = cur.fetchall()
    print(result)
    print("Select 'YES' to manipulate more data,'NO' for returning to the menu")
    Output26()

def Output26():
    Output=input()
    if(Output=='YES'):
        Union()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options ")
        Output26()

def Aliases():
    print("Do you want to name a column or a full table")
    print("choose one option from below")
    print("1)COLUMN")
    print("2)TABLE")
    choice=input()
    print("Enter the table name that you want to choose")
    print("These are all the tables that are present")
    cur.execute("SHOW TABLES")
    tables=cur.fetchall()
    print(tables)
    table_name=input()
    print("Given below is the description of the table ")
    command5="DESC "+table_name
    command6=command5
    cur.execute(command6)
    result = cur.fetchall()
    print(result)
    print("Now choose a column name")
    column_name=input()
    print("Now choose an alias name")
    alias_name=input()
    if(choice==1):
       command=" SELECT "+column_name +" AS "+ alias_name+ " FROM " +table_name
       cur.execute(command)
       Con.commit()
       result = cur.fetchall()
       print(result)
    else:
        command1001=" SELECT "+column_name +" FROM " +table_name +" AS "+alias_name 
        cur.execute(command1001)
        Con.commit()
        result = cur.fetchall()
        print(result)
    print("Select 'YES' to manipulate more data,'NO' for returning to the menu")
    Output27()
   
def Output27():
    Output=input()
    if(Output=='YES'):
        Aliases()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options ")
        Output27()

############################################################################################################################
#                                            MISCELLANEOUS FUNCTION                                                        #       
#                                                                                                                          #
############################################################################################################################

def Miscellaneous_function():
    print("1)Extra Stuff")
    print("2)Quit")
    Output28()

def Output28():
    Output=input()
    if (Output=='1'):
       Extra_Stuff()
    elif(Output=='2'):
        Quit()
    else:
        print("Please select a number given in the options")
        Output28()

def Extra_Stuff():
    print("Dear User,please type the commands so as to see what you wish")
    input_data=input()
    cur.execute(input_data)
    Con.commit()
    result = cur.fetchall()
    print(result)
    print("Select 'YES' to manipulate more data,'NO' for returning to the menu")
    Output29()

def Output29():
    Output=input()
    if(Output=='YES'):
        Aliases()
    elif(Output=='NO'):
        Menu()
    else:
        print("Please select a number given in the options ")
        Output27()
Menu()

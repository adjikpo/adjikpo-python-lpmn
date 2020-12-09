from sqlite3 import *

#Connecting to sqlite
connection = connect("base.db")

#Creating a cursor object using the cursor() method
cursor = connection.cursor()

#Doping STUDENT table if already exists.
cursor.execute("DROP TABLE IF EXISTS STUDENT")

# Create table - STUDENT
sql ='''CREATE TABLE STUDENT(
   id INTEGER AUTO_INCREMENT PRIMARY KEY, 
   firstName TEXT, 
   lastName TEXT, 
   age INTEGER
)'''
cursor.execute(sql)

# Commit your changes in the database
connection.commit()
print("Table created successfully........")


#Insert into table - STUDENT
new_student1 = (cursor.lastrowid, "Arthur", "Djikpo", 24)
cursor.execute('INSERT INTO STUDENT VALUES(?, ?, ?, ?)', new_student1)

new_student1 = (cursor.lastrowid, "Ettiènne", "Thunder", 69)
cursor.execute('INSERT INTO STUDENT VALUES(?, ?, ?, ?)', new_student1)

# Commit your changes in the database
connection.commit()
print("Records inserted........")

#Retrieving data
my_student=(1,)
cursor.execute('''SELECT * FROM STUDENT WHERE id=?''',my_student)

#Fetching a row from the table
print(cursor.fetchone())

#Updating a row from the table 
update_student = ('Euttiènne', "CrespiThunder", 69, 1)
cursor.execute('''UPDATE STUDENT SET firstName=?, lastName=?, age=? WHERE id=?''', update_student)


# Commit your changes in the database
connection.commit()
print("Table updated...... ")

#Fetching all the rows after the update
print("Contents of the Student table after the update operation: ")
cursor.execute('''SELECT * FROM STUDENT''')
print(cursor.fetchall())

#Deleting records
cursor.execute('''DELETE FROM STUDENT WHERE age > 25''')

# Commit your changes in the database
connection.commit()
print("Table updated after delete...... ")

#Retrieving data after delete
print("Contents of the table after delete the old student ")
cursor.execute("SELECT * from STUDENT")
print(cursor.fetchall())

#Doping STUDENT table if already exists
cursor.execute("DROP TABLE STUDENT")

# Commit your changes in the database
connection.commit()
print("Table dropped... ")

#Closing the cursor & the connection
cursor.close()
connection.close()
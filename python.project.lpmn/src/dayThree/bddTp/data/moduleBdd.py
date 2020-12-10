from sqlite3 import *

#Connecting to sqlite
connection = connect("base.db")

#Creating a cursor object using the cursor() method
cursor = connection.cursor()

#Doping ALL table if already exists.
cursor.execute("DROP TABLE IF EXISTS STUDENT")
cursor.execute("DROP TABLE IF EXISTS CURRICULUM")
cursor.execute("DROP TABLE IF EXISTS LANGUAGE")
cursor.execute("DROP TABLE IF EXISTS CURRICULUM_LANGUAGE")

print("Database was cleaned successfully........")

####################### CREATE ALL TABLE ####################################

# Create table - STUDENT
sql ='''CREATE TABLE STUDENT(
   idStudent INTEGER AUTO_INCREMENT PRIMARY KEY, 
   firstName TEXT NOT NULL, 
   lastName TEXT NOT NULL, 
   age INTEGER NOT NULL,
   idCurriculum INTEGER DEFAULT NULL,
   CONSTRAINT fk_id_curriculum FOREIGN KEY (idCurriculum) REFERENCES CURRICULUM(idCurriculum)
)'''
cursor.execute(sql)

# Commit your changes in the database
connection.commit()
print("Table STUDENT created successfully........")

# Create table - CURRICULUM
sql ='''CREATE TABLE CURRICULUM(
   idCurriculum INTEGER AUTO_INCREMENT PRIMARY KEY, 
   nameCurriculum TEXT NOT NULL
)'''
cursor.execute(sql)

# Commit your changes in the database
connection.commit()
print("Table CURRICULUM created successfully........")

# Create table - LANGUAGE
sql ='''CREATE TABLE LANGUAGE(
   idLanguage INTEGER AUTO_INCREMENT PRIMARY KEY, 
   nameLanguage TEXT NOT NULL
)'''
cursor.execute(sql)

# Commit your changes in the database
connection.commit()
print("Table LANGUAGE created successfully........")

# Create table - CURRICULUM_LANGUAGE
sql ='''CREATE TABLE CURRICULUM_LANGUAGE(
   idCurriculum INTEGER DEFAULT NULL,
   idLanguage INTEGER DEFAULT NULL,
   FOREIGN KEY (idCurriculum) REFERENCES CURRICULUM(idCurriculum),
   FOREIGN KEY (idLanguage) REFERENCES LANGUAGE(idLanguage)
   UNIQUE (idCurriculum, idLanguage)

)'''
cursor.execute(sql)

# Commit your changes in the database
connection.commit()
print("Table CURRICULUM_LANGUAGE created successfully........")


######################### ADD FUNCTIONS #####################################

def addStudent(firstname, lastname, age, curriculum):
   #Insert into table - STUDENT
   curriculumId = getIdCurriculum(curriculum)
   student = (cursor.lastrowid, firstname, lastname, age, curriculumId)
   cursor.execute('INSERT INTO STUDENT VALUES(?, ?, ?, ?, ?)', student)
   # Commit your changes in the database
   connection.commit()
   print("Records inserted........")


def addCurriculum(nameCurriculum):
   #Insert into table - CURRICULUM
   curriculum = (cursor.lastrowid, nameCurriculum)
   cursor.execute('INSERT INTO CURRICULUM VALUES(?, ?)', curriculum)
   # Commit your changes in the database
   connection.commit()
   print("Records inserted........")

def addLanguage(nameLanguage):
   #Insert into table - LANGUAGE
   language = (cursor.lastrowid, nameLanguage)
   cursor.execute('INSERT INTO LANGUAGE VALUES(?, ?)', language)
   # Commit your changes in the database
   connection.commit()
   print("Records inserted........")

def addLanguageToCurriculum(nameLanguage, nameCurriculum):
   #Insert into table - LANGUAGE
   language = getIdLanguage(nameLanguage)
   curriculum = getIdCurriculum(nameCurriculum)
   curriculum_language = (curriculum, language)

   cursor.execute('INSERT INTO CURRICULUM_LANGUAGE VALUES(?, ?)', curriculum_language)
   # Commit your changes in the database
   connection.commit()
   print("Records inserted........")

####################### GET FUNCTIONS #######################################

def getAllStudents():
   cursor.execute('''SELECT * FROM STUDENT''')

   #Fetching all row from the table
   allStudents = cursor.fetchall()
   allStudents = filter(None, allStudents)
   for i in allStudents:
      print(i[4] + ' : ' + i[1] + ' ' + i[2] + ' ' + str(i[3]) + 'yrs')   

def getOneStudent(name,age):
   #Retrieving data
   student=(name,age)
   cursor.execute('''SELECT * FROM STUDENT WHERE firstname=? AND age=?''',student)

   #Fetching a row from the table
   print(cursor.fetchone())

def getAllCurriculums():
   cursor.execute('''SELECT * FROM CURRICULUM ''')

   #Fetching all row from the table
   allCurriculums = cursor.fetchall()
   for i in allCurriculums:
      print(i[1]) 

def getOneCurriculum(name):
   #Retrieving data
   curriculum=(name,)
   cursor.execute('''SELECT * FROM CURRICULUM WHERE nameCurriculum=? ''',curriculum)

   #Fetching a row from the table
   print(cursor.fetchone())

def getOneCurriculumById(id):
   #Retrieving data
   curriculum=(id,)
   cursor.execute('''SELECT * FROM CURRICULUM WHERE idCurriculum=? ''',curriculum)

   #Fetching a row from the table
   curriculum = cursor.fetchone()
   print(curriculum)


def getAllLanguages():
   cursor.execute('''SELECT * FROM LANGUAGE ''')

   #Fetching all row from the table
   allLanguages = cursor.fetchall()
   for i in allLanguages:
      print(i[1]) 

def getOneLanguage(name):
   #Retrieving data
   language=(name,)
   cursor.execute('''SELECT * FROM LANGUAGE WHERE nameLanguage=? ''',language)

   #Fetching a row from the table
   print(cursor.fetchone())

def getOneLanguageById(id):
   #Retrieving data
   language=(id,)
   cursor.execute('''SELECT * FROM LANGUAGE WHERE idLanguage=? ''',language)

   #Fetching a row from the table
   language = cursor.fetchone()
   print(language)
   # for x in language:
   #    print(x[1])

def getIdLanguage(name):
   language=(name,)
   cursor.execute('''SELECT idLanguage FROM LANGUAGE WHERE nameLanguage=? ''',language)

   #Fetching a row from the table
   idLanguage = cursor.fetchone()
   return idLanguage[0]

def getIdCurriculum(name):
   curriculum=(name,)
   cursor.execute('''SELECT idCurriculum FROM CURRICULUM WHERE nameCurriculum=? ''',curriculum)

   #Fetching a row from the table
   idCurriculum = cursor.fetchone()
   return idCurriculum[0]

def getIdStudent(firstname, lastname):
   student=(firstname,lastname)
   cursor.execute('''SELECT idStudent FROM STUDENT WHERE firstname=? AND lastname=? ''',student)

   #Fetching a row from the table
   idStudent = cursor.fetchone()
   return idStudent[0]

####################### UPDATE FUNCTION #######################################

def updateStudent(firstname, lastname, age, idStudent):
   update_student = (firstname, lastname, age, idStudent)
   cursor.execute('''UPDATE STUDENT SET firstName=?, lastName=?, age=? WHERE idStudent=?''', update_student)
   # Commit your changes in the database
   connection.commit()
   print("Table STUDENT updated...... ")

def updateCurriculum(nameCurricullum,idCurriculum):
   update_curriculum = (nameCurricullum, idCurriculum)
   cursor.execute('''UPDATE CURRICULUM SET nameCurriculum=? WHERE idCurriculum=?''', update_curriculum)
   # Commit your changes in the database
   connection.commit()
   print("Table CURRICULUM updated...... ")

def updateLanguage(nameLanguage,idLanguage):
   update_language = (nameLanguage, idLanguage)
   cursor.execute('''UPDATE LANGUAGE SET nameLanguage WHERE idLanguage=?''', update_language)
   # Commit your changes in the database
   connection.commit()
   print("Table LANGUAGE updated...... ")


####################### DELETE FUNCTION #######################################

def deleteOneStudent(firstname, lastname):
   idStudent = getIdStudent(firstname,lastname)
   delete_student = (idStudent,)

   #Deleting records
   cursor.execute('''DELETE FROM STUDENT WHERE idStudent=?''', delete_student)

   # Commit your changes in the database
   connection.commit()
   print("Table updated after delete...... ")

def deleteOneCurriculum(name):
   idCurriculum = getIdCurriculum(name)
   delete_curriculum = (idCurriculum,)
   #Deleting records
   cursor.execute('''DELETE FROM CURRICULUM WHERE idCurriculum=?''',delete_curriculum)

   # Commit your changes in the database
   connection.commit()
   print("Table updated after delete...... ")

def deleteOneLanguage(name):
   idLanguage = getIdLanguage(name)
   delete_language = (idLanguage)
   #Deleting records
   cursor.execute('''DELETE FROM LANGUAGE WHERE idLanguage=?''', delete_language)

   # Commit your changes in the database
   connection.commit()
   print("Table updated after delete...... ")


######################## ANOTHER FUNCTIONS ######################################

def getStudentsOneCurriculum(name):
   idCurriculum=getIdCurriculum(name)
   studentsOneCurriculum = (idCurriculum,)
   cursor.execute('''SELECT * FROM STUDENT WHERE idCurriculum=?''',studentsOneCurriculum)

   #Fetching all row from the table
   allStudents = cursor.fetchall()
   for i in allStudents:
      print(str(i[0]) + ' - ' + i[1] + ' ' + i[2])

def getLanguagesOneCurriculum(nameCurriculum):
   idCurriculum = getIdCurriculum(nameCurriculum)
   nameCurriculum = (idCurriculum,)
   cursor.execute('''SELECT * FROM CURRICULUM_LANGUAGE WHERE idCurriculum=?''',nameCurriculum)

   languagesId = cursor.fetchall()

   for i in languagesId :
      getOneLanguageById(i[1])

def getCurriculumOneLanguage(nameLanguages):
   idLanguage = getIdLanguage(nameLanguages)
   nameLanguages = (idLanguage,)
   cursor.execute('''SELECT * FROM CURRICULUM_LANGUAGE WHERE idLanguage=?''',nameLanguages)

   curriculumId = cursor.fetchall()

   for i in curriculumId :
      getOneCurriculumById(i[1])

####################### FIXTURES #######################################

def installFixtures():

   new_student1 = (cursor.lastrowid, "Arthur", "Djikpo", 24, 0)
   cursor.execute('INSERT INTO STUDENT VALUES(?, ?, ?, ?, ?)', new_student1)

   new_student2 = (cursor.lastrowid, "Ettiènne", "Thunder", 69, 0)
   cursor.execute('INSERT INTO STUDENT VALUES(?, ?, ?, ?, ?)', new_student2)

   new_student3 = (cursor.lastrowid, "azerty", "test", 24, 2)
   cursor.execute('INSERT INTO STUDENT VALUES(?, ?, ?, ?, ?)', new_student3)

   new_student4 = (cursor.lastrowid, "qsdfg", "test2", 69, 1)
   cursor.execute('INSERT INTO STUDENT VALUES(?, ?, ?, ?, ?)', new_student4)

   print('Students fixtures : ok ...... ')

   curriculum1 = (0, "Devops")
   cursor.execute('INSERT INTO CURRICULUM VALUES(?, ?)', curriculum1)

   curriculum2 = (1, "Dev Mobile")
   cursor.execute('INSERT INTO CURRICULUM VALUES(?, ?)', curriculum2)

   curriculum3 = (2, "Dev Python")
   cursor.execute('INSERT INTO CURRICULUM VALUES(?, ?)', curriculum3)

   print('Curriculum fixtures : ok ...... ')

   language1 = (cursor.lastrowid, "Python")
   cursor.execute('INSERT INTO LANGUAGE VALUES(?, ?)', language1)

   language2 = (cursor.lastrowid, "Java")
   cursor.execute('INSERT INTO LANGUAGE VALUES(?, ?)', language2)

   language3 = (cursor.lastrowid, "Shell")
   cursor.execute('INSERT INTO LANGUAGE VALUES(?, ?)', language3)


   print('Language fixtures : ok ...... ')


   language1 = getIdLanguage("Python")
   curriculum1 = getIdCurriculum("Devops")
   curriculum_language1 = (curriculum1, language1)

   cursor.execute('INSERT INTO CURRICULUM_LANGUAGE VALUES(?, ?)', curriculum_language1)

   language2 = getIdLanguage("Java")
   curriculum2 = getIdCurriculum("Dev Mobile")
   curriculum_language2 = (curriculum2, language2)

   cursor.execute('INSERT INTO CURRICULUM_LANGUAGE VALUES(?, ?)', curriculum_language2)

   language3 = getIdLanguage("Java")
   curriculum3 = getIdCurriculum("Devops")
   curriculum_language3 = (curriculum3, language3)

   cursor.execute('INSERT INTO CURRICULUM_LANGUAGE VALUES(?, ?)', curriculum_language3)

   print('Curiculum & Language fixtures : ok ...... ')


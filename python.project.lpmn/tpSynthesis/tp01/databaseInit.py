from sqlite3 import *

#Connecting to sqlite
connection = connect("base.db")

#Creating a cursor object using the cursor() method
cursor = connection.cursor()

#Doping ALL table if already exists.
cursor.execute("DROP TABLE IF EXISTS customer")
cursor.execute("DROP TABLE IF EXISTS accountBank")
cursor.execute("DROP TABLE IF EXISTS bank")
cursor.execute("DROP TABLE IF EXISTS ACCOUNTBANK_BANK")

print("Database was cleaned successfully........")

####################### CREATE ALL TABLE ####################################

# Create table - customer
sql ='''CREATE TABLE customer(
   idCustomer INTEGER AUTO_INCREMENT PRIMARY KEY, 
   civility VARCHAR(10) NOT NULL,
   firstName TEXT NOT NULL, 
   lastName TEXT NOT NULL, 
   address TEXT NOT NULL
)'''
cursor.execute(sql)

# Commit your changes in the database
connection.commit()
print("Table customer created successfully........")

# Create table - accountBank
sql ='''CREATE TABLE accountBank(
   idAccount INTEGER AUTO_INCREMENT PRIMARY KEY, 
   sold INTEGER NOT NULL,
   overdrawn INTEGER NOT NULL,
   idCustomer INTEGER NOT NULL,
   idBank INTEGER NOT NULL,
   CONSTRAINT fk_id_customer FOREIGN KEY (idCustomer) REFERENCES customer(idCustomer)
   CONSTRAINT fk_id_bank FOREIGN KEY (idBank) REFERENCES bank(idBank)

)'''
cursor.execute(sql)

# Commit your changes in the database
connection.commit()
print("Table accountBank created successfully........")

# Create table - bank
sql ='''CREATE TABLE bank(
   idBank INTEGER AUTO_INCREMENT PRIMARY KEY, 
   nameBank TEXT NOT NULL
)'''
cursor.execute(sql)

# Commit your changes in the database
connection.commit()
print("Table bank created successfully........")

######################### ADD FUNCTIONS #####################################

def addCustomer(civility, firstname, lastname, address):
   #Insert into table - customer
   customer = (cursor.lastrowid,civility, firstname, lastname, address)
   cursor.execute('INSERT INTO customer VALUES(?, ?, ?, ?, ?)', customer)
   # Commit your changes in the database
   connection.commit()
   print("Records inserted........")


def addAccountBank(sold,overdrawn,idCustomer):
   #Insert into table - ACOUNTBANK
   accountBank = (cursor.lastrowid, sold,overdrawn,idCustomer)
   cursor.execute('INSERT INTO ACOUNTBANK VALUES(?, ?)', accountBank)
   # Commit your changes in the database
   connection.commit()
   print("Records inserted........")

def addBank(nameBank, idAccountBank):
   #Insert into table - bank
   bank = (cursor.lastrowid, nameBank, idAccountBank)
   cursor.execute('INSERT INTO bank VALUES(?, ?)', bank)
   # Commit your changes in the database
   connection.commit()
   print("Records inserted........")

####################### GET FUNCTIONS #######################################

def getAllCustomers():
   cursor.execute('''SELECT * FROM customer''')

   #Fetching all row from the table
   allCustomers = cursor.fetchall()
   print("Customer:")
   for i in allCustomers:
      print(i[1] + '. ' + i[2] + ' ' + i[3] + ' - ' + i[4])   

def getOneCustomer(firstname, lastname):
   #Retrieving data
   customer=(firstname, lastname)
   cursor.execute('''SELECT * FROM customer WHERE firstname=? AND lastname=?''',customer)

   #Fetching a row from the table
   print(cursor.fetchone())

def getAllAccountBank():
   cursor.execute('''SELECT * FROM accountBank ''')

   #Fetching all row from the table
   allAccountBanks = cursor.fetchall()
   print('Account in Bank')
   for i in allAccountBanks:
      print(i[1], i[2], i[3], i[4]) 

def getOneAccountBank(idAccountBank):
   #Retrieving data
   accountBank=(idAccountBank,)
   cursor.execute('''SELECT * FROM accountBank WHERE idAccountBank=? ''',accountBank)

   #Fetching a row from the table
   print( cursor.fetchone())

# def getOneAccountBankById(id):
#    #Retrieving data
#    accountBank=(id,)
#    cursor.execute('''SELECT * FROM accountBank WHERE idAccountBank=? ''',accountBank)

#    #Fetching a row from the table
#    accountBank = cursor.fetchone()
#    print(accountBank)


def getAllBanks():
   cursor.execute('''SELECT * FROM bank ''')

   #Fetching all row from the table
   allBanks = cursor.fetchall()
   print("Bank:")
   for i in allBanks:
      print(i[1]) 

def getOneBank(name):
   #Retrieving data
   bank=(name,)
   cursor.execute('''SELECT * FROM bank WHERE nameBank=? ''',bank)

   #Fetching a row from the table
   print(cursor.fetchone())

def getOneBankById(id):
   #Retrieving data
   bank=(id,)
   cursor.execute('''SELECT * FROM bank WHERE idBank=? ''',bank)

   #Fetching a row from the table
   bank = cursor.fetchone()
   print(bank)
   # for x in bank:
   #    print(x[1])

def getIdBank(name):
   bank=(name,)
   cursor.execute('''SELECT idBank FROM bank WHERE nameBank=? ''',bank)

   #Fetching a row from the table
   idBank = cursor.fetchone()
   return idBank[0]

def getIdCustomer(firstname, lastname):
   customer=(firstname,lastname)
   cursor.execute('''SELECT idCustomer FROM customer WHERE firstname=? AND lastname=? ''',customer)

   #Fetching a row from the table
   idCustomer = cursor.fetchone()
   return idCustomer[0]

####################### UPDATE FUNCTION #######################################

def updateCustomer(id, civility, firstname, lastname, address):
   update_customer = (id, civility,firstname, lastname, address)
   cursor.execute('''UPDATE customer SET civility=? ,firstName=?, lastName=?, address=? WHERE idCustomer=?''', update_customer)
   # Commit your changes in the database
   connection.commit()
   print("Table Customer updated...... ")

def updateAccountBank(sold,overdrawn, idCustomer, idBank):
   update_AccountBank = (sold,overdrawn, idCustomer, idBank)
   cursor.execute('''UPDATE accountBank SET sold=?, overdrawn=?, idCustomer=?, idBank=? ''', update_AccountBank)
   # Commit your changes in the database
   connection.commit()
   print("Table AccountBank updated...... ")

def updateBank(nameBank):
   update_Bank = (nameBank,)
   cursor.execute('''UPDATE bank SET nameBank''', update_Bank)
   # Commit your changes in the database
   connection.commit()
   print("Table Bank updated...... ")

####################### DELETE FUNCTION #######################################

def deleteOneCustomer(firstname, lastname):
   idCustomer = getIdCustomer(firstname,lastname)
   delete_Customer = (idCustomer,)

   #Deleting records
   cursor.execute('''DELETE FROM customer WHERE idCustomer=?''', delete_Customer)

   # Commit your changes in the database
   connection.commit()
   print("Table updated after delete...... ")

def deleteOneAccountBank(idAccountBank):
   delete_AccountBank = (idAccountBank,)
   #Deleting records
   cursor.execute('''DELETE FROM accountBank WHERE idAccountBank=?''',delete_AccountBank)

   # Commit your changes in the database
   connection.commit()
   print("Table updated after delete...... ")

def deleteOneBank(name):
   idBank = getIdBank(name)
   delete_Bank = (idBank,)
   #Deleting records
   cursor.execute('''DELETE FROM bank WHERE idBank=?''', delete_Bank)

   # Commit your changes in the database
   connection.commit()
   print("Table updated after delete...... ")

####################### ANOTHER FUNCTIONS #######################################

def addMoney(customer, accountBank, money):
   update_AccountBank = (sold,overdrawn, idCustomer, idBank)
   cursor.execute('''UPDATE accountBank SET sold=?, overdrawn=?, idCustomer=?, idBank=? ''', update_AccountBank)
   # Commit your changes in the database
   connection.commit()
   print("Table AccountBank updated...... ")
   

####################### FIXTURES #######################################

def installFixtures():

   new_customer = (1,"M", "Arthur", "Djikpo","13 rue des test")
   cursor.execute('INSERT INTO customer VALUES(?, ?, ?, ?, ?)', new_customer)
   cursor.connection.commit()

   new_customer = (2,"Mme", "Ettiènne", "Thunder", "100 pourcent rue de JeSuiSLoin")
   cursor.execute('INSERT INTO customer VALUES(?, ?, ?, ?, ?)', new_customer)
   cursor.connection.commit()

   new_customer = (3,"M", "azerty", "test", "56 rue azertyuiop")
   cursor.execute('INSERT INTO customer VALUES(?, ?, ?, ?, ?)', new_customer)
   cursor.connection.commit()

   new_customer = (4,"Mme", "azeqsd", "qss", "58bis rue azertyuiop")
   cursor.execute('INSERT INTO customer VALUES(?, ?, ?, ?, ?)', new_customer)
   cursor.connection.commit()

   print('customers fixtures : ok ...... ')

   bank = (1, "BNP")
   cursor.execute('INSERT INTO bank VALUES(?, ?)', bank)
   cursor.connection.commit()

   bank = (2, "La Poste")
   cursor.execute('INSERT INTO bank VALUES(?, ?)', bank)
   cursor.connection.commit()

   bank = (3, "LCL")
   cursor.execute('INSERT INTO bank VALUES(?, ?)', bank)
   cursor.connection.commit()

   bank = (4, "CIC")
   cursor.execute('INSERT INTO bank VALUES(?, ?)', bank)
   cursor.connection.commit()

   bank = (5, "Orange Bank")
   cursor.execute('INSERT INTO bank VALUES(?, ?)', bank)
   cursor.connection.commit()


   print('bank fixtures : ok ...... ')

   accountBank = (1, 15000, 1200, 1, 1)
   cursor.execute('INSERT INTO accountBank VALUES(?, ?, ?, ?, ?)', accountBank)
   cursor.connection.commit()

   accountBank = (2, 212, 2, 3, 2)
   cursor.execute('INSERT INTO accountBank VALUES(?, ?, ?, ?, ?)', accountBank)
   cursor.connection.commit()

   accountBank = (3, 21233, 33, 3, 1)
   cursor.execute('INSERT INTO accountBank VALUES(?, ?, ?, ?, ?)', accountBank)
   cursor.connection.commit()

   accountBank = (4, 15000, 0, 1, 5)
   cursor.execute('INSERT INTO accountBank VALUES(?, ?, ?, ?, ?)', accountBank)
   cursor.connection.commit()
   
   accountBank = (5, 12233, 43, 4, 4)
   cursor.execute('INSERT INTO accountBank VALUES(?, ?, ?, ?, ?)', accountBank)
   cursor.connection.commit()

   accountBank = (6, 15000, 123, 2, 4)
   cursor.execute('INSERT INTO accountBank VALUES(?, ?, ?, ?, ?)', accountBank)
   cursor.connection.commit()

   accountBank = (7, 15000, 50, 3, 5)
   cursor.execute('INSERT INTO accountBank VALUES(?, ?, ?, ?, ?)', accountBank)
   cursor.connection.commit()



   print('accountBank fixtures : ok ...... ')





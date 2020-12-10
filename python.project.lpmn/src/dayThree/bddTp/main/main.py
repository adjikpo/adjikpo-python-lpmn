#coding:utf-8

import sys
import os
import time

os.system('clear')

sys.path.append('..')
from data.moduleBdd import *

# Wait for 5 seconds
time.sleep(1)
os.system('clear')

def get_menu_choice():
    def print_menu():       # Your menu design here
        print(30 * "-", "TRAINING MANAGEMENT", 30 * "-")
        print("01. Add a student ")
        print("02. Add a curriculum ")
        print("03. Add a language ")
        print("04. Add a language in curriculum ")
        print("05. Show all student")
        print("06. Show all curriculum")
        print("07. Show all language")  
        print("08. Update a student")
        print("09. Update a curriculum")
        print("10. Update a language")
        print("11. Delete a student")
        print("12. Delete a curriculum")
        print("13. Delete a language")
        print("14. Show all students on a curriculum")
        print("15. Show all languages on a curriculum")
        print("16. Show currilum for a languages")
        print("-1. Install and test fixtures")      
        print("0. Exit  ")
        print(81 * "-")

    loop = True
    

    while loop:          # While loop which will keep going until loop = False
        print_menu()    # Displays menu
        choice = input("Enter your choice [1-16]: ")

        if choice == '1':
            choice = ''
            while len(choice) == 0:
                os.system('clear')
                print('01. Add a student')
                try:
                    firstName = str(input("Enter a firstname : \n"))
                    lastName = str(input("Enter a lastname : \n"))
                    age = int(input("Enter a age : \n"))

                    # print("List of Curriculum:\n{}".format(getAllCurriculums()))
                    print("List of Curriculum:\n")
                    print(getAllCurriculums())  
                    curriculum = str(input("Choose a curriculum:\n"))

                    if len(firstName) == 0:
                        print("Please enter your fistname.\n")
                        # Wait for 3 seconds
                        time.sleep(3)
                        if len(lastName) == 0:
                            print("Please enter your lastname.\n")
                            # Wait for 3 seconds
                            time.sleep(3)
                            break
                        break
                    
                    addStudent(firstName,lastName,age,curriculum)
                except ValueError:
                    print("Records not inserted........\nPlease enter a correct value for the age\n")
                    # Wait for 3 seconds
                    time.sleep(3)

                os.system('clear')
                break
            loop = True
        elif choice == '2':
            choice = ''
            while len(choice) == 0:
                os.system('clear')
                print('02. Add a curriculum')

                curriculum = str(input("Enter a curriculum : "))
                if len(curriculum) == 0:
                    print("Please enter a curriculum.\n")
                    # Wait for 3 seconds
                    time.sleep(3)
                    break

                addCurriculum(curriculum)

                os.system('clear')
                break
            
            loop = True
        elif choice == '3':
            choice = ''
            while len(choice) == 0:
                os.system('clear')
                print('Add a language')

                language = str(input("Enter a language : "))
                if len(language) == 0:
                    print("Please enter a language.\n")
                    # Wait for 3 seconds
                    time.sleep(3)
                    break
                
                addLanguage(language)
                
                os.system('clear')
                break
            
            loop = True
        elif choice == '4':
            choice = ''
            while len(choice) == 0:
                os.system('clear')
                print('Add a language in curriculum')
                
                curriculum = str(input("Enter a curriculum : "))
                language = str(input("Enter a language : "))

                print(addLanguageToCurriculum(curriculum,language))

                os.system('clear')
                break
            
            loop = True
        elif choice == '5':
            choice = ''
            while len(choice) == 0:
                os.system('clear')
                print('05. Show all students')
                
                getAllStudents()

                break
            loop = True
        elif choice == '6':
            choice = ''
            while len(choice) == 0:
                os.system('clear')

                getAllCurriculums()

                
                break
            
            loop = True
        elif choice == '7':
            choice = ''
            while len(choice) == 0:
                os.system('clear')

                getAllLanguages()

                
                break
            
            loop = True
        elif choice == '8':
            choice = ''
            while len(choice) == 0:
                os.system('clear')

                try:
                    print(getAllStudents())
                    oldFirstname = str(input("Enter the old fistname:\n"))
                    oldLastname = str(input("Enter the old lastname:\n"))

                    idStudent = getIdStudent(oldFirstname, oldLastname)

                    firstName = str(input("Enter a new firstname :\n"))
                    lastName = str(input("Enter a new lastname : \n"))
                    age = int(input("Enter a age : \n"))

                    print(updateStudent(firstName,lastName,age, idStudent))
                except ValueError:
                    print("Records not inserted........\nPlease enter a correct value for the age\n")
                    # Wait for 3 seconds
                    time.sleep(3)

                os.system('clear')
                break
            
            loop = True
        elif choice == '9':
            choice = ''
            while len(choice) == 0:
                os.system('clear')

                oldCurriculum = str(input("Enter the old curriculum name :\n"))

                idCurriculum = getIdCurriculum(oldCurriculum)

                curriculum = str(input("Enter the new curriculum name : \n"))

                print(updateCurriculum(curriculum, idCurriculum))

                os.system('clear')
                break
            
            loop = True
        elif choice == '10':
            choice = ''
            while len(choice) == 0:
                os.system('clear')

                oldLanguage = str(input("Enter the old language name :\n"))

                idLanguage = getIdLanguage(oldLanguage)

                language = str(input("Enter the new languages name : \n"))

                print(updateLanguage(language, idLanguage))
                
                os.system('clear')
                break
            
            loop = True
        elif choice == '11':
            choice = ''
            while len(choice) == 0:
                os.system('clear')
                
                print('List of students :')
                getAllStudents()
                
                print('\nDeleting a student ....\n')
                firstname = str(input("Enter the firstname:\n"))
                lastname = str(input('Enter the lastname:\n'))
                deleteOneStudent(firstname, lastname)

                os.system('clear')
                break
            
            loop = True  
        elif choice == '12':
            choice = ''
            while len(choice) == 0:
                os.system('clear')
                
                print('List of curriculums :')
                getAllCurriculums()
                
                print('\nDeleting a curriculum ....\n')
                curriculum = str(input('Enter the curriculum name:\n'))
                deleteOneCurriculum(curriculum)

                os.system('clear')
                break
            
            loop = True  
        elif choice == '13':
            choice = ''
            while len(choice) == 0:
                os.system('clear')
                
                print('List of languages :')
                getAllLanguages()
                
                print('\nDeleting a language ....\n')
                try:
                    language = str(input('Enter the language name:\n'))
                    deleteOneLanguage(language)
                except ValueError as e:
                    print(e)
                    # Wait for 1 seconds
                    time.sleep(10)

                os.system('clear')
                break
            
            loop = True
        elif choice == '14':
            choice = ''
            while len(choice) == 0:
                os.system('clear')

                print('List of curriculums :')
                getAllCurriculums()
                
                curriculum = str(input('\nChoose a curriculum :\n'))
                getStudentsOneCurriculum(curriculum)
               
                
                break
            
            loop = True
        elif choice == '15':
            choice = ''
            while len(choice) == 0:
                os.system('clear')

                print('List of curriculums :')
                getAllCurriculums()
                
                curriculum = str(input('\nChoose a curriculum :\n'))
                getLanguagesOneCurriculum(curriculum)

                
                break
            
            loop = True
        elif choice == '16':
            choice = ''
            while len(choice) == 0:
                os.system('clear')
                
                print('List of languages :')
                getAllLanguages()
                
                language = str(input('\nChoose a language :\n'))
                getCurriculumOneLanguage(language)
                
                break
            
            loop = True       
        elif choice == '-1':
            choice = ''
            while len(choice) == 0:
                os.system('clear')
                installFixtures()
                # Wait for 1 seconds
                time.sleep(1)
                os.system('clear')
                break
            
            loop = True      
        elif choice == '0':
            print("Exiting..")
            loop = False  # This will make the while loop to end
        else:
            # Any inputs other than values 1-16 we print an error message
            input("Wrong menu selection. Enter any key to try again..")
    return choice


print(get_menu_choice())
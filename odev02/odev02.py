studentList = []

def fullName(name, surname):
    nameSurnameValue = (name + " " + surname)
    return nameSurnameValue

def addList(name, surname):
    studentList.append(fullName(name, surname))

def printList(list):
    for value in list:
        print(value)

name = input("Öğrenci ismini giriniz : ")
surName = input("Öğrenci soyismini giriniz :")

addList(name, surName)

printList(studentList)
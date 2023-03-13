studentList = ["Lionel Messi", "Cristiano Ronaldo", "Mauro Icardi"]

def fullName(name, surname):
    nameSurnameValue = (name + " " + surname)
    return nameSurnameValue


# Aldığı isim soy isim ile listeye öğrenci ekleyen
def addList(name, surname):
    studentList.append(fullName(name, surname))


# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
def deleteStudent(student):
    if student in studentList:
        studentList.remove(student)
        print(f"{student} isimli öğrenci listeden silindi")
    else:
        print(f"{student} isimli öğrenci listede yok")


#Listeye birden fazla öğrenci eklemeyi mümkün kılan
def multiplyAddStudent():
    while True:
        print("Öğrenci Girişi Yapmadan Çıkmak İçin [H / h] Giriniz.")
        name = input("Öğrenci ismini giriniz : ")
        surName = input("Öğrenci soyismini giriniz :")
        if(name == "H" or name == "h"):
            break
        else:
            studentList.append(fullName(name, surName))

# Listedeki tüm öğrencileri tek tek ekrana yazdıran
def printList(list):
    for value in list:
        print(value)


# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
def findStudentNumber(student):
    if student in studentList:
        print(f"{student} isimli öğrencinin numarası : {studentList.index(student)}")
    else:
        print(f"{student} isimli öğrenci listede yok...")

# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)

# Fonksiyonların Testleri :

# findStudentNumber("Lionel Messi")
# multiplyAddStudent()

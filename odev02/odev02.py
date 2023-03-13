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



# Listedeki tüm öğrencileri tek tek ekrana yazdıran
def printList(list):
    for value in list:
        print(value)


# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan


# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)

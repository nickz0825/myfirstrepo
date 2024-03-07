grade=int(input("Enter Grade: "))
if (grade>=101):
   print("Error")
   
elif(grade>=90):
    print("A+")
elif(grade>=80):
    print("A")
elif(grade>=75):
    print("B+")
elif(grade>=70):
    print("B")
elif(grade>=65):
    print("C+")
elif(grade>=60):
    print("C")
elif(grade>=55):
    print("D+")
elif(grade>=50):
    print("D")
elif(grade>=0):
    print("F")

else:
    print("Error")

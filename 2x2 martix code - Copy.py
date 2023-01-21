print("A Program to multiply 2 x 2 matrix")
print("Entry for the first Matrix")
e11=int(input("Enter the element of First row and first column"))
e12=int(input("Enter the element of first row and second column"))
e21=int(input("Enter the element of second row and first column"))
e22=int(input("Enter the element of second row and second column"))
print("Entery for the second Matrix")
E11=int(input("Enter the element of First row and first column"))
E12=int(input("Enter the element of first row and second column"))
E21=int(input("Enter the element of second row and first column"))
E22=int(input("Enter the element of second row and second column"))
a=e11*E11+e12*E21
b=e11*E12+e12*E22
c=e21*E11+e22*E21
d=e21*E12+e22*E22
print(a ,b)
print(c,d)
Answer=a*d-c*b
print("The determinant of the given two matrices after mutiplying them is ",Answer)

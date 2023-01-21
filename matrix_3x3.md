print("For matrix A")
e11=int(input(print("Enter the element of first row and first column")))
e12=int(input(print("Enter the element of first row and second column")))
e13=int(input(print("Enter the element of first row and third column")))
e21=int(input(print("Enter the element of second row and first column")))
e22=int(input(print("Enter the element of second row and second column")))
e23=int(input(print("Enter the element of second row and third column")))
e31=int(input(print("Enter the element of third row and first column")))
e32=int(input(print("Enter the element of third row and second column")))
e33=int(input(print("Enter the element of third row and third column")))
print("For matrix B")
E11=int(input(print("Enter the element of first row and first column")))
E12=int(input(print("Enter the element of first row and second column")))
E13=int(input(print("Enter the element of first row and third column")))
E21=int(input(print("Enter the element of second row and first column")))
E22=int(input(print("Enter the element of second row and second column")))
E23=int(input(print("Enter the element of second row and third column")))
E31=int(input(print("Enter the element of third row and first column")))
E32=int(input(print("Enter the element of third row and second column")))
E33=int(input(print("Enter the element of third row and third column")))
a=e11*E11+e12*E21+e13*E31
b=e11*E12+e12*E22+e13*E32
c=e11*E13+e12*E23+e13*E33
d=e21*E11+e22*E21+e23*E31
e=e21*E12+e22*E22+e23*E32
f=e21*E13+e22*E23+e23*E33
g=e31*E11+e32*E21+e33*E31
h=e31*E12+e32*E22+e33*E32
i=e31*E13+e32*E23+e33*E33
print(a,b,c)
print(d,e,f)
j=e*i-h*f
k=d*i-g*f
l=d*h-g*e
Answer=a*j-b*k+c*l
print("The determinant of the given matrices is ",Answer)

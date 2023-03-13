from math import factorial
def pascal_tri(numRows,divisibles):
  '''Print Pascal's triangle with numRows.'''
  if (1<divisibles<numRows):
    for i in range(numRows):
        # loop to get leading spaces
        for j in range(numRows-i+1):
            print(end=" ")
        
        # loop to get elements of row i
        for j in range(i+1):
            # nCr = n!/((n-r)!*r!)
            num1= factorial(i)//((factorial(j)*factorial(i-j)))
            residuo=num1%divisibles
            if(residuo==0):
              print("1", end=" ")
            else:
              print("0", end=" ")
        # print each row in a new line
        print("\n")
  else:
    print("No se puede realizar")
n= int(input("Ingrese el numero d de filas "))
d= int(input("Ingrese el numero divisible "))
pascal_tri(n,d)

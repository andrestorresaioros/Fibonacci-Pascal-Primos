from math import factorial


def pascal_tri(numRows):
    '''Print Pascal's triangle with numRows.'''
    for i in range(numRows):
      # loop to get leading spaces
        for j in range(numRows-i+1):
            print(end=" ")
      # loop to get elements of row i
        for j in range(i+1):
            # nCr = n!/((n-r)!*r!)
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

   # print each row in a new line
        print("\n")


num = int(input("Ingrese el valor deseado "))
pascal_tri(num)

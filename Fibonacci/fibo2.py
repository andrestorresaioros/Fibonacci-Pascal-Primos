def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True
def fibonacci_iter(n,a1,a2):
    a=a1
    b=a2
    if n==1:
        print('0')
    elif n==2:
        print('0','1')
    else:
        print('0')
        print(a)
        print(b)
        for i in range(n-3):
            total = a + b
            b=a
            a= total
            if(es_primo(total)):
                print(total,"Es primo")
            else:
                print(total)
num = int(input("¿Hasta qué número quieres la lista?: "))
num2 = int(input("Ingrese el valor de A "))  
num3 = int(input("Ingrese el valor de B "))         
fibonacci_iter(num,num2,num3)
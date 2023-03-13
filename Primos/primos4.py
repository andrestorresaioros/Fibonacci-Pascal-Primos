def eratostenes(n,n2):
    primos = [True for i in range(n+1)]
    for m in range(2,n+1):
        k = 2
        while m*k <= n:
            primos[m*k] = False
            k += 1
    primos_val = []
    for m in range(2,n+1):
        if primos[m] == True:
            primos_val.append(m)
    N = len(primos_val)
    tuplas1 = []
    for i in range(N-1):
        for j in range(i+1,N):
            if primos_val[j]-primos_val[i] == 2*n2:
                tuplas1.append((primos_val[i],primos_val[j]))
    return tuplas1

num= int(input("¿Hasta qué número quieres la lista?: "))
num2= int(input("Ingrese el valor k "))
t1 = eratostenes(num,num2)
print(t1)

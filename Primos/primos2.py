comprobar = True
while comprobar:
    n1=1
    n2= int(input("¿Hasta qué número quieres la lista?: "))
    a=0
    if n1>0 and n2>0 and n1!=n2:
        comprobar=False
        if n1>n2:
            n1^=n2
            n2^=n1
            n1^=n2
        i=n1
        
        while i<=n2:
            creciente =2    
            esPrimo=True
            while esPrimo and creciente<i:
                if i% creciente ==0:
                    esPrimo = False
                else:
                    creciente+=1
            if esPrimo and not a:
                a=i
            elif esPrimo and a:
                b=i

                if b-a==2:
                    print(a,"y",b,"son primos gemelos.")
                a=i
            i+=1
    else:
        if n1==n2:
            print("los numeros son iguales. Intentelo nuevamente.")




print("***********************")
print(" Operadores lógicos")
print("***********************\n")
print("Conjunción (And)")
numero = int(input("Ingrese un número entre 2 y 5: \n"))
if numero > 2 and numero < 5:
    print("El número: ",numero,"Cumple la condición\n")
else:
    print("El número: ",numero,"no cumple la condición\n")

print("Disyunción (Or)")
palabra = input("Para cumplir la condición, escriba Si o No: \n")
palabra = palabra.upper()
if palabra == "SI" or palabra == "NO":
    print("Cumple la condición\n")
else:
    print("No Cumple la condición\n")
    
print("Negación (Not)")
valor = int(input("Ingrese valor distinto a 5: "))
if not valor == 5:
    print("Cumple la condición")
else:
    print("No cumple la condición")

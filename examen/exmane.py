# Escriba un programa que calcule el promedio de un conjunto de numeros ingresados por el usuario

suma = 0
contador = 0

while True:
    numero = input("Ingrese las notas de las cuales desea saber el promedio ('no' para finalizar la lista): ")

    if numero.lower == 'no':
        break 

    suma = numero # el error esta aqui
    contador += 1


promedio = suma / contador

print("Su nota final es: ", promedio)


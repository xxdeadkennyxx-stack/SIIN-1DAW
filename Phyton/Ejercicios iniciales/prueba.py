def calculaiva(numero):
    iva = numero * 0.21
    return iva

teclado = input("Dime un precio: ")
numero = int(teclado)
preciofinal = numero + calculaiva(numero)

resultado = calculaiva(numero)

print("El IVA es " + str(resultado))
print("El precio final es " + str(preciofinal))

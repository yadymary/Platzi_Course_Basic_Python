def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos * valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")


menu = """
Bienvenido al conversor de monedas locales a dólar estadounidense 💰

1 - Moneda Pesos Mexicanos
2 - Moneda Bitcoin
3 - Moneda Soles Peruanos

Elige una opción por favor: """

opcion = int(input(menu))
##Valores referenciales de Tipo de Cambio  de cada moneda al Día 13/11/2021 
if opcion == 1:
    conversor("mexicano", 0.049)
elif opcion == 2:
    conversor("bitcoin", 64481.184)
elif opcion == 3:
    conversor("soles", 0.24)
else:
    print('Ingresa una opción correcta por favor')

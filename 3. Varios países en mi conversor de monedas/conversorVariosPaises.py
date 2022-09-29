def conversor(tipo_pesos,valor_dolar):
    pesos = input("¿Cuantos pesos "+ tipo_pesos +" tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $"+dolares+" dolares")

menu = """
Bienvenido al conversor de monedas 💰

1 - Peso colombiano
2 - Peso argentino
3 - Peso mexicano

Elige una opcion: """

opt = int(input(menu))

if opt ==1:
    conversor("colombianos", 3875)

elif opt == 2:
    conversor("argentinos", 65)
elif opt == 3:
    conversor("mexicanos", 20)
else:
    print("Ingresa una opcion correcta porfavor")

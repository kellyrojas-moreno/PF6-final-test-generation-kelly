import requests
import json

def dish_fetch(numero):
    
    url = f"https://api-colombia.com/api/v1/TypicalDish/{numero}"
    
    response = requests.get(url)

    # Convertir en diccionario
    plato = response.json()

    return plato


if __name__ == "__main__":
    numero = int(input("Ingrese el número del plato: "))
    informacion_plato = dish_fetch(numero)
    
    print("Diccionario del plato:")
    print(informacion_plato)

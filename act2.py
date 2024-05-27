#api key = ef8754cef0e156a6f79e18aeb7980680
#api_url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es'

import requests

def obtener_datos(ciudad, api_key):
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es'
    respuesta = requests.get(api_url)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        print(f"error conectandose a la API. {respuesta.status_code}")


def mostrar_datos(datos):
    temperatura_actual = datos['main']['temp'] 
    sensacion_termica = datos['main']['feels_like']
    humedad = datos['main']['humidity']
    descripcion_clima = datos['weather']['description']

    print(f"informacion meteoroligca".center(50, '-'))
    print(f"temperatura actual: {str(temperatura_actual).rjust(30)} C°")
    print(f"sensacion termica: {str(sensacion_termica).rjust(31)} C°")
    print(f"humedad: {str(humedad).rjust(38)}")
    print(f"descripcion del clima: {descripcion_clima.rjust(25).capitalize()}")
    print("-" * 50)

def main():
    api_key = 'ef8754cef0e156a6f79e18aeb7980680'
    ciudad = input('ingresa el nombre de la coudad deseada por faovr')
    datos = mostrar_datos(ciudad, api_key)
    if datos:
        mostrar_datos(datos)

if __name__ == "__main__":
    main()

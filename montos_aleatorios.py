import json
import globales
import random

productos = ["Cafe Americano","Te Chai","Croissant","Jugo Naranja","Panini de Pavo y Queso","Pastel de Zanahoria","Espresso Doble","Batido de Frutas","Muffin","Ensalada","Chocolate Caliente","Tarta de Frambuesa","Sandwich de Huevo","Galletas de Avena","Frappe de Caramelo"]

def generar_montos_aleatorios():
    items = []
    for producto in productos:
        item = {
            "nombre": producto,
            "valor": random.randint(2000, 10000)
            
        }
        items.append(item)
    globales.guardar_archivo_json('valores.json', items)

if __name__ == "__main__":
    generar_montos_aleatorios()
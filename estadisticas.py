import json
import globales
import math

def calculo_estadistico():
    items = globales.leer_archivo_json('valores.json')
    if not items:
        print("No hay datos registrados")
        return
    
    valores = [item['valor'] for item in items]

    valor_mas_alto = max(valores)
    valor_mas_bajo = min(valores)
    promedio_valores = sum(valores) / len(valores)
    media_geometrica = math.exp(sum(math.log(valor) for valor in valores) / len(valores))

    print(f"El valor mas alto es: ${valor_mas_alto}")
    print(f"El valor mas bajo es: ${valor_mas_bajo}")
    print(f"El promedio es: ${promedio_valores:.2f}")
    print(f"La media geométrica es: ${media_geometrica:.2f}")

if __name__ == "__main__":
    calculo_estadistico()

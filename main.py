from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure,show


def caminata(campo,borracho,pasos):
    inicio=campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)
    return inicio.distancia(campo.obtener_coordenada(borracho))



def simular_caminata(pasos,intentos,tipo_de_Borracho):
    borracho=tipo_de_Borracho(nombre='Brielga')
    origen=Coordenada(0,0)
    distancias=[]
    
    for _ in range(intentos):
        campo=Campo()
        campo.anadir_borracho(borracho,origen)
        simulacion_caminata=caminata(campo,borracho,pasos)
        distancias.append(round(simulacion_caminata,1))
    return distancias


def graficar(x,y):
    grafica=figure(title='Camino aleatorio',x_axis_label='Pasos',y_axis_label='Distancia')
    grafica.line(x,y,legend='Distancia media')
    show(grafica)

def main(distancias,intentos,tipo_de_Borracho):
    distancias_media_por_caminata=[]
    for pasos in distancias:
        distancias=simular_caminata(pasos,intentos,tipo_de_Borracho)
        distancia_media=round(sum(distancias)/len(distancias),4)
        distancia_maxima=max(distancias)
        distancia_minima=min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_de_Borracho.__name__} caminata aleatoria de {pasos} ')
        print(f'Media={distancia_media}')
        print(f'Max={distancia_maxima}')
        print(f'Min={distancia_minima}')
    graficar(distancias_de_caminata,distancias_media_por_caminata)


if __name__ == '__main__':
    distancias_de_caminata=[10,100,1000,10000]
    numero_de_intentos=100 #numero de cantidades que se hara la simulacion
    main(distancias_de_caminata,numero_de_intentos,BorrachoTradicional)

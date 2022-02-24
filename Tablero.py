from turtle import color
from Ficha import *

class Tablero:
    
    #Defina aquí los atributos de Tablero

    casillas = 0
    fichas = []

    #también va a necesitar una lista de Fichas (puede asumir un número de Fichas fijo si le parece más fácil), 
    #y un mecanismo para saber quién sigue en el turno

    #agregue parámetros necesarios después de self
    #para iniciar los valores de sus atributos
    def __init__(self , casillasp , fichasp):
        self.casillas = casillasp
        self.fichas = fichasp

        #inicialice aquí todos los atributos
        #no olvide usar self.atributo para acceder el atributo de la clase

    #defina aquí los métodos de Tablero
    #recuerde que el primer parámetro de cada método es siempre self

    def turno(self):
        cambiarturno=0
        indice = 0

        #realizamos un ciclo para el juego
        while cambiarturno ==0:
            self.fichas[indice].avanzar()
            if (self.fichas[indice].posicion >= self.casillas ):
                
                fichaganadora= self.fichas[indice].__dict__
                #Esta es la manera para que me diera la ficha ganadora
                fichaganadora =fichaganadora["color"]
                print("Ficha ganadora" , fichaganadora)
                print("SE TERMINO EL JUEGO")
                return 
            else:
                
                indice = indice +1

                #Si el numero de indice se sobrepasa a la cantidad de fichas se devuelve a 0 , reiniciando la ronda
                if indice >= len(self.fichas):
                    indice=0

                else:
                    continue





    


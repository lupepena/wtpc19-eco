# Se importa la superclase de la cual hereda

from sc_animal import Animal

class Predador(Animal):
    """Subclase Predador que hereda de la superclase Animal."""
    
    def decidir(self,terreno):
        """Etapa de planificación. Observa el terreno y decide una acción pensando como predador. Si observa una presa y ésta se encuentra a una distancia inferior a su velocidad máxima, planea comerla; caso contrario, si se encuentra dentro de su rango de visión, planea perseguirla: se mueve para reducir su distancia con la presa más cercana; si tampoco cumple esta última condición, se planea moverse en alguna dirección aleatoria, una cantidad de pasos aleatorios inferior a su velocidad."""
        # Localiza a las presas visibles entre sus vecinos visibles
        vecinos_visibles = terreno.ubicar_vecinos(self)
        presas_visibles = [vecino for vecino in vecinos_visibles if vecino.get_clase() == "Presa"]
        # Si visualiza presas, calcula su distancia a ellas
        if len(presas_visibles) != 0:
            distancias_y_vecinos = {}
            for vecino in lista_vecinos:
                distancia = terreno.calcular_distancia(terreno.ubicar(self), terreno_ubicar(vecino))
                distancias_y_vecinos[distancia] = vecino
            # Determina el vecino más cercano
            distancia_menor = min(list(distancias_y_vecinos.keys()))
            vecino_mas_cercano = distancias_y_vecinos[distancia_menor]
            posicion_vecino_mas_cercano = terreno.ubicar(vecino_mas_cercano)
            # Si está más cerca que su velocidad máxima, planea comerlo (se ubica en la posición de la grilla de la presa y ésta desaparece) 
            if distancia_menor <= self.velocidad:
                terreno.mover(self, posicion_vecino_mas_cercano)
                #self.modificar_energía(valor_porcentual)
            # Si no está lo suficientemente próximo, planea perseguirlo    
            else:
                terreno.mover(self, posicion_vecino_mas_cercano)
        # En caso de no observar presas cercanas, planea moverse en una dirección random
        else:
           posicion_random = terreno.generar_posicion_random()
           terreno.mover(self, posicion_random)

    def ejecutar(self,terreno):
        """Realiza la acción del plan."""
        pass
        # Debe modificarse el método decidir() para que guarde la orden de moverse en el atributo plan y luego aquí se intereprete y se ejecute.
import random
class Persona:
    '''Creo una classe persona con metodi nome e cognome'''
    def __init__(self,a,b):
        self.nome=a
        self.eta=b
class Cubo:
    '''Creo un un oggetto cubo che abbia volume e superficie come method '''
    def __init__(self,l:float=6):
        self.lato=l

    def triple(self,x):
        return 3*x
    def sup_faccia(self):
        return self.lato**2
    def superficie(self):
        return self.sup_faccia()*6
    def volume(self):
        return self.sup_faccia()*self.lato
class Math:

    def __init__(self):
        self.lista = []
        for self.element in range(10):
            self.lista.append(random.randint(0,10))



        def mean(self):
            sum = 0
            for element in self.lista:
                sum += element
            return (sum/self.lista.len())
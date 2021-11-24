from zooAnimales.animal import Animal

class Anfibio(Animal):

    _listado = []
    ranas =0 
    salamandras =0
    def __init__(self, nombre, edad, habitat, genero,colorPiel,venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel= colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)


    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self,colorPiel):
        self._colorPiel = colorPiel

    def getVenenoso(self):
        return self._venenoso

    def setVenenoso(self,venenoso):
        self._venenoso = venenoso

    def getListado(self):
        return self._listado

    def setListado(self,listado):
        self._listado = listado
    
    @classmethod
    def crearRana(cls,nombre,edad,genero):
        cls.ranas +=1
        return Anfibio(nombre,edad,"selva",genero,"rojo",True)

    @classmethod
    def crearSerpiente(cls,nombre,edad,genero):
        return Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)

    @staticmethod
    def movimiento():
        return "saltar"
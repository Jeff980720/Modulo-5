class libro:
    cantidad_libros = 0
    def __init__(self,titulo,autor,paginas):
        self.titulo=titulo
        self.autor=autor
        self.paginas=paginas
        libro.cantidad_libros+=1

    def mostrar_info(self):
        return f"Titulo: {self.titulo} Autor: {self.autor} Paginas: {self.paginas}"
    

    @staticmethod
    def es_grande(pag):
        if pag >300:
            resp=True
        else:
            resp=False
        return resp
    
    @classmethod
    def total_libros(cls):
        return f"Se han creado {cls.cantidad_libros} libros."
    

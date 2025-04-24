class Libro:
    count_id = 0
    def __init__(self, title, author, gender):
        self.title = title
        self.author = author
        self.gender = gender
        Libro.count_id += 1
        self.id = Libro.count_id
    
    # getters
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_gender(self):
        return self.gender
    # tambien en ves de getters  podemos usar la etiqueta property
    # pero es algo que veremos en proximos sistemas tambien usaremos atributos protegidos ya que
    # hasta el momento no hemos visto attributos privados
    # @property
    # def title(self):
    #     return self.title
    
    # necesitamos una etiqueta de method para count_id
    @classmethod
    def get_total_books(cls):
        return cls.count_id
        
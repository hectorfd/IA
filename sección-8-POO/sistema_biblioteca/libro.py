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
    
    # necesitamos una etiqueta de method para count_id
    @classmethod
    def get_total_books(cls):
        return cls.count_id
        
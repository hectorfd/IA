from libro import Libro
class Biblioteca:
    def __init__(self, name_biblioteca):
        self.name_biblioteca = name_biblioteca
        self.list_books = []
    
    # metodo para agregar libros -. esta funcion es de agregación
    def add_book(self, title, author, gender):
        book = Libro(title, author, gender)
        self.list_books.append(book)
        
    # metodo para  buscar libro por author
    def search_book_by_author(self, author):
        print(f'Search by Author: {author}')
        for i in self.list_books:
            if i.get_author() == author:
                print(f'Id: {i.id}\n\t Title: {i.title}\n\t Author: {i.author}\n\t Gender: {i.gender}')
    
    # metodo para buscar libros por genero
    def search_book_by_gender(self, gender):
        print(f'Search by Gender: {gender}')
        for i in self.list_books:
            if i.get_gender() == gender:
                print(f'Id: {i.id}\n\t Title: {i.title}\n\t Author: {i.author}\n\t Gender: {i.gender}')
    
    # metodo para mostrar todos los libros
    def show_total_books(self):
        print(f'Total Books: {len(self.list_books)}')
        for i in self.list_books:
            print(f'Id: {i.id}\n\t Title: {i.title}\n\t Author: {i.author}\n\t Gender: {i.gender}')
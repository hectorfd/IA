from biblioteca import Biblioteca
print('Sistema de Biblioteca')

# nombre de la biblioteca
biblioteca = Biblioteca('Yachay Huasi')

# agregar libros al sistema

biblioteca.add_book('El viejo y el mar', 'Ernesto Hemingway', 'Fiction')
biblioteca.add_book('La guerra de dos mundos', 'Ridgely', 'science Fiction')
biblioteca.add_book('Narnia', 'Lewis', 'Adventure')
biblioteca.add_book('Juego de Tronos Danza de Dragones', 'George R.R. Martin', 'Adventure')
biblioteca.add_book('The Alchemist', 'Paulo Coelho', 'Fiction')

# mostrar  libro por autor
biblioteca.search_book_by_author('Ernesto Hemingway')

# mostrar libros por genero
biblioteca.search_book_by_gender('Fiction')

# mostrar todos los libros
biblioteca.show_total_books()

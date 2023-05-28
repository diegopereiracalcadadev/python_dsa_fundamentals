class Livro:
    def __init__(self) -> None:
        self.titulo = 'LivroEx'
        self.id = 123
        print("Livro constructor invoked")
    
    def imprime(self) -> None:
        print("Livro %s de id %d" %(self.titulo, self.id))

Livro1 = Livro()

print(type(Livro1))
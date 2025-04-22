class Aritmetica:
    #* None hara que el valor inicial de los atributos sea vacios
    def __init__(self, operando1 = None, operando2 = None):
        self.operando1 = operando1
        self.operando2 = operando2
    
    def sumar(self):
        return self.operando1 + self.operando2
        
    def restar(self):
        return self.operando1 - self.operando2
    
    
def main():
    aritmetica1 = Aritmetica(5, 7)
    print(aritmetica1.sumar())
    aritmetica2 = Aritmetica(12,16)
    print(aritmetica2.restar())
main()
    
    
    
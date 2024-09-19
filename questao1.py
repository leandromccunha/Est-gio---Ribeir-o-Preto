
class Fibonacci:
    def __init__(self,n):
        self.k_0, self.k_1 = 0, 1
        self.calcular(n)
    def calcular(self, n):
        if n == self.k_0:
            return n
        elif n == self.k_1:
            return n
        else:
            while n > self.k_1:
                k_n = self.k_1 + self.k_0
                self.k_0 = self.k_1
                self.k_1 = k_n
            if n < self.k_1:
                print("O numero não pertence a sequencia de Fibonacci")
            else:
                print("O numero pertence a sequencia de Fibonacci")
            return self.k_1
    
    

def main(): 
    n = int(input("Digite um número para avaliar se pertence a sequência de Fibonacci: "))
    fibonacci = Fibonacci(n)
   
if __name__ == "__main__":
    main()


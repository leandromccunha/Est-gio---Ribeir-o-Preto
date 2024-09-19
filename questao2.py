class Buscador:
    def __init__(self,frase):
        self.letra = "a"
        self.frase = frase
        self.procurar()
    def procurar(self):
        contador = 0
        for i in range(len(self.frase)):
            if self.frase[i].lower() == self.letra:
                contador += 1
        return contador
            

def main(): 
    frase = input("Digite uma frase: ")
    buscador = Buscador(frase)
    print(f"A letra {buscador.letra} aparece {buscador.procurar()} vezes na frase ({buscador.frase})")
if __name__ == "__main__":
    main()

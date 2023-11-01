class Pessoa:
    def __init__(self, n, i, p, c):
        self.nome = n
        self.peso = i
        self.idade = p
        self.comida = c
        self.comendo = False
        self.dormindo = False
        self.andando = False
        self.andarcomendo = False
        self.andardormindo = False

    def Andar(self):
        if self.andando == False:
            self.andando = True
            print(f"{self.nome} está andando.")
        else:
            print(f"{self.nome} já está andando.")

    def PararAndar(self):
        if self.andando:
            print(f"{self.nome} parou de andar.")
            self.andando = False
        else:
            print(f"{self.nome} não está andando.")

    def Comer(self):
        if self.comendo == False:
            self.comendo = True
            print(f"{self.nome} está comendo {self.comida}.")
        else:
            print("Já está comendo.")

    def PararComer(self):
        if self.comendo:
            print(f"{self.nome} parou de comer.")
            self.comendo = False
        else:
            print("Não tem como mandar parar de comer quem não está comendo.")

    def AndarComendo(self):
        if self.comendo == True:
            if self.andarcomendo == False:
                self.andarcomendo = True
                print("Está comendo e não pode andar.")
        else:
            print("Não está comendo.")

    def Dormir(self):
        if self.dormindo == False:
            self.dormindo = True
            print(f"{self.nome} dormiu.")
        else:
            print(f"{self.nome} já está dormindo.")

    def AndarDormindo(self):
        if self.dormindo == True:
            if self.andardormindo == False:
                self.andardormindo = True
                print("Está dormindo e não pode andar.")
        else:
            print("Não está dormindo.")

    def Acordar(self):
        if self.dormindo:
            print(f"{self.nome} acordou.")
            self.dormindo = False
        else:
            print(f"{self.nome} não está dormindo!")

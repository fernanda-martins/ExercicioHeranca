from datetime import date
class Pai:
    def __init__(self,**D): #**D é dicionário
        self.nome      = D['nome']  #atributo tem self
        self.anoNasc   = D.pop('ano',0)
        self.sexo      = D.pop('sexo','nd')
    def calcIdade(self):
        agora = date.today()  #variaveis simples
        ano   = agora.year
        idade = ano - self.anoNasc
        return idade

P1 = Pai(nome='Joana',ano=1988,sexo='F') #DICIONARIO
print(P1.nome,P1.anoNasc,P1.sexo,P1.calcIdade(),'\n')


class Mae:
    def __init__(self,*L): #*L: só um * é LISTA
        self.peso    = L[0] #posicional
        self.altura  = L[1]
    def calcIMC(self):
        IMC = self.peso / (self.altura**2)
        return round(IMC,1) # 1 casa decimal

M1 = Mae(64,1.8)  #LISTA
print(M1.calcIMC(),'\n')


class Filha(Mae,Pai): #herda
    def __init__(self,cor,comp,*L,**dic):
        super().__init__(*L) #*L é parametro da MAE, que vou acessar
        Pai.__init__(self,**dic)
        self.cabeloCor   = cor
        self.cabeloCompr = comp

F1 = Filha('castanho','medio',63,1.7,nome='Maria Felipa',ano=2000,sexo='F') #VAR SIMPLES, LISTA E DICIONARIO
print(F1.cabeloCor,F1.cabeloCompr,F1.peso,F1.altura,F1.calcIMC(),F1.calcIdade()) #calcIMC é método, precisa de ()





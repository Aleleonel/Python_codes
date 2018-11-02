class Elevador():
    def __init__(self, capacidade, total_andares):
        self.capacidade = 8
        self.ocupantes = list()
        self.total_andares = 28
        terreo = True 

    def limite_de_ocupantes(self, embarque):
        soma = 0
        soma = sum(embarque)
        self.embarque = []
        self.ocupantes = []
        if soma > self.capacidade:
            nao_embarq = soma - self.capacidade
            embarq = self.capacidade
            return self.capacidade
            while embarq != 0:
                self.ocupantes.append(1)
                embarq -= 1
            self.soma_fim = sum(self.ocupantes)                                
            return self.imprime(self.soma_fim, nao_embarq)
        else:
            self.ocupantes = []
            embarq = soma
            nao_embarq = 0
            while embarq != 0:
                self.ocupantes.append(1)
                embarq -= 1
            self.soma_fim = sum(self.ocupantes)                                             
            return self.imprime(self.soma_fim, nao_embarq)
                        
    def entra(self):
        op = 'S'
        embarque = list()
        while op != 'N':
            emb = int(input('Quantos desejam entrar? : '))
            if emb > self.capacidade:
                print(f'Capacidade maxima é de {self.capacidade} pessoas')
                emb = int(input(f'Ajuste Quantos desejam entrar para {self.capacidade} ou menos: '))
                if emb <= self.capacidade:
                    embarque.append(emb)
                    soma = sum(embarque)
                    op = 'N'
            else:
                embarque.append(emb)
                soma = sum(embarque)
                op = 'N'
                            
        return self.limite_de_ocupantes(embarque)
    
    def sair(self, ocupantes):

        self.pessoas = list()
        for i in range (len(self.ocupantes)):
            self.pessoas.append(1)
        soma = sum(self.pessoas)
        desemb = int(input('Qtos desejam descer?: '))
        if desemb > soma:
            print(f'Apenas {soma} estão no elevador')
            desemb = int(input('Qtos realmente desejam descer?: '))
            if desemb > soma:
                print(f'Apenas {soma} estão no elevador o desembarque será ajustado para numero total de pessoas presente e ficará vazio!')
                self.pessoas = []
                print(f'Elevador vazio')
            elif desemb > 0 and desemb < soma:
                while desemb > 0:
                    desemb -= 1
                    self.pessoas.pop(1)                    
                soma = sum(self.pessoas)
                print(f'Restaram apenas {soma} pessoas no elevador')
            elif desemb == soma:
                    self.pessoas = []
                    print(f'O elevador está vazio')
            else:
                if desemb == 0:
                    desemb = int(input('Seleciona um numero maior que 0: '))
                    soma = sum(self.pessoas)

        elif desemb > 0 and desemb < soma:
                while desemb > 0:
                    desemb -= 1
                    self.pessoas.pop(1)                    
                soma = sum(self.pessoas)
                print(f'Restaram apenas {soma} pessoas no elevador')
        else:
            if desemb == soma:
                self.pessoas = []
                print(f'O elevador está vazio')                       
        
    def imprime(self, soma_fim, nao_embarq):
        if nao_embarq == 0:
            print(f'{self.soma_fim} embarcaram com sucesso')
        else:
            print(f'Limite maximo de 8 pessoas, apenas {self.soma_fim} embarcaram, Capacidade excedida em {nao_embarq} pessoas ')

    def sobe(self):

        terreo = True
        andar_atual = 0
        andar = 0
        sb = 'S'
        while andar == 0:
            if andar == 0:
                print(f'Andar atual Terreo')
                andar_atual = 0
                terreo = True
            andar = int(input('Digite o Andar desejado: '))
            if terreo is True and andar != andar_atual and andar <= self.total_andares:
                andar_atual = andar
                print(f'Você subiu até o andar {andar_atual}')
                terreo = False
                while terreo is False:
                    andar = int(input('Digite o Andar desejado: '))
                    if andar != andar_atual and  andar > andar_atual and andar <= self.total_andares:
                        andar_atual = andar
                        terreo = False
                        print(f'Você subiu para o andar {andar_atual}')
                    elif andar != andar_atual and andar < andar_atual and andar != 0:
                        andar_atual = andar
                        print(f'Você desceu ao {andar_atual} andar')
                        terreo = False
                    elif andar == andar_atual and andar != 0:
                        andar_atual = andar
                        terreo = False
                        print(f'Vocẽ já se encontra no andar {andar_atual}')
                    
                    elif andar != 0 and andar > self.total_andares:
                        andar_atual = andar_atual
                        terreo = False
                        print(f'andar invalido esse elevador só vai ate o andar {self.total_andares}!')
                        print(f'seu andar atual é {andar_atual}')
                    
                    elif andar == 0:
                        andar_atual = andar
                        terreo = True
                        print(f'Você desceu ao Terreo')                 
            else:
                if andar > self.total_andares or andar == 999:
                    andar = 0
                    terreo = True
                    print(f'andar invalido esse elevador só vai ate o andar {self.total_andares}!')
                    
                    


elevator = Elevador(8, 28)
menu = 0
menu = int(input('Digite [1] para embarcar no Elevador [2] para escolher um andar [3] para desembarque [4] sair: '))
while menu != 4:
    if menu == 1:
        elevator.entra()
        menu = int(input('Digite [1] para embarcar no Elevador [2] para escolher um andar [3] para desembarque [4] sair: '))
    if menu == 2:
        elevator.sobe()
        menu = int(input('Digite [1] para embarcar no elevador [2] para escolher um andar [3] para desembarque [4] sair: '))
    elif menu == 3:
        elevator.sair(3)
        menu = int(input(f'Digite [1] para novo embarque [2] Para novo andar [4] sair: '))
    else:
        if menu == 4:
            exit

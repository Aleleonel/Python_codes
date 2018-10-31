class Elevador():
    def __init__(self, capacidade, total_andares):
        self.capacidade = capacidade
        self.ocupantes = list()
        self.total_andares = 28
        terreo = True 

    def limite_de_ocupantes(self, embarque):
        
        soma = sum(embarque)
        if soma > 8:
            nao_embarq = soma - 8
            embarq = 8
            while embarq != 0:
                self.ocupantes.append(1)
                embarq -= 1
            self.soma_fim = sum(self.ocupantes)
                        
            return self.imprime(self.soma_fim, nao_embarq)
        else:
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
            emb = int(input('Quantos pretendem entrar? : '))
            embarque.append(emb)
            op = str(input('Alguem mais deseja embarcar? [S/N]'))

        return self.limite_de_ocupantes(embarque)
    
    def sair(self, ocupantes):

        self.pessoas = list()
        for i in range (len(self.ocupantes)):
            self.pessoas.append(1)
        sm = sum(self.pessoas)            
        print(sm)
        desemb = int(input('Qtos desejam descer?: '))
        for i in self.pessoas:
            soma = sum(self.pessoas)
        if desemb > soma:
            print(f'Apenas {soma} estão no elevador')
            desemb = int(input('Qtos realmente desejam descer?: '))
            for i in self.pessoas:
                soma = sum(self.pessoas)
            if desemb > soma:
                desemb = soma
                while desemb > 1:
                    desemb -= 1
                    self.pessoas.pop(1)                    
                soma = sum(self.pessoas)
                if soma == 1:
                    self.pessoas = []  
                    soma = 0 
                print(f'Elevador vazio')
            elif desemb < soma:
                while desemb >= 1:
                    desemb -= 1
                    self.pessoas.pop(1)                    
                soma = sum(self.pessoas)
                print(f'Restaram apenas {soma} pessoas no elevador')                       
        else:
            if desemb == 1:
                self.pessoas.pop(1)
                soma = sum(self.pessoas)
                print(f'Restam {soma} pessoas no elevador')
            else:
                while desemb > 1:
                    desemb -= 1
                    self.pessoas.pop(1)
                    soma = sum(self.pessoas)
                print(f'Restam {soma} pessoas no elevador')
    
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
                if andar > self.total_andares:
                    andar = 0
                    terreo = True
                    print(f'andar invalido esse elevador só vai ate o andar {self.total_andares}!')
                    
                    


elevator = Elevador(8, 30)
menu = int(input('Digite [1] para entrar no Elevador: '))
if menu == 1:
    elevator.entra()
    menu = int(input('Digite [2] para escolher um andar: '))
if menu == 2:
    elevator.sobe()
elif menu == 3:
     elevator.sair(3)

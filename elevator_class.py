class Elevador():
    def __init__(self, capacidade, total_andares):
        self.capacidade = capacidade
        self.ocupantes = list()
        self.total_andares = total_andares
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
            print(f'Limite maximo de 8 pessoas, {self.soma_fim} embarcaram e {nao_embarq} não puderam embarcar')
        else:
            embarq = soma
            nao_embarq = 0
            while embarq != 0:
                self.ocupantes.append(1)
                embarq -= 1
            self.soma_fim = sum(self.ocupantes)
            print(f'Limite maximo de 8 pessoas, {self.soma_fim} embarcaram')
                        

    def entra(self):
        op = 'S'
        embarque = list()
        while op != 'N':
            emb = int(input('Quantos pretendem entrar? : '))
            embarque.append(emb)
            op = str(input('Alguem mais deseja embarcar? [S/N]'))
        return self.limite_de_ocupantes(embarque)
    
    def imprime(self, soma_fim):
        print(f'{self.soma_fim} embarcaram com sucesso')






class Nao_usada():

    def sobe():

        terreo = True
        andar_atual = 0
        andar = 0
        sb = 'S'
        while andar == 0:
            if andar == 0:
                print(f'Andar atual Terreo')
            andar = int(input('Digite o Andar desejado: '))
            if terreo is True and andar != andar_atual and andar < 28:
                andar_atual = andar
                print(f'Você subiu até o andar {andar_atual}')
                terreo = False
                while terreo is False:
                    andar = int(input('Digite o Andar desejado: '))
                    if andar != andar_atual and  andar > andar_atual and andar < 28:
                        andar_atual = andar
                        print(f'Você subiu para o andar {andar_atual}')
                    elif andar != andar_atual and andar < andar_atual and andar != 0:
                        andar_atual = andar
                        print(f'Você desceu ao {andar_atual} andar')
                    elif andar == andar_atual:
                        andar_atual = andar
                        print(f'Vocẽ já se encontra no andar {andar_atual}')
                    elif andar != andar_atual and andar == 0:
                        andar_atual = andar
                        print(f'Você desceu ao Terreo')
                        terreo = True
                    elif andar > 27:
                        print(f'andar invalido esse elevador só vai ate o andar 27!')
                    elif andar == 0:
                        terreo = True
                        print(f'Você desceu ao Terreo')
            else:
                if andar > 27:
                    print(f'andar invalido esse elevador só vai ate o andar 27!')
                    andar = andar_atual




    def sair():

        pessoas = [1, 1, 1, 1,]       
        desemb = int(input('Qtos desejam descer?: '))
        for i in pessoas:
            soma = sum(pessoas)
        if desemb > soma:
            print(f'Apenas {soma} estão no elevador')
            desemb = int(input('Qtos realmente desejam descer?: '))
            for i in pessoas:
                soma = sum(pessoas)
            if desemb > soma:
                desemb = soma
                while desemb > 1:
                    desemb -= 1
                    pessoas.pop(1)                    
                soma = sum(pessoas)
                if soma == 1:
                    pessoas = []  
                    soma = 0 
                print(f'Elevador vazio')
            elif desemb < soma:
                while desemb >= 1:
                    desemb -= 1
                    pessoas.pop(1)                    
                soma = sum(pessoas)
                print(f'Restaram apenas {soma} pessoas no elevador')
                

                
        else:
            if desemb == 1:
                pessoas.pop(1)
                soma = sum(pessoas)
                print(f'Restam {soma} pessoas no elevador')
            else:
                while desemb > 1:
                    desemb -= 1
                    pessoas.pop(1)
                    soma = sum(pessoas)
                print(f'Restam {soma} pessoas no elevador')

        return ''


elevator = Elevador(8, 30)
elevator.entra()

import random

class Perceptron():

    def __init__(self):
        self.weightFunction1=random.randrange(-1000,1000)   #Losowa waga 1 do funkcji aktywacji
        self.weightFunction2=random.randrange(-1000,1000)   #Losowa waga 2 do funkcji aktywacji    
        self.weightBias=random.randrange(-1000,1000)        #Losowa waga bias do funkcji aktywacji
        self.step=0.2       #Szybkość uczenia neuronu
        self.dataTable=[    #Dane treningowe które można pobrać z pliku bądź bazy danych. [Długość, Średnica, Rodzaj] - Obrączka bądź długopis
            [23,4,1],       #Długopis
            [18,3,1],       #Długopis
            [8,2,1],        #Długopis
            [200,30,1],     #Długopis
            [8,150,0],      #Obrączka
            [30,350,0],     #Obrączka
            [30,100,0],     #Obrączka
            [10,200,0],     #Obrączka
        ]

    def genDataTable(self):
        for row in self.dataTable:
            yield row[2]

    def neuron(self):
        #VARIABLES - ZMIENNE
        resultat=[]

        #CREATING NEURON SECTION - TWORZENIE NEURONU
        for row in self.dataTable:
            res=self.weightBias+(row[0]*self.weightFunction1)+(row[1]*self.weightFunction2)
            if res>0:
                resultat.append([row[0],row[1],0])
            elif res<0:
                resultat.append([row[0],row[1],1])
        return resultat

    def training(self):
        #VARIABLES - ZMIENNE
        counter=0       #Licznik poprawnych outputów
        counter2=0      #Licznik ilości treningów
        
        #PRINT SECTION - POKAŻ NEURON
        print('Neuron before traning:')
        for i in self.neuron():
            print(i)

        #TRAINING SECTION - TRENOWANIE
        while counter<len(self.dataTable):
            gen=self.genDataTable()
            tabelaResulatat=self.neuron()

            counter2+=1
            counter=0
            for row in tabelaResulatat:
                correct=next(gen)
                if row[2] == correct:
                    counter+=1
                else:
                    if row[2]==1:
                        self.weightFunction1=self.weightFunction1+(self.step*1*row[0])
                        self.weightFunction2=self.weightFunction2+(self.step*1*row[1])
                        self.weightBias=self.weightBias+(self.step*1*row[1])
                    elif row[2]==0:
                        self.weightFunction1=self.weightFunction1+(self.step*-1*row[1])
                        self.weightFunction2=self.weightFunction2+(self.step*-1*row[1])
                        self.weightBias=self.weightBias+(self.step*-1*row[1])
        
        #PRINT SECTION - POKAŻ NEURON
        print('Numbers of training:',counter2)
        print('Neuron after training:')
        for i in self.neuron():
            print(i)
        

if __name__=='__main__':
    perceptron=Perceptron()
    perceptron.training()
    
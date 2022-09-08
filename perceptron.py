import random

class Perceptron():
    def __init__(self, dataTable):                          #dataTable - lista w liście(im więcej tym lepiej)
        self.weightFunction1=random.randrange(-1000,1000)   #Losowa waga 1 do funkcji aktywacji
        self.weightFunction2=random.randrange(-1000,1000)   #Losowa waga 2 do funkcji aktywacji    
        self.weightBias=random.randrange(-1000,1000)        #Losowa waga bias do funkcji aktywacji
        self.step=0.2                                       #Szybkość uczenia neuronu 
        self.dataTable=dataTable                            #Dane treningowe [Długość, Średnica, Rodzaj] - Obrączka bądź długopis

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
        
    def use(self, input1, input2):
        #FUNCTION ACTIVATION SECTION
        output=self.weightBias+(input1*self.weightFunction1)+(input2*self.weightFunction2)

        #PRINT SECTION - POKAŻ OUTPUTA
        if output>0:
            print('Output from neuron: 0')
        elif output<0:
            print('Output from neuron: 1')


if __name__=='__main__':
    #EXAMPLE
    perceptron=Perceptron([
            [23,4,1],
            [18,3,1],
            [8,2,1],
            [200,30,1],
            [8,150,0],
            [30,350,0],
            [30,100,0],
            [10,200,0],
        ])
    perceptron.training()
    perceptron.use(200,35)
    
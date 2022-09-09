import random

class Perceptron():
    def appendVariables(self,step=0.2):
        #VARIABLES - ZMIENNE
        self.weightFunction1=random.randrange(-1000,1000)   #WEIGHT FUNCTION ACTIVATION 1 - WAGA FUNKCJI AKTYWACJI 1
        self.weightFunction2=random.randrange(-1000,1000)   #WEIGHT FUNCTION ACTIVATION 2 - WAGA FUNKCJI AKTYWACJI 2
        self.weightBias=random.randrange(-1000,1000)        #WEIGHT FUNCTION ACTIVATION BIAS - WAGA FUNKCJI AKTYWACJI BIAS
        self.step=step                                      #STEP - KROK

    def appendDataTable(self,dataTable):
        #VARIABLES - ZMIENNE
        self.dataTable=dataTable    #TRAINIG DATA - DANE TREINIGOWE

    def genDataTable(self):
        #GENERATOR
        for row in self.dataTable:
            yield row[2]

    def neuron(self):
        #VARIABLES - ZMIENNE
        resultat=[]

        #CREATING NEURON - TWORZENIE NEURONU
        for row in self.dataTable:
            res=self.weightBias+(row[0]*self.weightFunction1)+(row[1]*self.weightFunction2)
            if res>0:
                resultat.append([row[0],row[1],0])
            elif res<0:
                resultat.append([row[0],row[1],1])
        return resultat

    def training(self):
        #VARIABLES - ZMIENNE
        self.counter1=0      #COUNTER GOOD OUTPUT - LICZNIK DOBRYCH OUTPUTÓW
        self.counter2=0      #COUNTER TRAINING - LICZNIK TRENINGÓW

        #TRAINING - TRENOWANIE
        while self.counter1<len(self.dataTable):
            gen=self.genDataTable()
            tabelaResulatat=self.neuron()

            self.counter2+=1
            self.counter1=0
            for row in tabelaResulatat:
                correct=next(gen)
                if row[2] == correct:
                    self.counter1+=1
                else:
                    if row[2]==1:
                        self.weightFunction1=self.weightFunction1+(self.step*1*row[0])
                        self.weightFunction2=self.weightFunction2+(self.step*1*row[1])
                        self.weightBias=self.weightBias+(self.step*1*row[1])
                    elif row[2]==0:
                        self.weightFunction1=self.weightFunction1+(self.step*-1*row[1])
                        self.weightFunction2=self.weightFunction2+(self.step*-1*row[1])
                        self.weightBias=self.weightBias+(self.step*-1*row[1])
        return self.counter2
        
    def use(self, input1, input2):
        #FUNCTION ACTIVATION - FUNKCJA AKTYWACJI
        output=self.weightBias+(input1*self.weightFunction1)+(input2*self.weightFunction2)

        #PRINT OUTPUT - POKAŻ OUTPUTA
        if output>0:
            return 0
        elif output<0:
            return 1

    def getTrainingCounter(self):
        #RETURN COUNTER - ZWRÓC LICZNIK
        return self.counter2
    
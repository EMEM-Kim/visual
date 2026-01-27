from abc import ABC, abstractmethod

class vendingMachine(ABC):
    def __init__(self,)
        

    def serve(self,):
        self.insertmoney()
        self.verification()
        self.making()
        self.dispense()
        self.change()

    def insertmoney():
        print("돈 투입")
    
    def verification():
        print("검증")
    
    def prepare(self):
        pass

    def dispense():
        print("제품 배출")

    def change():

class coffevendingmachine(vendingMachine):
    def __init__(self):


    def prepare(self):
        print("")
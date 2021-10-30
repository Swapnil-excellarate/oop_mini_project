A=[]
addModels=[]
sellCar=[]
class Carinfo:

    def __init__(self) -> None:
        self.stock=10
        

    def Display_data(self, companyname, model, milege, type):
        self.companyname=companyname
        self.model=model
        self.milege=milege
        self.type=type

        print("""Here is all the infomation of audi car
        Car Name= {}
        Model Numbr = {}
        Milege = {}
        Type of car= {}""".format(self.companyname, self.model, self.milege, self.type))
    
    def Input_stock(self):    
        self.input=int(input("Enter how much stock is available"))
        A.append(self.input)
        return A
    
    def New_model(self):
        self.add_model=input("Add new model")
        addModels.append(self.add_model)
        self.add_stock=int(input("Enter the new added stock :- "))
        A.append(self.add_stock)
        return addModels, A

class Coustmer:
    def shareinfo(self):
        self.carName=input("Enter the car name :- ")
        sellCar.append(self.carName)
        self.carModel=input("Enter the car model :- ")
        sellCar.append(self.carModel)
        self.year=int(input("Enter model year :- "))
        sellCar.append(self.year)
        self.companyName=input("Enter company name :- ")
        sellCar.append(self.companyName)


    def buyNewcar(self):
        self.carName=input("Enter which car you want to buy :- ")
        self.carModel=input("Enter which model you want to buy :- ")
        for i in addModels:
            if i==self.carModel:
                print(""" Here is some stock information 
                Model Name = {} and {} car are available""".format(self.carModel, A))
            else:
                print("Stock is not available, wait for sometime")
        if len(addModels)!=0:


            if self.carModel==addModels[0]:
                
                print("congratulation for new brand new car")
                remaining_cars=A[0]-1
                A.pop()
                A.append(remaining_cars)
                return A
            else:
                print("Model is not available, You should wait or book your car")
        else:
            print('Not available')


class Show:
    def Display_stock(self):
        if A[0]<=0:
            print("No stock available")
        else:
            print(A) 
    
    def Display_model(self):
        print(addModels)

    def SecondHand_carinfo(self):
        print(sellCar)

#c1=carinfo()
#c1.Display_data('audi', 'a1', 12, 'petrol')    
#c1.Display_model(c1.Display_stock())

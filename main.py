from util import A, Carinfo, Coustmer, Show


def main():
    while True:


        c1=Carinfo()
        c2=Coustmer()
        c3=Show()
        print("""
        1. If you are coustmer :-
        2. If you are showroom staff :- 
        3. To quit 
        """)
        category=int(input("Enter your authentication :- "))

        if category==1:

            print("""
            1. Display infomation.
            2. Buy brand new car.
            3. Sell your car to us.
            4. Check secondhand car.
            5. Display models.
            """)

            choise=int(input("Enter your choise :-"))
        
            if choise==1:
                c1.Display_data('audi', 'A1', 12, 'petrol')
            elif choise==2:
                c2.buyNewcar()
            elif choise==3:
                c2.shareinfo()
            elif choise==4:
                c3.SecondHand_carinfo()
            elif choise==5:
                c3.Display_model()
            elif choise==6:
                print("stop execution")
                break
            else:
                print('Invalid Choise, please enter valid choise')
        elif category==2:
            print("""
            1. Display Seconhand car stock :-
            2. Add new car model in list :- 
            3. Add total car in stock :- 
            4. Display stock
            5. Quit
            """)
            choise=int(input("Enter your choise :-"))

            if choise==1:
                c3.SecondHand_carinfo()
            elif choise==2:
                c1.New_model()
            elif choise==3:
                c1.Input_stock()
            elif choise==4:
                c3.Display_stock()
            elif choise==5:
                print('stop execution')
                break
        elif category==3:
            print('stop execution')
            break
        else:
            print("wrong choise")
            


if __name__=='__main__':
    main()

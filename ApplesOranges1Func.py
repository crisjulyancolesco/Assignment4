print("Welcome to Fruity store!")

def GetInputs():
    print("The price of an Apple is 20 pesos.")
    ApplesFunction = int(input("How many Apple/s would you like to buy? "))
    print("The price of an Orange is 25 pesos.")
    OrangesFunction = int(input("How many Orange/s would you like to buy? "))
    return ApplesFunction, OrangesFunction

def GetAmount(AmountFunction):
    print(f"The total amount is {AmountFunction} pesos.")

Apples, Oranges = GetInputs()

GetAmount(Apples*20+Oranges*25)
print("Hi! Im your Apple assistant for today!")

def GetInputs():
    AmountFunction = int(input("How much is your money? "))
    PriceFunction = int(input("What is the price of an Apple? "))
    return AmountFunction, PriceFunction

def GetOutput(QuantityFunction, ChangeFunction):
    print(f"You can buy {QuantityFunction} apples and your change is {ChangeFunction} pesos.")

Amount, Price = GetInputs()

GetOutput(Amount//Price, Amount-Amount//Price*Price)
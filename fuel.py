#This section is all variables
fuelno = input("How much fuel was bought? ")
fuelprice = input("How much does fuel cost (in cents)? ")
storepurchase = input()
fueltemp = fuelno * fuelprice
grossprice = fueltemp * storepurchase
changeorno = 0
changegiven = input()
DisBarcode = input()
barvalid = 0

#function that calculates the discounted fuel cost
def DiscountRun():
    if storepurchase < 10:
        fueltemp = (fuelprice - 5) * fuelno
    elif storepurchase > 10 and storepurchase < 50:
        fueltemp = (fuelprice - 7.5) * fuelno
    else:
        fueltemp = fuelprice - 10 * fuelno


# function that checks whether the discount barcode is valid
def BarcodeValid():
    if len(DisBarcode) == 8:
        print("Discount Accepted")
        barvalid = 1
    else:
        print("Unaccepted discount")
        barvalid = 0


if barvalid == 1:
    DiscountPrice
    print(grossprice)

if changeorno == 0:
    if changegiven > grossprice:
        changereturned = changegiven - grossprice
    else:
        print("Not enough money.")


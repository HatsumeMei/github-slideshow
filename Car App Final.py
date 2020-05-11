# Car Sales

# Welcome Message
# Get vehicle type
# Get extra options
# Calculate discounts/total
# Output total

def outputWelcomeMessage():
    print("Welcome to Kirsten's Car Shop")

def getVehicleType():
    userVehicleChoice = None

    print("Which type of vehicle would you like to purchase? ")
    print("1. Car")
    print("2. Truck")
    print("3. SUV")

    while userVehicleChoice == None or userVehicleChoice <= 0 or userVehicleChoice > 3:
        try:
            userVehicleChoice = int(input())
        except:
            print("Please enter a valid number (1-3)")
            continue

        if userVehicleChoice == 1:
            return "car"
        elif userVehicleChoice == 2:
            return "truck"
        elif userVehicleChoice == 3:
            return "SUV"
        elif userVehicleChoice == 99:
            return "batmobile"
        elif userVehicleChoice == 88:
            return "Delorean"
        else:
            print("Please enter a valid number (1-3)")


def getVehicleOptions():
    optionsList = {}
    userOptionsChoice = None

    print("What additionl options would you like to add?")
    print("0. None")
    print("1. Engine package")
    print("2. Exhaust package")
    print("3. Interior package")
    print("4. Exterior package")

    while True:
        try:
            userOptionsChoice = int(input())
        except:
            print("Please enter a valid number (0-4)")
            continue

        if userOptionsChoice == 0:
            return optionsList
        elif userOptionsChoice == 1:
            optionsList.update(Engine = 1000)
        elif userOptionsChoice == 2:
            optionsList.update(Exhaust = 800)
        elif userOptionsChoice == 3:
            optionsList.update(Interior = 300)
        elif userOptionsChoice == 4:
            optionsList.update(Exterior = 400)
        else:
            print("Please enter a valid number (0-4)")

        print("Would you like any additional options? ")


def calculateTotal(discountType, vehicleType, optionsList):

    totalAmount = 0
    discountAmount = 0

    if vehicleType == "car":
        totalAmount += 2000
    elif vehicleType == "truck":
        totalAmount += 4000
    elif vehicleType == "SUV":
        totalAmount += 5000
    elif vehicleType == "batmobile":
        totalAmount += 500000
    elif vehicleType == "delorean":
        totalAmount += 8800

    if len(optionsList) != 0:
        for k,v in optionsList.items():
            totalAmount += v

    if discountType == "v":
        discountAmount = 0.2
        totalAmount = totalAmount * discountAmount
    elif discountType  == "e":
        discountAmount = 0.15
        totalAmount = totalAmount * discountAmount
    
    return totalAmount, discountAmount

def outputTotal(vehicleChoice, optionChoice, totalAmount, discountAmount):
    print("Here is the total: $" + str(totalAmount) + " including a " + str(discountAmount * 100) + "% discount")
    print("You chose a " + vehicleChoice)
    if len(optionChoice) != 0:
        print("With the following options:")
        for k,v in optionChoice.items():
            print(k)

    print("Thank you for shopping with us!")
    

vehicleChoice = None
optionChoice = None
totalAmount = None
discountAmount = None
userExit = False

outputWelcomeMessage()

while userExit == False:
    vehicleChoice = getVehicleType()
    print(vehicleChoice)
    optionChoice = getVehicleOptions()
    print(optionChoice)

    discountType = input("Are you a (V)eteran, or an (E)mployee (or n for none)? ")

    while True:
        if discountType.lower() == "v":
            totalAmount, discountAmount = calculateTotal("v", vehicleChoice, optionChoice)
            break
        elif discountType.lower() == "e":
            totalAmount, discountAmount = calculateTotal("e", vehicleChoice, optionChoice)
            break
        elif discountType.lower() == "n" or discountType.lower() == "none":
            totalAmount, discountAmount = calculateTotal("n", vehicleChoice, optionChoice)
            break
        else:
            discountType = input("Please enter v (for veteran), e (for employee), or none? ")

    print(str(totalAmount))
    print(str(discountAmount * 100) + "%")
    outputTotal(vehicleChoice, optionChoice, totalAmount, discountAmount)

    userExitChoice = input("Would you like to purchase another vehicle?")

    if userExitChoice.lower() == "n" or userExitChoice.lower() == "no":
        userExit = True

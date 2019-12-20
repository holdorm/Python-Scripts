def bmi():
        a = float(input("Enter your height in metres:"))
        b = float(input("Enter your weight in kilograms:"))
        bmu = (b/(a**2))
        if (0 <= bmu < 18.5):
                print("You are underweight, your bmi is " + str(b/(a**2)))
        elif (18.5 <= bmu < 25):
                print("You are healthy, your bmi is " + str(bmu))
        elif (bmu >= 25):
                print("You are overweight, your bmi is " + str(bmu))
        elif (bmu < 0):
                print("You are a helium balloon")
        else:
                print("wtf")

bmi()

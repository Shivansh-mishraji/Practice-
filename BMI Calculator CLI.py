print("=" * 10 + " BMI Calculator " + 10 * "=")
while True:
    try:
            
        height = float(input("Enter your height in cm :"))
        if height <=0:
            print("Not Valid less than 0. \nEnter Height again. ")
            continue
        weight = float (input ("Enter your weight in Kg :"))
        if weight <=0:
            print("Not Valid less than 0. \nEnter Weight again ")
            continue
        else:
            bmi= weight/((height/100)**2)
            if bmi<18.5:
                category="Underweight"
            elif bmi<25:
                category = "Normal"
            elif bmi < 30:
                category= "Overweight "
            else :
                category= "obesse"
            
            print("="*20,"BMI REPORT Start",20*"=")
            print(f"Height:{height}")
            print(f"Weight:{weight}")
            print(f"BMI Value:{bmi:.2f}")
            print(f"Category:{category}")

            if category == "Normal":
                print("You Health is Good")
            else:
                print(" Need to Consult with Health Professional")
            print("="*20,"BMI REPORT End",20*"=")
            print()
    except ValueError:
            print("Friendly error : cannot type letters in place of numerical value")
                 
            
                
    choice = input("Press Y/y to Continue \nor \nelse press any key to end :")
    if choice in("Y","y"):
        continue
    else:
        break




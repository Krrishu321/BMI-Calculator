def classify_bmi(bmi):
    if bmi > 0:
       if bmi <16:
        print('You Are Severely Underweight')
       elif bmi <17:
        print("You Are Moderately Underweight")
       elif bmi <18.5:
        print("You Are Underweight")
       elif bmi <25:
        print("You are Healthy")
       elif bmi<30:
        print("You are Overweight")
       elif bmi<35:
        print("You Are Moderately Obese")
       elif bmi<=40:
        print("You Are Severely obese")
       elif bmi>40:
        print("You Are Morbidly obese")
    else:
     print("The Information That you put in is Incorrect:-")

def calculate_bmi(weight,height):
     h2=height*height
     w=weight
     bmi = (w /h2)*703
     return bmi  
def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight,height)
    category = classify_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")
main()
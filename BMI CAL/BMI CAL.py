name = str(input('Name:'))

gender = str(input('He/She:'))

age = int(input('Age:')) 

height = float(input('Height in meters: ')) # 1.02 m for avg 4 year old boy

weight = float(input('Weight in Kgs: ')) # 20.5 kgs for avg 4 year old boy

bmi = weight/(height**2)

BMITwoDecimal= round(bmi, 2) 

print('BMI =',BMITwoDecimal)

BMITwoDecimal = str(BMITwoDecimal)

def BMIresult(name,BMITwoDecimal):
    if bmi<16:                       
        print('BMI of ' +name +" is " +BMITwoDecimal+ " is Severely Underweight.".format(name,BMITwoDecimal))
    elif bmi>=16 and bmi<18.5:        
        print('BMI of ' +name +" is " +BMITwoDecimal+ " is Underweight.".format(name,BMITwoDecimal))
    elif bmi>=18.5 and bmi<25:        
        print('BMI of ' +name +" is " +BMITwoDecimal+  "  is Healthy.".format(name,BMITwoDecimal))
    elif bmi>=25 and bmi<30:          
        print('BMI of ' +name +" is " +BMITwoDecimal+  " is Overweight.".format(name,BMITwoDecimal))
    elif bmi>=30:                     
        print('BMI of ' +name +" is " +BMITwoDecimal+  " is Obesity.".format(name,BMITwoDecimal))
        
BMIresult(name,BMITwoDecimal)

print("")

print("Calorie Consumption of child")

calories={}
calories["Milk"]=int(input("Milk:")) # 280-320 calories for avg 4 year old boy.
calories["Vegetables"]=int(input("Vegetables:")) # 110-290 calories for avg 4 year old boy.
calories["Meat"]=int(input("Meat:")) # 120-220 calories for avg 4 year old boy.
calories["Lentils"]=int(input("Lentils:")) # 140 calories for avg 4 year old boy.
calories["Egg"]=int(input("Egg:")) # 160-180 calories for avg 4 year old boy.
calories["Rice"]=int(input("Rice:")) # 144-380 calories for avg 4 year old boy.
print("")
    
def BMICalculator(calories):
    caloriesCount={"Milk":100,"Vegetables":85,"Meat":143,"Lentils":113,"Egg":155,"Rice":130} 
    totalCalories = 0
    for key, value in calories.items():
            calorie=value                      
            while calorie!=0:
                if  calorie- 100 >= 0:         
                    calorie-= 100
                    totalCalories += caloriesCount[key]
                else:                             
                    fraction = calorie/100
                    totalCalories +=  caloriesCount[key]* fraction
                    calorie = int(calorie - (caloriesCount[key] * fraction))
                    break
             
    return totalCalories 

def Result(name,age,totalCalories):
    if age>=0 and age<2:      
        if totalCalories<800:
            print('The daily calorie consumption of ' +name+ " should be 800, but " +gender+ " is taking {1},required more calories  and is  under-nourished.".format(name,totalCalories))
        else:
            print('The daily calorie consumption of ' +name+ " should be 800, " +gender+ " is taking {1}, is nourished.".format(name,totalCalories))
    elif age>=2 and age<4:       
        if totalCalories<1400:
            print('The daily calorie consumption of ' +name+ " should be 1400, but " +gender+ " is taking {1}, required more calories  and is  under-nourished.".format(name,totalCalories))
        else:
            print('The daily calorie consumption of ' +name+ " should be 1400, " +gender+ " is taking {1}, is nourished.".format(name,totalCalories))
    elif age>=4 and age<8:      
        if totalCalories<1800:
            print('The daily calorie consumption of ' +name+ " should be 1800, but " +gender+ " is taking {1}, required more calories  and  is  under-nourished.".format(name,totalCalories))
        else:
            print('The daily calorie consumption of ' +name+ " should be 1800, " +gender+ " is taking {1}, is nourished.".format(name,totalCalories))
    elif age>8:
        print( "HUH!" +gender+ ' is not Child!')
        return 0

totalCalories = BMICalculator(calories)  

totalCaloriesTwoDecimal= round(totalCalories, 2)

Result(name,age,totalCaloriesTwoDecimal)

print("")
 

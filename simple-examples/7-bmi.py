print "What is your weight in KG?"
weight = int(raw_input())

print "What is your height?"
height = float(raw_input())

bmi = weight / (height * height)
print "Your bmi is {}".format(bmi)

if bmi <= 18.5 :
    print "You are UNDERWEIGHT"
elif bmi > 18.5 and bmi <= 25 :     
    print "You are in NORMAL range "
elif bmi > 25 and bmi <= 30 :
    print "You are OVERWEIGHT"
else :
    print "You are OBESE"
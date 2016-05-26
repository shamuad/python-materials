print "What is your weight in KG?"
weight = int(raw_input())

print "What is your height?"
height = float(raw_input())

bmi = weight / (height * height)
print "Your bmi is {}".format(bmi)
pin = "abc"
input_pin = raw_input("Enter your PIN number")

if input_pin == pin:
    print "Welcome"
else:
    while input_pin != pin:
        input_pin = raw_input("enter your PIN again")
    print "Welcome"
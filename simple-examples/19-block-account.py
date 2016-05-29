pin = "abc"
input_limit = 3      

while input_limit != 0 :
    input_pin = raw_input("Please enter your PIN number : ")
    input_limit = input_limit - 1
    if input_pin == pin :
        print "Welcome"
        break
    else :
        print "You have {} input left".format(input_limit)
        continue
else:
    print "your account is currently blocked"     

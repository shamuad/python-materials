import math

# Function calculates triangle area and return the result
def triangle_area(base,height) :
    return base * height / 2
   
# Function calculates rectangle area and return the result
def rectangle_area(length,width) :
    return length * width
    
# Function calculates Square area and return the result
def square_area(side_lenght) :
    return side_lenght * side_lenght
    
# Funtion calculates circle area and return the result
def circle_area(radius) :
    return math.pi * radius ** 2
    
      
ifchosed = True
while ifchosed == True :
    choice = raw_input("\n1) Triangle \n2) Rectangle \n3) Square \n4) Circle \n5) Quit \n\nwhich shape ? ")    
    if choice.isdigit() == False :
         print "You have to give numeric number"
         continue
    else :  
        choice = int(choice)    
        if  choice == 1 :
            base = int(raw_input("Enter the base of triangle : "))
            height = int(raw_input("Enter the height of triangle : "))
            result = triangle_area(base,height)
            print result
            continue
        elif choice == 2 :
            lenght = int(raw_input("Enter the length of rectangle : "))
            width = int(raw_input("Enter the width of rectangle : "))
            result = rectangle_area(lenght,width)
            print result
            continue
        elif choice == 3 :
            side_lenght = int(raw_input("Enter the side lenght of the square : "))
            result = square_area(side_lenght)
            print result
            continue
        elif choice == 4 :
            radius = int(raw_input("Enter the radius of the circle : "))
            result = circle_area(radius)
            print result
            continue
        else :
            ifchosed = False
            break     

    
 
   


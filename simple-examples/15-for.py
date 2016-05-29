import sys

#for(int i = 0; i < 10; i++){
#    suite
#}

#actually range(10) is an array, so it behaves like foreach.
for i in range(10):
    print i
    
for i in range(4,8):
    print i
    
for i in range(2,10,2):
    sys.stdout.write(str(i) + " ")
    
print "\n"
for character in "Python":
    print character
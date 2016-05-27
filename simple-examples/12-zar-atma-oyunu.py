import random

raw_input("Please user 1 press ENTER for the dices") 
user1_dice1 = random.randint(1 , 6)      
user1_dice2 = random.randint(1 , 6)
print "User One  dice {} - {}".format(user1_dice1 , user1_dice2)

raw_input("Please user 2 press ENTER for the dices")           
user2_dice1 = random.randint(1 , 6)
user2_dice2 = random.randint(1 , 6)
print "User Two  dice {} - {}".format(user2_dice1 , user2_dice2)    

if user1_dice1 == user1_dice2 :
    user1_same = user1_dice1 + user1_dice2
else :
    user1_same = 0
    
if user2_dice1 == user2_dice2 :
    user2_same = user2_dice1 + user2_dice2
else :
    user2_same = 0
    
print "user1_same : {} , user2_same : {}".format(user1_same , user2_same)

'''    
if user1_same <> 0 and user2_same <> 0 and user1_same > user2_same :
    print "The winner is User One"
elif user1_same <> 0 and user2_same <> 0 and user2_same > user1_same :
    print "The winner is User Two"
elif user1_same <> 0 and user2_same <> 0 and user2_same == user1_same :
    print "Draw - No winner - woow same dice"
elif user1_same <> 0 and user2_same == 0 :
     print "The winner is User One"
elif user2_same <> 0 and user2_same == 0 :
    print "The winner is User Two"
elif user1_same == 0 and user2_same == 0 and user1_dice1 + user1_dice2 > user2_dice1 + user2_dice2 :
    print "The winner is User One"
elif user1_same == 0 and user2_same == 0 and user1_dice1 + user1_dice2 < user2_dice1 + user2_dice2 :
    print "The winner is User Two"
else :
    print "No winner" 
'''

if user1_same <> 0 and user2_same <> 0 and user1_same > user2_same :
    who_is_the_winner = "One"
elif user1_same <> 0 and user2_same <> 0 and user2_same > user1_same :
    who_is_the_winner = "Two"
elif user1_same <> 0 and user2_same <> 0 and user2_same == user1_same :
    who_is_the_winner = "Draw - No winner - woow same dice"
elif user1_same <> 0 and user2_same == 0 :
     who_is_the_winner = "One"
elif user2_same <> 0 and user1_same == 0 :
    who_is_the_winner = "Two"
elif user1_same == 0 and user2_same == 0 and user1_dice1 + user1_dice2 > user2_dice1 + user2_dice2 :
    who_is_the_winner = "One"
elif user1_same == 0 and user2_same == 0 and user1_dice1 + user1_dice2 < user2_dice1 + user2_dice2 :
    who_is_the_winner = "Two"
else :
    who_is_the_winner = "No winner"
    

print "\n**************************"
print "   The Winner is         "
print "     {}                  ".format(who_is_the_winner)
print "\n**************************"
 
    
    
    
    





import random

raw_input("Please user 1 press ENTER for the dices")
user1_dice1 = random.randint(1, 6)
user1_dice2 = random.randint(1, 6)

user1_get_double = False
if user1_dice1 == user1_dice2:
    user1_get_double = True

print "User One  dice {} - {}".format(user1_dice1, user1_dice2)

raw_input("Please user 2 press ENTER for the dices")
user2_dice1 = random.randint(1, 6)
user2_dice2 = random.randint(1, 6)

user2_get_double = False
if user2_dice1 == user1_dice2:
    user2_get_double = True

print "User Two  dice {} - {}".format(user2_dice1, user2_dice2)

point_of_user1 = user1_dice1 + user1_dice2
point_of_user2 = user2_dice1 + user2_dice2

winner = 0
if user1_get_double and not user2_get_double:
    winner = 1
elif not user1_get_double and user2_get_double:
    winner = 2
else:
    winner = 1 if point_of_user1 > point_of_user2 else 2

print "\n**************************"
print "   The Winner is         "
print "     {}                  ".format(winner)
print "\n**************************"
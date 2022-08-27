import random
men = 0
women = 0
for i in range(160):
    if random.randint(1, 2) == 1:
        men = men + 1
    else:
        women = women + 1
print('The number of men on the bus is ' + str(men) + '.')
print('The porcentage of men on the bus is ' + str(men/160) + '.')
print('The number of women on the bus is ' + str(women) + '.')
print('The porcentage of women on the bus is ' + str(women/160) + '.')
print('The total amount of passengers is ' + str(men + women) + '.')

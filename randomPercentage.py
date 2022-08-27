import random
num_0 = 0
num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
num_5 = 0
num_6 = 0
num_7 = 0
num_8 = 0
num_9 = 0
for i in range(100):
    randNum = random.randint(1, 10)
    if randNum == 1:
        num_0 = num_0 + 1
    elif randNum == 2:
        num_1 = num_1 + 1
    elif randNum == 3:
        num_2 = num_2 + 1
    elif randNum == 4:
        num_3 = num_3 + 1
    elif randNum == 5:
        num_4 = num_4 + 1
    elif randNum == 6:
        num_5 = num_5 + 1
    elif randNum == 7:
        num_6 = num_6 + 1
    elif randNum == 8:
        num_7 = num_7 + 1
    elif randNum == 9:
        num_8 = num_8 + 1
    elif randNum == 10:
        num_9 = num_9 + 1
    else:
        print('ERROR.')
print('num_0: ' + str(num_0) + ' ▮▮▮ num_0/100: ' + str(num_0/100))
print('num_1: ' + str(num_1) + ' ▮▮▮ num_1/100: ' + str(num_1/100))
print('num_2: ' + str(num_2) + ' ▮▮▮ num_2/100: ' + str(num_2/100))
print('num_3: ' + str(num_3) + ' ▮▮▮ num_3/100: ' + str(num_3/100))
print('num_4: ' + str(num_4) + ' ▮▮▮ num_4/100: ' + str(num_4/100))
print('num_5: ' + str(num_5) + ' ▮▮▮ num_5/100: ' + str(num_5/100))
print('num_6: ' + str(num_6) + ' ▮▮▮ num_6/100: ' + str(num_6/100))
print('num_7: ' + str(num_7) + ' ▮▮▮ num_7/100: ' + str(num_7/100))
print('num_8: ' + str(num_8) + ' ▮▮▮ num_8/100: ' + str(num_8/100))
print('num_9: ' + str(num_9) + ' ▮▮▮ num_9/100: ' + str(num_9/100))
print('∑(num_i) = ' + str(num_0 + num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7 + num_8 + num_9) + ' ▮▮▮ ∑(num_i/100) = ' + str(num_0/100 + num_1/100 + num_2/100 + num_3/100 + num_4/100 + num_5/100 + num_6/100 + num_7/100 + num_8/100 + num_9/100))

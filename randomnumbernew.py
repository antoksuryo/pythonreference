import random
from numpy import random
from cs50 import get_int
import numpy as np

fromnumber = get_int("enter number from : ")

untilnumber = get_int("enter number until : ") + 1

repeat = get_int("repeat how many time : ")

while True:
    destinynumber = get_int("what number result you want : ")
    if destinynumber >= fromnumber and destinynumber <= untilnumber:
        break

loop = get_int("loop for : ")

stability = untilnumber - destinynumber
stabilfrom = destinynumber - stability

stability2 = destinynumber - fromnumber
stabilto = destinynumber + stability2



average = round((untilnumber - fromnumber) / 2)
average2 = round((untilnumber - fromnumber) / 6)
average3 = round(((untilnumber - fromnumber) / 6) * 5)

generate1 = fromnumber + average
generate2 = fromnumber + average2
generate3 = fromnumber + average3


desirednumber = (destinynumber * repeat)

size=round((repeat - 1) / 2)
size2=((repeat - 1) - size)
size3=round((repeat - 1) / 4)
size4=((repeat - 1) - size3)

jumlah = 0

## result and output to array
for i in range(loop):
    while True:
        list1 = (random.randint(fromnumber, generate1, size))
        list2 = (random.randint(generate1, untilnumber, size2))
        minus = desirednumber - sum(list1)
        jumlah = (desirednumber - ((sum(list1) + sum(list2))))
        while jumlah <= fromnumber:
            list1 = (random.randint(fromnumber, stabilto, size))
            list2 = (random.randint(fromnumber, stabilto, size2))
            jumlah = (desirednumber - ((sum(list1) + sum(list2))))

        while jumlah >= untilnumber:
            list1 = (random.randint(stabilfrom, untilnumber, size))
            list2 = (random.randint(stabilfrom, untilnumber, size2))
            jumlah = (desirednumber - ((sum(list1) + sum(list2))))


        if jumlah <= destinynumber and jumlah >= fromnumber:
            break
    ## calculate the length of array


    newjumlah = [jumlah]
    hs = np.concatenate((list1, list2, newjumlah))
    ab = sum(hs) / len(hs)

    print(hs)

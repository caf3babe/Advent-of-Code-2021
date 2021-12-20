#!/usr/bin/env python3

def get_increased_values(list_of_values):
    previous = 0
    count = 0
    for value in list_of_values:
        number = int(value)
        if previous == 0:
            previous = number
            continue

        if number > previous:
            count = count + 1
        previous = number
    
    return count

fileName="day-one-input.txt"

with open(fileName) as file:
    lines = file.readlines()

# part 1 - correct value 1581
print(get_increased_values(lines))

# part 2
triples = []
firstTriple = [3]
secondTriple = [3]
thirdTriple = [3]

for idx, line in enumerate(lines):
    number = int(line)
    if(idx == 1):
        firstTriple.append(number)
        continue;
    if(idx % 3 == 0):
        firstTriple.append(number)
        thirdTriple.append(number)
    if(idx % 3 == 1):
        firstTriple.append(number)
        secondTriple.append(number)
    if(idx % 3 == 2):
        secondTriple.append(number)
        thirdTriple.append(number)
    if(len(firstTriple) == 3):
        triples.append(firstTriple)
        firstTriple = []
    if(len(secondTriple) == 3):
        triples.append(secondTriple)
        secondTriple = []
    if(len(thirdTriple) == 3):
        triples.append(thirdTriple)
        thirdTriple = []

summedValues = []

for triple in triples:
    sum = 0
    for value in triple:
        sum += value
    summedValues.append(sum)

print(get_increased_values(summedValues))

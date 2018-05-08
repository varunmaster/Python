# this script takes an input that is letters and translates them each 2 units to the right.
# e.g. k --> m | a--> c etc.
# challenge url: http://www.pythonchallenge.com/pc/def/map.html

from string import *

alphabet = 'abcdefghijklmnopqrstuvwxyz'
input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# "map"
input2Num = list(input)
num2Letter = list(input2Num)

# take input2Num list array and then convert the letters to numbers based on the position
for i in range(0, len(input)):
    if input2Num[i] == ' ' or input2Num[i] == '.' or input2Num[i] == '(' or input2Num[i] == ')':
        continue
    else:
        input2Num[i] = alphabet.index(input[i].lower()) + 3 #moved 3 spaces bc 2 (from challenge) + 1 (indexing starts at 0)

# if the values are over 26 (letter z) then loop back to the beginning
for i in range(0, len(input)):
    if input2Num[i] == ' ' or input2Num[i] == '.' or input2Num[i] == '(' or input2Num[i] == ')':
        continue
    elif input2Num[i] > 26:
        input2Num[i] = int(input2Num[i]) - 26

# convert the numbers to letter after they have been translated
for i in range(0, len(num2Letter)):
    if input2Num[i] == ' ' or input2Num[i] == '.' or input2Num[i] == '(' or input2Num[i] == ')':
        continue
    else:
        num2Letter[i] = alphabet[input2Num[i] - 1]

print(input2Num)
print(join(num2Letter))

# once you read the message, it says to apply it on the url. this means that take the last part of url "map" and then
# move each letter 2 spaces to the right. to do this, change the input variable to "map" and then run the program.

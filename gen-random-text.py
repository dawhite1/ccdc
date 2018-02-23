import sys
import string
import random
def get(randstring, size):
    max = size
    i = 0
    while i < max:
        set = [0,1,2]
        char = ""
        letter = random.choice(string.ascii_letters)
        number = random.choice(string.digits)
        symbol = random.choice(string.punctuation)
        pick = random.choice(set)
        if pick:
            char = letter
        elif pick == 1:
            char = number
        else:
            char = symbol
        randstring += char
        i += 1
    return randstring
def main():
    size = 128
    randstring = ""
    file = open('random-text.txt', 'w')
    i = 0
    while i < size:
        randstring = get(randstring, size)
        i += 1
        print randstring
    file.write(randstring)
    file.close()
if __name__ == "__main__": main()

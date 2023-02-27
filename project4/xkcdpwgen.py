
#!/usr/bin/env python3

import argparse
import random

import string
from string import punctuation


parser = argparse.ArgumentParser(description = "Generate a secure, memorable password using the XKCD method")


parser.add_argument("-w", "--words", type=int, default=4,
help="include WORDS words in the password")

parser.add_argument("-c", "--caps", type=int, default=0,
help="capitalize the first letter of CAPS random words")

parser.add_argument("-n", "--numbers", type=int, default=0,
help="insert NUMBERS random numbers in the password")

parser.add_argument("-s", "--symbols", type=int, default=0,
help="insert SYMBOLS random symbols in the password")

args = parser.parse_args()


# opens word list text file
readLoW = open("words.txt")
LoW = readLoW.read().splitlines()
subLoW = random.sample(LoW, args.words)


def get_random_caps(subLoW, num_caps):
    caps = random.sample(subLoW, num_caps)
    return [word.title() if word in caps else word for word in subLoW], caps

def get_random_nums(num_nums):
    return [str(random.randint(0, 9)) for _ in range(num_nums)]

def get_random_syms(num_syms):
    return random.sample(string.punctuation, num_syms)


if args.caps > 0 and args.words >= args.caps:
    subLoW, subCaps = get_random_caps(subLoW, args.caps)

if args.numbers > 0:
    subLoW += get_random_nums(args.numbers)

if args.symbols > 0:
    subLoW = get_random_syms(args.symbols) + subLoW

random.shuffle(subLoW)

genPassword ="".join(subLoW)
print(genPassword)

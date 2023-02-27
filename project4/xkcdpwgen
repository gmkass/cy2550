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


# for randomized Caps
defaultCaps = 0
List1 = list()
if 0 < args.caps and args.words >= args.caps:
 subCaps = random.sample(subLoW, args.caps)
 subLoW = list(set(subLoW) - set(subCaps))
while args.caps > defaultCaps:
 List1.append(subCaps[defaultCaps].title())
 defaultCaps += 1
subLoW = List1 + subLoW
random.shuffle(subLoW)



# for insert random Numbers
defaultNum = 0
List2 = list()
if (args.numbers > 0):
 while (defaultNum < args.numbers):
  LoN = [str(random.randint(0, 9))]
  defaultNum += 1
 List2 = List2 + LoN
subLoW = subLoW + List2
random.shuffle(subLoW)

# for insert random Symbols
defaultSym = 0
LoS = list()
if 0 < args.symbols:
    List3 = set(string.punctuation)
    subSyms = random.sample(List3, args.symbols)
    subLoW = subSyms + subLoW
    random.shuffle(subLoW)


genPassword ="".join(subLoW)

print(genPassword)

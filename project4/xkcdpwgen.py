#!/usr/bin/env python3

import random
import argparse
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

openLoW = open("words.txt")

LoW = openLoW.read().splitlines()

subLoW = random.sample(LoW, args.words)


defaultCaps = 0
capsList = []
if (args.caps > 0 and args.caps <= args.words):
 subCaps = random.sample(subLoW, args.caps)
 subLoW = list(set(subLoW) - set(subCaps))
while (defaultCaps < args.caps):
 capsList.append(subCaps[defaultCaps].title())
 defaultCaps += 1

subLoW = subLoW + capsList

random.shuffle(subLoW)


defaultNum = 0
numList = []
if (args.numbers > 0):
 while (defaultNum < args.numbers):
  tempList = [str(random.randint(0, 9))]
  defaultNum += 1
  numList = numList + tempList

subLoW = subLoW + numList
random.shuffle(subLoW)



if (args.symbols > 0):
    symsList = set(string.punctuation)
    subSyms = random.sample(symsList, args.symbols)

    subLoW = subLoW + subSyms
    random.shuffle(subLoW)


password ="".join(subLoW)
print(password)

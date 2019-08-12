## Crazytalk is a simple program to generate crazy word salad
## sentence syntax:
## [subject] [predicate] [subordinating conjunction] [subject] [predicate][punctuation]
## [My leg] [is on fire] [with] [the sound] [of shattering ants][!]
##
## pull the lists for the different parts at random from a json.

import jsonpickle, os, sys, random

SALAD_FILENAME = 'wordsalad.json'

## Loading wordsalad
def loadSalad():
    '''load up the word salad and dump the json to wordSalad'''
    with open(SALAD_FILENAME, 'r') as words:
        wordSalad = jsonpickle.decode(words.read())
    return wordSalad

## The generator
def sayCrazy(wordSalad):
    '''actual generator. Chooses from 1 or two clauses per sentence'''
    one = random.choice(wordSalad['subject']) + ' ' + random.choice(wordSalad['predicate'])
    two = random.choice(wordSalad['subject']) + ' ' +random.choice(wordSalad['predicate']) + ' ' + random.choice(wordSalad['conjunction']) + ' ' + random.choice(wordSalad['subject']) + ' ' + random.choice(wordSalad['predicate'])
    sentence = random.choice((one, two)).split(".")
    for i in sentence:
        print(i.strip().capitalize() + random.choice(wordSalad['punctuation']) + " ", end="", flush=True)

wordSalad = loadSalad()

## Asks for 0 to 6 sentences. If zero, you just get (...)
num = random.randint(0,7)
if num == 0:
    print("...")
else:
    for i in range(0, num):
        sayCrazy(wordSalad)

#Game to practice the states and their capitals and abbreviations
import copy
import random

def readFile(filename, aList):
    f = open(filename, 'r')
    for line in f:
       aList.append(line.strip().lower().split(','))
    f.close()

def makeAbbrev(stateList, aDict):
    for state in stateList:
      aDict[state[0]] = state[1]

def makeCapitals(stateList, aDict):
    for state in stateList:
      aDict[state[0]] = state[2]

def makeStateNames(stateList, aDict):
    for state in stateList:
      aDict[state[1]] = state[0]

def test(aDict, testType):
    if testType == 1:
      test = 'abbreviation'
    elif testType == 2:
      test = 'capital'
    elif testType == 3:
      test = 'name'
    
    ans = ''
    count = 0

    for k in aDict.keys():
      print('What is the state ' + test + ' of: ')
      print(k)
      ans = raw_input().strip().lower()
      if ans == aDict[k]:
        print('Correct!')
        count += 1
      else:
        print('Incorrect!')

    return score


def chooseTest():
    choice = ' '
    while choice not in [1, 2, 3]:
      print('Pick 1 for state names to abbreviations.')
      print('Pick 2 for state names to state capitals.')
      print('Pick 3 for abbreviations to state names.')
      choice = int(raw_input())
    return choice

def playAgain():
    print('Do you want to play again? (yes or no)')
    return raw_input().lower().startswith('y')

states = []
readFile('states.csv', states)
random.shuffle(states)
print('raw')
print(states)
print('\n')

abbrev = {}
makeAbbrev(states, abbrev)
print('names -> abbre')
print(abbrev)
print('\n')

capitals = {}
makeCapitals(states, capitals)
print('names -> capitals')
print(capitals)
print('\n')

names = {}
makeStateNames(states, names)
print('abbrev -> names')
print(names)
print('\n')

print('Welcome to the states games!')

repeatGame = True

while repeatGame:

  score = 0
  choice = ' ' 
  while choice not in [1, 2, 3]:
    choice = chooseTest()

  if choice == 1:
    print('You choose state names to abbreviations.')
    score = test(abbrev, 1)
  elif choice == 2:
    print('You choose state names to state capitals.')
    score = test(capitals, 2)
  elif choice == 3:
    print('You choose abbreviations to state names.')
    score = test(names, 3)

  print('You scored: ' + str(score) + ' out of ' + str(len(states)) + ' points.')
  print('\n')
  repeatGame = playAgain()
  if repeatGame == False:
    print('Thanks for playing! Goodbye!')

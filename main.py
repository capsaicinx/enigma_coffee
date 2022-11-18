# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import itertools


#Reading in participants
participants = pd.read_csv('participants.csv', header=0, encoding = 'utf8', delimiter=';')
print(participants.to_string(index=False, header=False));

print('');

#Reading in previous matches
previous_matches = pd.read_csv('previous_matches.csv', header=0, encoding = 'utf8', delimiter=';')
print(previous_matches.to_string(index=False, header=False));

print('')

#generate all possible matches from participants
participantslist = participants.Names.tolist()
print('List of Participants:')
print(participantslist)
print('')
print('List of possible matches/combinations:')
combinationslist = itertools.combinations(participantslist, 2);
print(list(combinationslist))


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#   print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

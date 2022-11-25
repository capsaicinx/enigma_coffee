# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import itertools

#Sorts a tuple with 2 values alphabetically
def tuplesort(inputtuple):
    a = inputtuple[0]
    b = inputtuple[1]
    #user lowercase string for comparisson, otherwise A != a
    al = a.lower()
    bl = b.lower()
    length = len(al)
    if (length > len(bl)):
        length = len(bl)
    for x in range(length):
        if (al[x] > bl[x]):
            outputtuple = (b,a)
            return outputtuple
            break
        if  (al[x] < bl[x]):
            outputtuple= (a,b)
            return outputtuple
            break
        if x==length-1:
            if len(al) > len(bl):
                outputtuple= (b,a)
                return outputtuple
            else:
                outputtuple= (a,b)
                return outputtuple

#Reading in participants
participants = pd.read_csv('participants.csv', header=0, encoding = 'utf8', delimiter=';')
print(participants.to_string(index=False, header=False));

print('');

#Reading in previous matches
previous_matches = pd.read_csv('previous_matches.csv', header=0, encoding = 'utf8', delimiter=';')
print(previous_matches.to_string(index=False, header=False));

print('')

#generate all possible matches (2ppl) from participants
participantslist = participants.Names.tolist()
print('List of possible matches/combinations:')
combinationslist = list(itertools.combinations(participantslist, 2));
print(combinationslist)

#Sorting individual tupls alphabetically
print('Sorting combinations alphabetically')
for i in combinationslist:
    print(i)
    print(tuplesort(i))

#print('test tuplesort')
#testtuple = ("abcd","abc");
#print(testtuple);
#print(tuplesort(testtuple))





#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#   print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

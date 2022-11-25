# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#ToDo: Implement shuffling
#ToDo: Detect and move around not possible to create enough matches
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
print('Reading in participans...')
participants = pd.read_csv('./input/participants.csv', header=0, encoding = 'utf8', delimiter=';')
print('Dropping duplicate participants')
participants = participants.drop_duplicates();
print('Participants')
print(participants)
#print(participants.to_string(index=False, header=False));

#generate all possible matches (2ppl) from participants
participantslist = participants.Names.tolist()
print('List of possible matches/combinations:')
combinationslist = list(itertools.combinations(participantslist, 2));
print(combinationslist)

#Sorting individual tupls alphabetically
print('Sorting combinations alphabetically')
for index, tuple in enumerate(combinationslist):
    combinationslist[index] = tuplesort(tuple)

#Reading in previous matches
print('Reading previous matches...')
previous_matches = pd.read_csv('./input/previous_matches.csv', header=0, encoding = 'utf8', delimiter=';')
previous_matchlist = list(previous_matches.itertuples(index=False, name=None))
#sort prev match tuples alphabetically
print('Sorting prev_matches alphabetically')
for index, tuple in enumerate(previous_matchlist):
    previous_matchlist[index] = tuplesort(tuple)

#drop duplicates after sorting
#for sure there is a more efficient way to do this :D
print('Dropping duplicates in previous matches')
previous_matches = pd.DataFrame(previous_matchlist);
previous_matches = previous_matches.drop_duplicates()
previous_matchlist = list(previous_matches.itertuples(index=False, name= None))

print('')

#Remove already completed matches from combinationslist to create possible matches
print('Removon previous matches form possibles')
possible_unmatched_matches = list(set(combinationslist)-set(previous_matchlist))

#Generate matches for paticipants
print('Generate Matches')
#Idea go through possible matches and take the ones for which both are still in participants list until participantslist empty
temp_participants = participantslist
final_matches = []
for match in possible_unmatched_matches:
    if match[0] in temp_participants and match[1] in temp_participants:
        final_matches.append(match)
        temp_participants.remove(match[0])
        temp_participants.remove(match[1])
        #end if all participants matched
        if len(temp_participants) <= 1:
            if len(temp_participants) == 1:
                final_matches.append((temp_participants.pop(), "NO_MATCH"))
            break
        #ToDo: Detect if list not empty but no more unmatched matches possible

print('Final matches:')
print(final_matches)

print('Write matches to output...')
final_matches_df = pd.DataFrame(final_matches)
final_matches_df.to_csv('./output/generated_matches.csv', encoding = 'utf8', sep=';', index=False, header=False)




#print('test tuplesort')
#testtuple = ("abcd","abc");
#print(testtuple);
#print(tuplesort(testtuple))


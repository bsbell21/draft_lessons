import random
import sys
from monty import Monty


def switch(doors, chosen, empty):
    '''
    INPUT: list of strings, string, string
    OUTPUT: integer

    doors is a list of length three containing the names of all the doors.
    chosen is the door the user has chosen and empty is the door that has been
    shown to be empty.
    Return the door that is the result of switching doors.
    '''

    return [x for x in doors if x not in [empty, chosen]][0]

def stay(doors, chosen, empty):
    '''
    INPUT: list of strings, string, string
    OUTPUT: integer

    doors is a list of length three containing the names of all the doors.
    chosen is the door the user has chosen and empty is the door that has been
    shown to be empty.
    Return the door that is the result of staying with the original door.
    '''
    return chosen

def randomdoor(doors, chosen, empty):
    '''
    INPUT: list of strings, string, string
    OUTPUT: integer

    doors is a list of length three containing the names of all the doors.
    chosen is the door the user has chosen and empty is the door that has been
    shown to be empty.
    Return the door that is chosen randomly from the two doors that are not
    empty.
    '''
    return random.choice([x for x in doors if x != empty])


def main(n):
    strategies = {'switch': switch, 'stay': stay, 'random': randomdoor}
    for name, strategy in strategies.iteritems():
        monty = Monty()
        print name, "\t", monty.play_n_times(n, strategy)

if __name__ == '__main__':
    main(int(sys.argv[1]))

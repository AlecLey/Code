# This already implements menu option 1.  The program initially
# reads the input file into a single list of Inspection objects
# called allrecords.  To make search more efficient, the program
# creates 2 dictionaries: violation_name_dict.
# The first is indexed by restaurant name, and maps to a list of
# indices where the name is contained in allrecords.
file1 = open('test.txt','r')
from datetime import date
from math import isclose
from operator import itemgetter
from sys import exit

with open("restaurant_inspections.txt", "a") as myfile:
    myfile.write("appended text")

class Inspection:
# Class Inspection is a data holder of an inspection record.
    def __init__(self, record_str):
        '''
        record_str is a line string from the input file.
        '''
        record_str = record_str.lower()
        tokens = record_str.split('*')
        self.record_id = tokens[0]
        self.name = tokens[1]
        self.boro = tokens[2]
        self.cuisine = tokens[3]
        self.inspection_date = tokens[4]
        self.violation = tokens[5]

        # if a score is either not recorded, is near zero, or is negative,
        # then assign infinity to it
        try:
            self.score = float(tokens[6])
            if isclose(self.score, 0.0) or self.score < 0.0:
                self.score = float('+inf')
        except:
            self.score = float('+inf')

        self.grade = tokens[7]

        # store grade date as a date object (part of datetime module) for
        # ease of comparison
        # see https://docs.python.org/3/library/datetime.html
        date_fields = tokens[8].split('/')
        if (len(date_fields) == 3):
            self.grade_date = date(int(date_fields[2]), int(date_fields[0]),
                                   int(date_fields[1]))
        else:
            self.grade_date = date(1800,1,1)

    def __str__(self):
        return self.name + " inspected on " + self.inspection_date + " with a score of " + str(self.score)

    def __repr__(self):
        return str(self)

    '''
    Implementation of less than special function to enable comparison
    of Inspection objects.
    '''
    def __lt__(self, other):
        return self.name < other.name

### End of Inspection class

def build_inspections_list(filename):
    '''
    Build list of inspection objects from input file.

    filename: name of input file
    returns: list of inspection objects, sorted by restaurant name.
    '''
    allrecords = []

    try:
        fin = open(filename, 'r', encoding='utf-8')
    except IOError:
        print('restaurant_inspections file error.')
        print('Be sure file is in the same folder as the python program.  Bye.')
        exit(0)

    fin.readline()
    for record in fin:
        allrecords.append(Inspection(record))

    fin.close()
    allrecords.sort()

    return allrecords





#def build_violation_term_dict(allrecords):
    '''
    Input: allrecords, a list of all restaurant records.
    Returns: A dictionary of all words occurring in violation descriptions for
    efficient lookup.  Dictionary is keyed by violation word, and it maps
    to a list of list indices in allrecords where the word occurs.  Removes
    punctuation symbols from the violation description:
    [',', '.', ';', ':', '!', '?']
    '''
    #
    #  Fill in your code here
    #

#def search_violations(search_term, allrecords, violation_term_dict):
    #
    #  Fill in your code here
    #

def build_restaurant_name_dict(allrecords):
    '''
    Build a dictionary for efficient lookup by restaurant name.  Dictionary
    maps restaurant name to a list of indices in allrecords containing with
    a matching restaurant name.

    allrecords: list of all inspection records
    returns: dictionary mapping restaurant name to indices in allrecords
    '''
    restaurant_dict = {}
    for idx, inspection in enumerate(allrecords):
        if inspection.name in restaurant_dict:
            restaurant_dict[inspection.name].append(idx)
        else:
            restaurant_dict[inspection.name] = [idx]

    return restaurant_dict

def search_by_name(search_term, allrecords, restaurant_name_dict):
    if search_term in restaurant_name_dict:
        indices = restaurant_name_dict[search_term]
        print('nRecords found:')
        for idx in indices:
            print("   ", allrecords[idx])
        print('nn')
    else:
        print('nRestaurant not found.')


def get_menu_option():
    '''
    Display menu options and validate input.

    returns: selection string
    '''
    valid_options = ['1', '2', '3', 'EXIT']
    selection = ''

    while selection not in valid_options:
        print('   1. Search restaurant by name.')
        print('   2. Search by violation keyword.')
        print('   3. Search A-rated restaurants by borough and cuisine.n')
        selection = input('Make your selection, EXIT if done: ').upper()
        if selection not in valid_options:
            print('    Invalid option.  Try again.nn')

    return selection
class ressearch():
   
    def keyword(key):
        t = 0
        for res in file1.readlines():
            res2 = res.split('*')[5]
            res3 = res2.split()
            t += 1
            if key in res3:
                name = res.split('*')[1]
                print(f"name : {name} | {res2}")
                
    def borough_grade_type(bor, grade, ty):
        t = 0
        for res in file1.readlines():
            
            type1 = ty.title()
            bor = bor.upper()
            grade = grade.upper()
            res2 = res.split('*')[2]
            res3 = res.split('*')[7]
            res4 = res.split('*')[3]
            res5 = res.split('*')[1]
            if res2 == bor and res3 == grade and res4 == type1:
                print(f"name : {res5} | type : {type1} | grade : {res3}") 

def main():
    print('nnNYC restaurant inspections')
    print('   Loading records.  Please wait. n')
    allrecords = build_inspections_list('restaurant_inspections.txt')
    restaurant_name_dict = build_restaurant_name_dict(allrecords)
    #violation_term_dict = build_violation_term_dict(allrecords)

    end_input = False
    file1 = open('restaurant_inspections.txt','r')
    while not end_input:
        selection = get_menu_option()
        if selection == '1':
            search_term = input('nEnter restaurant name: ').lower()
            search_by_name(search_term, allrecords, restaurant_name_dict)
        elif selection == '2':
            ressearch.keyword(key=input('Keyword : '))
        elif selection == '3':
            bor = input('bor : ')
            gra = input('grade : ')
            typ = input('type : ')
            ressearch.borough_grade_type(bor,gra,typ)
        elif selection == 'EXIT':
            end_input = True

    print('nGoodbye.')

main()

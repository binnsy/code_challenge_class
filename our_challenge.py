"""Our Coding Challenge

Write a script that counts how many times each letter appears in your full name."""

################################# Part 1 ############################################
# Inital solution
def count_letters(full_name):
    """Returns a dictionary of the letters and how often they appear in name

    >>> count_letters('Brighticorn')
    {'c': 1, 'B': 1, 'g': 1, 'i': 2, 'h': 1, 'o': 1, 'n': 1, 'r': 2, 't': 1}
    """

    # your code here

    count_letters = {}
    for letter in full_name:
        if letter not in count_letters:
            count_letters[letter]=1
        else:
            count_letters[letter]+= 1
    return count_letters
    print count_letters
################################# Part 2 ############################################
# Solves for spaces
def count_letters_no_spaces(full_name):
    """Returns a dictionary of the letters and how often they appear in name

    >>> count_letters_no_spaces('Brighticorn Hackbright')
    {'a': 1, 'c': 2, 'B': 1, 'g': 2, 'i': 3, 'h': 2, 'k': 1, 'o': 1, 'n': 1, 'r': 3, 't': 2, 'H': 1, 'b': 1}
    """

    # your code here
    #split_name = full_name.split(" ")
    full_name.replace("", " ")
    print full_name
    count_letters_no_spaces = {}
    
   
    # for letter in split_name[0]:
    #     if letter not in count_letters_no_spaces:
    #         count_letters_no_spaces[letter]=1
    #     else:
    #         count_letters_no_spaces[letter]+= 1
    # for letter in split_name[1]:
    #     if letter not in count_letters_no_spaces:
    #         count_letters_no_spaces[letter]=1
    #     else:
    #         count_letters_no_spaces[letter]+= 1

    # return count_letters_no_spaces


# solves for spaces & punctuation
def count_letters_no_spaces_punctuation(full_name):
    """Returns a dictionary of the letters and how often they appear in name

    >>> count_letters_no_spaces_punctuation("Bright-icorn O'Hackbright")
    {'O': 1, 'a': 1, 'c': 2, 'B': 1, 'g': 2, 'i': 3, 'h': 2, 'k': 1, 'o': 1, 'n': 1, 'r': 3, 't': 2, 'H': 1, 'b': 1}
    """

    # your code here
    pass


# solves for spaces, punctuation, case sensitivity
def count_letters_no_spaces_punctuation_case_sensitivity(full_name):
    """Returns a dictionary of the letters and how often they appear in name

    >>> count_letters_no_spaces_punctuation_case_sensitivity("Bright-icorn O'Hackbright")
    {'a': 1, 'c': 2, 'b': 2, 'g': 2, 'i': 3, 'h': 3, 'k': 1, 'o': 2, 'n': 1, 'r': 3, 't': 2}
    """

    # your code here
    pass


#####################################################################
# Don't touch the code below!
# This is just allowing us to run the doctests

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
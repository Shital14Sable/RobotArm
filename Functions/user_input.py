#!/usr/bin/env python3
max_length = 5

def take_user_input():
    """
    This function takes a user inputs, perform constraint checks and parses it
    @:return list of parsed user input
    """
    input_word = input("Please Enter a single letter or a string of letters from the English Alphabet")
    checks_passed = perform_checks(input_word)
    if checks_passed:
        parsed_list = parse_input(input_word)
        return parsed_list
    else:
        print("Sorry, this is not an acceptable input. Please try again")
        raise ValueError


def perform_checks(given_word):
    """
    This function checks whether the input string is part of the english  alphabet
    and if it fits in the given max_length  constraint
    :param given_word: Input string
    :return: check: (True-> meets constraints)/(False-> doesn't meet constraints)
    """
    global max_length
    check = True
    if len(given_word) > max_length:
        check = False
    if not given_word.isalpha():
        check = False
    return check


def parse_input(given_word):
    """
    This function parses the input into a list of individual  characters
    :param given_word: Input string
    :return: list  of letters
    """
    return list(given_word)


if __name__ == '__main__':
    #Parsing check
    trial_word = "Hello"
    parsed = parse_input(trial_word)
    print("Parsed input:", parsed)

    #Check checks
    trial_word1 = "He21"
    trial_word2 = ";fkdwl?"
    check_result =  perform_checks(trial_word)
    check_result1 = perform_checks(trial_word1)
    check_result2 = perform_checks(trial_word2)
    print("Test for {} : Result = {}".format(trial_word, check_result))
    print("Test for {} : Result = {}".format(trial_word1, check_result1))
    print("Test for {} : Result = {}".format(trial_word2, check_result2))

    #Putting it all together
    final_result = take_user_input()
    print("Final Result: {}".format(final_result))

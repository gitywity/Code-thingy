"""
Sets, much like lists, are a data structure that is used 
capable of holding multiple pieces of data at the same time. 

Every item in a list has a position starting at 0

In a set, items are not ordered and do not have a position. 

How to Make a Set:
    1)Making an Empty list
        my_set = set()
        my_set = {} 
    2)Making a list with items
        my_set = {'hello', 'world'}

Important Set Methods(tools):
    1).add(value)
        -takes a value and adds it to the set

Key Points About Sets:
    1) Sets can only store unique values
        -if you were to add the string 'hello' 
        to a set one million times, the set would
        only contain one item {'hello'}
"""


"""
Example Problems
"""

def check_unique_words(sentence):
    words = sentence.split() # here im splitting the given string into a list of the individual words
    my_set = set()
    for word in words: # im iterating through the list of words
        my_set.add(word)
    
    unique_word_count = len(my_set)
    return unique_word_count

user_input = input("Please enter a sentence or phrase >>> ") # add a comment to the beginning of the line to disable user input

if user_input:
    unique_word_count = check_unique_words(user_input)
    print(f"Your sentence contained {unique_word_count} unique words!")
    
"""
Homework

    1) Add a unique word counter to your sentence analyzer, much like above.

    2) Add a unique character counter to your sentence analyzer.
"""


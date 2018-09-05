"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed 
(Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than 
one word is present.
"""

def spin_words(sentence):
    split_sentence = sentence.split()
    hold=[]
    for each in split_sentence:
        if len(each) >= 5:
            each = each[::-1]
            hold.append(each)
        else:
            hold.append(each)
    return " ".join(hold)

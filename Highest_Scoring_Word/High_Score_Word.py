"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.
"""
import string

def high(x):

    letters = list(string.ascii_lowercase)
    nums = range(1, 26)
    mapper = dict(zip(letters, nums))
    word_list = x.split(" ")
    #store total score for each word
    word_score_list = {}
    
    for each in word_list:
        temp_score_holder = []
        for item in each:
            letter_score = mapper.get(item)
            temp_score_holder.append(letter_score)
        word_score_list[each] = sum(temp_score_holder)
    
    return(max(word_score_list.keys(), key=(lambda key: word_score_list[key])))

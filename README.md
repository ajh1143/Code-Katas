# Code Katas: Code Wars!
Solved, Remixed, and Test Driven Practice Challenges
_______________________________________________________________________________________________________________________________________
## Encrypt
```Python3
    """
    For building the encrypted string:
    Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
    Do this n times!
    Examples:
    "This is a test!", 1 -> "hsi  etTi sats!"
    "This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
    """

    def encrypt(text, n):
        if n <= 0:
            return text
        else:
            i = 1
            for each in range(n):
                seconds = []
                leftovers = []
                i = 1
                for x in text:
                    if i%2 == 0:
                        seconds.append(x)
                        i+=1
                    else:
                        i+=1
                        leftovers.append(x)
                        pass
                text = seconds + leftovers
            return("".join(text))
   ```     
## Encrypt: Testing
```Python3
    Test.describe('Basic Tests')
    Test.assert_equals(encrypt("This is a test!", 0), "This is a test!")
    Test.assert_equals(encrypt("This is a test!", 1), "hsi  etTi sats!")
    Test.assert_equals(encrypt("This is a test!", 2), "s eT ashi tist!")
    Test.assert_equals(encrypt("This is a test!", 3), " Tah itse sits!")
    Test.assert_equals(encrypt("This is a test!", 4), "This is a test!")
    Test.assert_equals(encrypt("This is a test!", -1), "This is a test!")
    Test.assert_equals(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")
```
_______________________________________________________________________________________________________________________________________

## Camel Casing 
```Python3
import re

def to_camel_case(text):
    temp = re.split('-|, |_', text)
    final = []
    for each in range(len(temp)):
        if each == 0:
            final.append(temp[0])
        else:
            upperize = temp[each].capitalize()
            final.append(upperize)
    return ''.join(final)
```
## Camel Casing: Tests
```Python3
test.describe("Testing function to_camel_case")
test.it("Basic tests")
test.assert_equals(to_camel_case(''), '', "An empty string was provided but not returned")
test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")
test.assert_equals(to_camel_case('jon-of-the_Snow'), 'jonOfTheSnow', "You know nothing")
test.assert_equals(to_camel_case('Hod-o-r'), 'HodOR', "Hold the door")
```
_______________________________________________________________________________________________________________________________________

## Highest Scoring Word
```Python3
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
```
## Highest Scoring Word: Tests
```Python3
    test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
    test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
    test.assert_equals(high('take me to semynak'), 'semynak')
```
_______________________________________________________________________________________________________________________________________
## Majority Occurance 
```Python3
    """
    Given a list of elements [a1, a2, an], with each ai being a string, write a function majority that returns the value that 
    appears the most in the list. If there's no winner, the function should return None
    """

    from collections import Counter

    class majorityFinder(object):



    def majority(arr):
    """ 
        input: array of letters
        return: unique charset that appears most, None if list empty or a tie
    """
        count=Counter(arr)
        #if arr is empty, return none
        if not count:
            return None
        #find max value in list (# occurances)
        max_value = max(count.values()) 
        #extract key associated with max_value
        parse_max = [key for key, value in count.items() if value == max_value]
        #if there are multiple keys returned, there must be a tie, return none
        if len(parse_max) > 1:
            return None
        return(' '.join(parse_max))
```        
 ## Majority Occurance: Tests
 ```Python3
      test.describe("Find the majority")
      test.it("Base fixed tests")

      test.assert_equals(majority(["A", "B", "A"]), "A")
      test.assert_equals(majority(["A", "BB", "A"]), "A")
      test.assert_equals(majority(["A", "B", "C"]), None)
      test.assert_equals(majority(["A", "B", "B", "A"]), None)
      test.assert_equals(majority(['A','A','A','A']), "A")
      test.assert_equals(majority(['A',]), "A")
      test.assert_equals(majority(['A','A','A','BBBBBBBB']), "A")
      test.assert_equals(majority(["A", "B", "C", "C"]), "C")
      test.assert_equals(majority([]), None)
```      
_______________________________________________________________________________________________________________________________________
## Shortest Words
```Python3
    #Given a string, return the shortest word/words contained within

    def find_short(s):
        store =  []
        for each in s.split():
            cur = len(each)
            store.append(cur)
        low = min(store)
        return low
 ```       
## Shortest Words: Tests
```Python3
    test.describe("Basic Tests")
    test.assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
    test.assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
    test.assert_equals(find_short("lets talk about javascript the best language"), 3)
    test.assert_equals(find_short("i want to travel the world writing code one day"), 1)
    test.assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)
```
    
_______________________________________________________________________________________________________________________________________
## Spin Words
```Python3
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
```       
## Spin Words: Tests
```Python3
    test.assert_equals(spin_words("Welcome"), "emocleW")
    test.assert_equals(spin_words( "Hey fellow warriors" ), "Hey wollef sroirraw") 
    test.assert_equals(spin_words( "This is a test"),  "This is a test" )
    test.assert_equals(spin_words( "This is another test"), "This is rehtona test")
```
_______________________________________________________________________________________________________________________________________  
## Unique Orders
```Python3
    """
    Implement the function unique_in_order which takes as argument a 
    sequence and returns a list of items without any elements with the same value next to each other and preserving the original order 
    of elements.
    """

    def unique_in_order(iterable):
        hold = []
        for index, each in enumerate(iterable):
            cur = each
            if index+1 < len(iterable):
                nxt = iterable[index+1]
                if cur == nxt:
                    pass
                else:
                    hold.append(cur)
            else:
                hold.append(cur)
        return hold
```        
## Unique Orders: Tests
```Python3
    test.assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])
    test.assert_equals(unique_in_order('ABBCcAD'), ['A', 'B', 'C', 'c', 'A', 'D'])
    test.assert_equals(unique_in_order([1,2,2,3,3]), [1,2,3])
```

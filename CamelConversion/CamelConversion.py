"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized (aka Pascal Case). 

Examples:
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
"""
import re
def to_camel_case(text):
    # Split multiple delimeters, build list of elements from text
    temp = re.split('-|, |_', text)
    # Empty list to hold final solution
    final = []
    for each in range(len(temp)):
        # Add first word (the pascal potential case) to final list
        if each == 0:
            final.append(temp[0])
        # For all others, capitalize first letter of each element and add to final list
        else:
            upperize = temp[each].capitalize()
            final.append(upperize)
    # Join final list so that no spaces exist between elements, then return
    return ''.join(final)

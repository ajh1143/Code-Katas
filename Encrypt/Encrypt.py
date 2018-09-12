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
    

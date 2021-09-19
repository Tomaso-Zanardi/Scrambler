# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 21:00:46 2021
@author: Tomaso Zanardi
"""
# this is the main body of mid scrambler this solution was adapted from user Joel Cornet's answer to user Tyler on stack overflow:
# https://stackoverflow.com/questions/15349709/how-can-i-strip-punctuation-from-a-string-and-then-add-it-back-at-the-same-index
def mid_scrambler(text):
    
    """
    
    This function takes a string of text as an input and returns an other srting
    of text, in which every word is randomly scrambled but for the first and
    last letter of every word.
    This function is also sensitive to punctuation and doesn't process it as 
    part of words, leaving it in the original position.
    
    Parameters
    ----------
    text : STRING.

    Returns
    -------
    scrambled_text : STRING.
    
    Examples
    -------
    >mid_scrambler('I was at the concert yesterday, it was great!')
    >'I was at the cnreoct ydateseery, it was garet!'

    """
    # this function as the next ones needs the random and re modules to work, so I created a main function that imports the modules and an inner function that actually does the scrambling
    import random
    import re
    # here is the core of the function, it takes the same argument of the main function and scrambles middle letter of every word of it to then reassemble them, while mantaining the structure of the sentence
    def mid(text):
        word = text.group()
        inner = ''.join(random.sample(word[1:-1], len(word) - 2))
        return'%s%s%s' % (word[0], inner, word[-1])
    scrambled_text =  (re.sub(r'\b\w{3}\w+\b', mid, text))
    return scrambled_text
# also but_first_scrambler was adapted from user Joel Cornet's answer to user Tyler on stack overflow:
# https://stackoverflow.com/questions/15349709/how-can-i-strip-punctuation-from-a-string-and-then-add-it-back-at-the-same-index
def but_first_scrambler(text):
    
    """
    
    This function takes a string of text as an input and returns an other string
    of text, in which every word is randomly scrambled but for the first letter 
    of every word.
    This function is also sensitive to punctuation and doesn't process it as 
    part of words, leaving it in the original position.
    
    Parameters
    ----------
    text : STRING.

    Returns
    -------
    scrambled_text : STRING.
    
    Examples
    -------
    >but_first_scrambler('I was at the concert yesterday, it was great!')
    >'I was at teh cnreotc ydateseeyr, it wsa garte!'

    """
    import random
    import re
    def shuffle_word(m):
        word = m.group()
        inner = ''.join(random.sample(word[1:], len(word) - 1))
        return '%s%s' % (word[0], inner)
    scrambled_text = (re.sub(r'\b\w{2}\w+\b', shuffle_word, text))
    return scrambled_text
# total_scrambler was adapted from a solution proposed by username "t3m2" in response to username "Zara"
# https://stackoverflow.com/questions/53931675/shuffle-words-characters-while-maintaining-sentence-structure-and-punctuations
def total_scrambler(sentence):
    
    """
    
    This function takes a string of text as an input and returns an other string
    of text, in which every word is randomly scrambled.
    This function is also sensitive to punctuation and doesn't process it as 
    part of words, leaving it in the original position.
    
    Parameters
    ----------
    text : STRING.

    Returns
    -------
    scrambled_text : STRING.
    
    Examples
    -------
    >total_scrambler('I was at the concert yesterday, it was great!')
    >'I swa ta hte ncreotc adyteseeyr, ti swa ragte!'

    """
    from random import sample
    scrambled_text = ""
    word=""
    for i,char in enumerate(sentence+' '):
        if char.isalpha():
            word += char
        else:
            if word:
                if len(word) == 1:
                    scrambled_text += word
                else:
                    new_word = ''.join(sample(word,len(word)))
                    if word == word.title():
                        scrambled_text += new_word.title()
                    else:
                        scrambled_text += new_word          
                word=""
            scrambled_text += char
    return scrambled_text



def rand_upper_lower(text):
    
    """
    
    This function takes a string of text as an input and returns an other srting
    of text, in which every word is randomly scrambled but for the first and
    last letter of every word.
    This function is also sensitive to punctuation and doesn't process it as 
    part of words, leaving it in the original position.
    
    Parameters
    ----------
    text : STRING.

    Returns
    -------
    scrambled_text : STRING.
    
    Examples
    -------
    >rand_upper_lower('I was at the concert yesterday, it was great!')
    >'i Was AT ThE cONCeRt YEsTeRDaY, iT wAs GrAeT!'

    """
    import random
    import string
    word1 = ""
    new_word = ""
    for word in text.split():
        word = word + ' '
        for letter in word:
            l = random.randint(0,1)
            if l == 0:
                lett = letter.lower()
                word1 = word1 + lett
            else:
                lett = letter.upper()
                word1 = word1 + lett    
            
    scrambled_text = word1
    return scrambled_text

if __name__ == '__main__':
    testo ='Sono stato al mare, e mi sono dedicato alla pesca subacquea, ma non ho trovato quasi niente. Faceva molto caldo (che è bello) (che ) (che) ( che) ma a volte troppo, che è preoccupante!'
    text = 'Scrambling words is very interesting. Because even if they are scrambled, it does not impact our reading. Because we do not read letter by letter, we read the word as a whole.'
    mid_scrambler('(questo) è un test (test) (tre) (tre) (tre) (cinque) (cinque) cinque cinque tre tre tre ')
    mid_scrambler('lala-lala lala-lala lal-lal lal-lal lal-lala lal-lala ')
    print('----------------\n----------------')
    print(but_first_scrambler(text))
    print('----------------\n----------------')
    print(but_first_scrambler(testo))
    print('----------------\n----------------')
    print(total_scrambler(text))
    print('----------------\n----------------')
    print(total_scrambler(testo))
    print('----------------\n----------------')
    print(rand_upper_lower(text))
    print('----------------\n----------------')
    print(rand_upper_lower(testo))
    print('----------------\n----------------')
    print(mid_scrambler(testo))
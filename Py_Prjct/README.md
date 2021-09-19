***
# README
***

## TLDR; first...

Scrambler.py is a Python script that allows you to scramble text in many different ways.
It is a module and all the different ways in which the script allows you to scramble text are coded separately in different specific functions.

The main functions are 4:

    mid_scrambler

this one is a fuction that scrambles randomly every letter of each word but the first and the last one

    but_first_scrambler

this second function works similarly to the previous one, but it scrambles every letter but the first

    total_scrmbler

as the name suggests, this third function will scramble every word completely (every letter of every word)

    rand_upper_lower

this last function operates a bit differently, it doesn't scramble the order of the letters, but it randomly capitalize some letters or lower case them.

This is just a presentation of the basic features of the module, further in this document you'll find more specifics about the behaviour of each function.

# Getting started
***

## Features

What's in the folder/repository:

* A .txt version of the current documentation


* The word scrambler module, with 4 basic functions as requested by the corse's assignment
  
  
         mid_scrambler
     
        
     
         but_first_scrambler
     
        
     
         total_scrambler
     
        
     
         rand_upper_lower
     
        
     
* integrated testing
  
* An additional script to showcase the behaviour of the functions and to give the possibility to use them effectively to generate scrambled and whacky text

## Requirements

* Editors:

    Although the scripts can be used and tested in the basic python IDLE or in your machine's terminal we suggest you to use a more feature-rich IDE, like Spyder:
    https://www.spyder-ide.org/
    
* modules from the standard library:
  
    `re`, `random`, `os`
    
* Additional libraries or packages:

    to have a more fun experience and to ensure that the testing script works properly install `termcolor`. you can do that very easily by typing `conda install termcolor` in the anaconda terminal.

# scrambler.py 
***

This script is the main interest. It is a module that can be called in any other python script to import the functions it contains, individually or as * (star) import 

## mid_scrambler

This function takes a string of text as an input and returns another srting
    of text, in which every word is randomly scrambled but for the first and
    last letter of every word.
    This function is also sensitive to punctuation and doesn't process it as 
    part of words, leaving it in the original position.

### Arguments

it takes one argument that has to be a string. it can be from a .txt document, or it can be typeded as an argument for the function, or it can be a variable with an assigned string. 

### Returns

`mid_scrambler` returns a string containing the original text scrambled for every letter but the first and last of each word. It is sensitive to punctuation, therefore it mantains the punctuation from the input text in the same position when it returns it scrambled.

### Examples

1. Here you can see how you can use `mid_scrambler` writing a string to scramble directly as the argumument of the function, in your script, or in the command line.


```python
from scrambler import *
mid_scrambler('sono stato a trovare la nonna')
```




    'sono sttao a tvrroae la nnona'



2. you can give a variable previously assigned with a string as argument


```python
from scrambler import mid_scrambler
a = 'I went to grandma\'s house to visit her'
print(mid_scrambler(a))
```

    I wnet to gndamra's hosue to viist her


3. the argument can be a variable assigned with the content of a specific file, like the test_text.txt file in this example


```python
f = open('testo_di_prova.txt',mode='r')
test_text_file = f.read()
f.close()
from scrambler import mid_scrambler
print(mid_scrambler(test_text_file))
```


    This txet was wtterin in sdyepr, not unisg nepoatd, vi, vim, or any ohetr eotidr


## but_first_scrambler

Similarly to the previous one, this function takes a string of text as an input and returns another srting of text, in which every word is randomly scrambled but for the first (**and only the first!**) letter. This function is also sensitive to punctuation and doesn't process it as part of words, leaving it in the original position.

### Arguments

as for the previous function , `but_first_scrambler` takes one argument that has to be a string. it can be from a .txt document, or it can be typeded as an argument for the function, or it can be a variable with an assigned string.

### Returns

`but_first_scrambler` returns a string containing the original text scrambled for every letter but the first of each word. It is sensitive to punctuation, therefore it mantains the punctuation from the input text in the same position when it returns it scrambled.

### Examples

1. Here you can see how you can use `but_first_scrambler` writing the text to scramble directly in your script or in the command line.


```python
from scrambler import but_first_scrambler
but_first_scrambler('sono stato a trovare la zia')
```

    sono satto a tvreoar la zia 


2. you can give a variable previously assigned with a string as argument.


```python
a = 'I went to my aunt\'s house to visit her'
mid_scrambler(a)
```

    I went to my an'tus huose to viist her 


3. the argument can be a variable assigned with the content of a specific file, like the test_text.txt file in this example.


```python
f = open('testo_di_prova.txt',mode='r')
test_text_file = f.read()
f.close()
but_first_scrambler(test_text_file)
```

    Thsi text wsa wnreitt in spedry, not ugisn nepatdo, vi, vim, or any orthe eirotd 


## total_scrambler

Similarly to what we saw for previous functions, this one takes a string of text as an input and returns another srting of text, in which every word is randomly scrambled (**every letter of every word...a big mess!**) letter. This function is also sensitive to punctuation and doesn't process it as part of words, leaving it in the original position.

### Arguments

as for previous functions , `total_scrambler` takes one argument that has to be a string. It can be from a .txt document, it can be typeded as an argument for the function, or it can be a variable with an assigned string.

### Returns

`total_scrambler` returns a string containing the original text scrambled, every letter of each word can be in the wrong place. It is sensitive to punctuation, therefore it mantains the punctuation from the input text in the same position when it returns it scrambled.

### Examples

1. Here you can see an example on how to use `total_scrambler` writing the text to scramble directly in your script or in the command line.


```python
from scrambler import total_scrambler
total_scrambler('sono stato a trovare la cugina')
```

    snoo attos a rvtreoa la ngcaui 


2. or you can give a variable previously assigned with a string as argument


```python
a = 'I went to my cousin\'s house to visit her'
total_scrambler(a)
```

    I wnte to ym i'coussn sehuo to svtii erh 


3. or the argument can be a variable assigned with the content of a specific file, like the .txt file in this example


```python
f = open('testo_di_prova.txt',mode='r')
test_text_file = f.read()
f.close()
total_scrambler(test_text_file)
```

    hsTi ttxe saw tnietwr in pyreds, ont nsigu tondepa, iv, mvi, or ayn ohert deitor 


## rand_upper_lower

This time things are slightly different. This function takes a string of text as an input and returns another string of text, in which every letter ir randomly capitalized or lower-cased. This function, as the previous ones, is also sensitive to punctuation and doesn't process it as part of words, leaving it in the original position.

### Arguments

as for previous functions , `rand_upper_lower` takes one argument that has to be a string, from .txt document, it can be typeded as an argument for the function, or it can be a variable with an assigned string.

### Returns

`rand_upper_lower` returns a string containing the original text scrambled, every letter of each word can be in the wrong place. It is sensitive to punctuation, therefore it mantains the punctuation from the imput text in the same position when it returns it scrambled.

### Examples

1. Here you can see an example on how to use `rand_upper_lower` writing the text to scramble directly in your script or in the command line.


```python
from scrambler import rand_upper_lower
rand_upper_lower('sono stato a trovare la cugina')
```




    'sOno sTATO a TroVarE LA CuGINA '



2. or you can give a variable previously assigned with a string as argument.


```python
a = 'I went to my cousin\'s house to visit her'
print(rand_upper_lower(a))
```

    i wEnT to My cousIN's HouSe to ViSit hEr 


3. or the argument can be a variable assigned with the content of a specific file, like the .txt file in this example


```python
f = open('testo_di_prova.txt',mode='r')
test_text_file = f.read()
f.close()
print(rand_upper_lower(test_text_file))
```

    thIS tExT WAs wrITtEn iN sPYDer, Not uSing nOTEPAd, VI, VIM, or anY otheR edItor 


# test_scrambler.py

test_scrambler.py is a python script that offers to the user the possibility of testing and using the functions of the scrambler module.

## How does it works?

Once run, the program greets the user with a message that also explains the initial two basic choices that are given:

1. to load a text from a text file

2. to write a text than can then be manipulated

the user has to input the string 'open' if he chooses option 1. and the string 'scramble' if he wants to write a new text in the console, for the script to scramble.

* If he chooses first option the program will ask for the name of the file from which to extract the text. It will also issue a warning message, advising the user to either have the desired text file in the working directory or to specify the full path of the file.

* If instead the second option is chosen the program will ask the user to input the text to be scrambled.

At this point the user is presented with the option to manipulate the text according to Scrambler.py's basic functions. It is possible to produced a text scrambled by any of the functions or by them all.

Lastly the user is given the possibility to choose if he wants the scrambled text printed in the console, saved in a new text file, or both.
Unless the user chooses to have the text only printed the program will ask one last input from the user which is the name of the file in which the text will be written. the file will be saved in the working directory, therefore if a file with the same name already exists in that directory, an error message will be issued, asking the user to find another name.


# Final notes & Credits

to have a better experience whie using scrambler.py and test_scrambler.py we suggest you:

- to have the ToC extension for Jupiter installed, to be able to consult the .ipynb version of the current documentation with agility

- to use the spyder IDE to run the scripts, with the termcolor module installed, so that you'll have more fun and so that the colored output is properly visualized (if you open the scripts in a terminal that's not guaranteed)


Some of the functions built in scrambler.py were adapted by solutions found in stackoverflow.com threads:

- `mid_scrambler` and `but_first scrambler` were adapted from a solution proposed by username "Joel Cornet" in response to a thread opened by username "Tyler" https://stackoverflow.com/questions/15349709/how-can-i-strip-punctuation-from-a-string-and-then-add-it-back-at-the-same-index

- `total_scrambler` could have implemented by the same solution but for variety's sake I preferred to use and adapt a solution proposed by username "t3m2" in a thread opened by username "Zara" https://stackoverflow.com/questions/53931675/shuffle-words-characters-while-maintaining-sentence-structure-and-punctuations


```python

```

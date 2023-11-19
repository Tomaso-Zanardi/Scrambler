{
 "cells": [
  {
   "attachments": {
    "Ducati-Scrambler-logo-design-3.jpg": {
     "image/jpeg": "/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/2wBDAQMEBAUEBQkFBQkUDQsNFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBT/wAARCAFCAgoDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD8qqKK/qooA/lXor+qiigD+Veiv6qKKAP5V6K/qoooA/lXor+qiigD+Veiv6qKKAP5V6K/qoooA/lXor+qiigD+Veiv6qKKAP5V6K/qoooA/lXor+qiigD+Veiv6qKKAP5V6K/qoooA/lXor+qiigD+Veiv6qKKAP5V6K/qoooA/lXor+qiigD+Veiv6qKKAP5V6K/qoooA/lXor+qiigD+Veiv6qKKAP5V6K/qoooA/lXor+qiigD+Veiv6qKKAP5V6K/qoooA/lXor+qiigD+Veiv6qKKAP5V6K/qoooA/lXor+qiigD+Veiv6qKKAP5V6K/qoooA/lXor+qiigD+Veivqr/AIKjf8n2fE3/ALhn/pstK+VaACv6qK/lXr+qigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA/AH/AIKjf8n2fE3/ALhn/pstK+Va+qv+Co3/ACfZ8Tf+4Z/6bLSvlWgAr+qiv5V6/qooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAPwB/4Kjf8AJ9nxN/7hn/pstK+Va+qv+Co3/J9nxN/7hn/pstK+VaACv6qK/lXr+qigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA/AH/gqN/yfZ8Tf+4Z/6bLSvlWvqr/gqN/yfZ8Tf+4Z/wCmy0r5VoAK/qor+Vev6qKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD8Af+Co3/J9nxN/7hn/AKbLSvlWvqr/AIKjf8n2fE3/ALhn/pstK+VaACv6qK/lXr+qigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA/AH/AIKjf8n2fE3/ALhn/pstK+Va+qv+Co3/ACfZ8Tf+4Z/6bLSvlWgAr+qiv5V6/qooAKKKKACiiigAoooo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IXq0OkyzD80Br+j+igD+ZHUvgX8SdFydQ+H3iqwA6/adFuY/zygrlb/QdT0tiL3Tru0I6i4gZD+OQK/qYqGa3juV2yxJKn911BH5EUAfyu0V/UFqXw18Ia1kah4U0S/z1+06dDJ+eVNclq37LPwa1sN9t+FPgy4J6s2g2oP5hAaAP5qqK/om1L9gP9nrVt3n/CfQI8/8+sbwfl5bLiq/hn/gn3+z14Q1qDVdO+F2km8gYSR/bJZ7uMMDkHy5pHQkEcZHFAHgH/BIX9my5+Gfwt1T4j69YPaa54tKxWCTptePTUOVYAjIErktjuscZHWv0JqKOMRqFAAQAAKvAAHQCpaACiiigAooooA/AH/gqN/yfZ8Tf+4Z/wCmy0r5Vr6q/wCCo3/J9nxN/wC4Z/6bLSvlWgAr+qiv5V6/qooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAPwB/wCCo3/J9nxN/wC4Z/6bLSvlWvqr/gqN/wAn2fE3/uGf+my0r5VoAK/qor+Vev6qKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD8Af+Co3/ACfZ8Tf+4Z/6bLSvlWvqr/gqN/yfZ8Tf+4Z/6bLSvlWgAr+qiv5V6/qooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAPwB/4Kjf8n2fE3/uGf+my0r5Vr6q/4Kjf8n2fE3/uGf8ApstK+VaACv6qK/lXr+qigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA/AH/gqN/yfZ8Tf+4Z/wCmy0r5Vr6q/wCCo3/J9nxN/wC4Z/6bLSvlWgAr+qiv5V6/qooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAPwB/wCCo3/J9nxN/wC4Z/6bLSvlWvqr/gqN/wAn2fE3/uGf+my0r5VoAK/qor+VevVf+Gsfjf8A9Fk+IH/hUX3/AMdoA/pTor+az/hrH43/APRZPiB/4VF9/wDHaP8AhrH43/8ARZPiB/4VF9/8doA/pTor+az/AIax+N//AEWT4gf+FRff/HaP+Gsfjf8A9Fk+IH/hUX3/AMdoA/pTor+az/hrH43/APRZPiB/4VF9/wDHaP8AhrH43/8ARZPiB/4VF9/8doA/pTor+az/AIax+N//AEWT4gf+FRff/HaP+Gsfjf8A9Fk+IH/hUX3/AMdoA/pTor+az/hrH43/APRZPiB/4VF9/wDHaP8AhrH43/8ARZPiB/4VF9/8doA/pTor+az/AIax+N//AEWT4gf+FRff/HaP+Gsfjf8A9Fk+IH/hUX3/AMdoA/pTor+az/hrH43/APRZPiB/4VF9/wDHaP8AhrH43/8ARZPiB/4VF9/8doA/pTor+az/AIax+N//AEWT4gf+FRff/HaP+Gsfjf8A9Fk+IH/hUX3/AMdoA/pTor+az/hrH43/APRZPiB/4VF9/wDHaP8AhrH43/8ARZPiB/4VF9/8doA/pTor+az/AIax+N//AEWT4gf+FRff/HaP+Gsfjf8A9Fk+IH/hUX3/AMdoA/pTor+az/hrH43/APRZPiB/4VF9/wDHaP8AhrH43/8ARZPiB/4VF9/8doA/pTor+az/AIax+N//AEWT4gf+FRff/HaP+Gsfjf8A9Fk+IH/hUX3/AMdoA/pTor+az/hrH43/APRZPiB/4VF9/wDHaP8AhrH43/8ARZPiB/4VF9/8doA/pTor+az/AIax+N//AEWT4gf+FRff/HaP+Gsfjf8A9Fk+IH/hUX3/AMdoA/pTor+az/hrH43/APRZPiB/4VF9/wDHaP8AhrH43/8ARZPiB/4VF9/8doA/pTor+az/AIax+N//AEWT4gf+FRff/HaP+Gsfjf8A9Fk+IH/hUX3/AMdoA/pTor+az/hrH43/APRZPiB/4VF9/wDHaP8AhrH43/8ARZPiB/4VF9/8doA/pTor+az/AIax+N//AEWT4gf+FRff/HaP+Gsfjf8A9Fk+IH/hUX3/AMdoA/pTor+az/hrH43/APRZPiB/4VF9/wDHaP8AhrH43/8ARZPiB/4VF9/8doA/pTor+az/AIax+N//AEWT4gf+FRff/HaP+Gsfjf8A9Fk+IH/hUX3/AMdoA/pTor+az/hrH43/APRZPiB/4VF9/wDHaP8AhrH43/8ARZPiB/4VF9/8doA/pTor+az/AIax+N//AEWT4gf+FRff/HaP+Gsfjf8A9Fk+IH/hUX3/AMdoA/pTor+az/hrH43/APRZPiB/4VF9/wDHaP8AhrH43/8ARZPiB/4VF9/8doA/pTor+az/AIax+N//AEWT4gf+FRff/HaP+Gsfjf8A9Fk+IH/hUX3/AMdoA/pTor+az/hrH43/APRZPiB/4VF9/wDHaP8AhrH43/8ARZPiB/4VF9/8doA/pTor+az/AIax+N//AEWT4gf+FRff/HaP+Gsfjf8A9Fk+IH/hUX3/AMdoA/pTor+az/hrH43/APRZPiB/4VF9/wDHaP8AhrH43/8ARZPiB/4VF9/8doA/pTor+az/AIax+N//AEWT4gf+FRff/HaP+Gsfjf8A9Fk+IH/hUX3/AMdoA/pTor+az/hrH43/APRZPiB/4VF9/wDHaP8AhrH43/8ARZPiB/4VF9/8doA/pTor+az/AIax+N//AEWT4gf+FRff/HaP+Gsfjf8A9Fk+IH/hUX3/AMdoA/pTor+az/hrH43/APRZPiB/4VF9/wDHaP8AhrH43/8ARZPiB/4VF9/8doA9V/4Kjf8AJ9nxN/7hn/pstK+Va2vGHjbXviF4iuNe8T6vea/rdykST6hqEzTTzCONYk3uxyxCIq5JyccmsWgAooooAKKKKACiiigAooooAKKKKACiiigCaxUNeQKwDKXUEHoea9fbQdM+whv7OtN23r5C5/lRRQBwHiizgt1byoY4uR9xAK5miigAooooAKKKKACiiigAooooAKKKKACup1Gzt4/hf4fu1gjW6l1nUopJwgDuiwWJVS3UgF3IHbc3qaKKAOWp0nDGiigBtFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQBNEoMWSATmnKo9B+VFFAFeiiigAooooAfCAWORniptq/3R+VFFABtX+6Pyo2r/AHR+VFFADb1QtxhQANiHgf7IqCiigAooooA//9k="
    }
   },
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![Ducati-Scrambler-logo-design-3.jpg](attachment:Ducati-Scrambler-logo-design-3.jpg)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "***\n",
    "# README\n",
    "***"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## TLDR; first..."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Scrambler.py is a Python script that allows you to scramble text in many different ways.\n",
    "It is a module and all the different ways in which the script allows you to scramble text are coded separately in different specific functions.\n",
    "\n",
    "The main functions are 4:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "    mid_scrambler"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "this one is a fuction that scrambles randomly every letter of each word but the first and the last one"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "    but_first_scrambler"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "this second function works similarly to the previous one, but it scrambles every letter but the first"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "    total_scrmbler"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "as the name suggests, this third function will scramble every word completely (every letter of every word)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "    rand_upper_lower"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "this last function operates a bit differently, it doesn't scramble the order of the letters, but it randomly capitalize some letters or lower case them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This is just a presentation of the basic features of the module, further in this document you'll find more specifics about the behaviour of each function."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Getting started\n",
    "***"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Features"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What's in the folder/repository:\n",
    "\n",
    "* A .txt version of the current documentation\n",
    "\n",
    "\n",
    "* The word scrambler module, with 4 basic functions as requested by the corse's assignment\n",
    "    \n",
    "    \n",
    "         mid_scrambler\n",
    "        \n",
    "        \n",
    "         but_first_scrambler\n",
    "        \n",
    "        \n",
    "         total_scrambler\n",
    "        \n",
    "        \n",
    "         rand_upper_lower\n",
    "        \n",
    "        \n",
    "        \n",
    "* integrated testing\n",
    "    \n",
    "    \n",
    "* An additional script to showcase the behaviour of the functions and to give the possibility to use them effectively to generate scrambled and whacky text"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Requirements"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Editors:\n",
    "\n",
    "    Although the scripts can be used and tested in the basic python IDLE or in your machine's terminal we suggest you to use a more feature-rich IDE, like Spyder:\n",
    "    https://www.spyder-ide.org/\n",
    "    \n",
    "* modules from the standard library:\n",
    "    \n",
    "    `re`, `random`, `os`\n",
    "    \n",
    "    \n",
    "* Additional libraries or packages:\n",
    "\n",
    "    to have a more fun experience and to ensure that the testing script works properly install `termcolor`. you can do that very easily by typing `conda install termcolor` in the anaconda terminal."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# scrambler.py \n",
    "*** "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This script is the main interest. It is a module that can be called in any other python script to import the functions it contains, individually or as * (star) import "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## mid_scrambler"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This function takes a string of text as an input and returns another srting\n",
    "    of text, in which every word is randomly scrambled but for the first and\n",
    "    last letter of every word.\n",
    "    This function is also sensitive to punctuation and doesn't process it as \n",
    "    part of words, leaving it in the original position."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Arguments"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "it takes one argument that has to be a string. it can be from a .txt document, or it can be typeded as an argument for the function, or it can be a variable with an assigned string. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Returns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`mid_scrambler` returns a string containing the original text scrambled for every letter but the first and last of each word. It is sensitive to punctuation, therefore it mantains the punctuation from the input text in the same position when it returns it scrambled."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Examples"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. Here you can see how you can use `mid_scrambler` writing a string to scramble directly as the argumument of the function, in your script, or in the command line."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'snoo stato a tovarre la nnnoa'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from scrambler import *\n",
    "mid_scrambler('sono stato a trovare la nonna')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. you can give a variable previously assigned with a string as argument"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I wnet to gardmna's house to viist her\n"
     ]
    }
   ],
   "source": [
    "from scrambler import mid_scrambler\n",
    "a = 'I went to grandma\\'s house to visit her'\n",
    "print(mid_scrambler(a))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. the argument can be a variable assigned with the content of a specific file, like the test_text.txt file in this example"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Tihs txet was wtrtien in sdepyr, not usnig natpeod, vi, vim, or any ohter eidotr\n"
     ]
    }
   ],
   "source": [
    "f = open('testo_di_prova.txt',mode='r')\n",
    "test_text_file = f.read()\n",
    "f.close()\n",
    "from scrambler import mid_scrambler\n",
    "print(mid_scrambler(test_text_file))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## but_first_scrambler"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Similarly to the previous one, this function takes a string of text as an input and returns another srting of text, in which every word is randomly scrambled but for the first (**and only the first!**) letter. This function is also sensitive to punctuation and doesn't process it as part of words, leaving it in the original position."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Arguments"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "as for the previous function , `but_first_scrambler` takes one argument that has to be a string. it can be from a .txt document, or it can be typeded as an argument for the function, or it can be a variable with an assigned string."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Returns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`but_first_scrambler` returns a string containing the original text scrambled for every letter but the first of each word. It is sensitive to punctuation, therefore it mantains the punctuation from the input text in the same position when it returns it scrambled."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Examples"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. Here you can see how you can use `but_first_scrambler` writing the text to scramble directly in your script or in the command line."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'sono sttao a troreva la zia'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from scrambler import but_first_scrambler\n",
    "but_first_scrambler('sono stato a trovare la zia')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. you can give a variable previously assigned with a string as argument."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"I wnet to my anut's huose to viist her\""
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = 'I went to my aunt\\'s house to visit her'\n",
    "mid_scrambler(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. the argument can be a variable assigned with the content of a specific file, like the test_text.txt file in this example."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\nThsi ttxe wsa wretnti in sdyerp, not unisg ndoeatp, vi, vim, or ayn otehr etoird'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f = open('testo_di_prova.txt',mode='r')\n",
    "test_text_file = f.read()\n",
    "f.close()\n",
    "but_first_scrambler(test_text_file)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## total_scrambler"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Similarly to what we saw for previous functions, this one takes a string of text as an input and returns another srting of text, in which every word is randomly scrambled (**every letter of every word...a big mess!**) letter. This function is also sensitive to punctuation and doesn't process it as part of words, leaving it in the original position."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Arguments"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "as for previous functions , `total_scrambler` takes one argument that has to be a string. It can be from a .txt document, it can be typeded as an argument for the function, or it can be a variable with an assigned string."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Returns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`total_scrambler` returns a string containing the original text scrambled, every letter of each word can be in the wrong place. It is sensitive to punctuation, therefore it mantains the punctuation from the input text in the same position when it returns it scrambled."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Examples"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. Here you can see an example on how to use `total_scrambler` writing the text to scramble directly in your script or in the command line."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'onso taost a vartreo la uaigcn '"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from scrambler import total_scrambler\n",
    "total_scrambler('sono stato a trovare la cugina')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. or you can give a variable previously assigned with a string as argument"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"I went to ym ncuois's suoeh to itivs her \""
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = 'I went to my cousin\\'s house to visit her'\n",
    "total_scrambler(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. or the argument can be a variable assigned with the content of a specific file, like the .txt file in this example"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\nShit ttex asw wrtinet in seyrpd, nto suing atnpdeo, iv, imv, or yan eroht eoitdr '"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f = open('testo_di_prova.txt',mode='r')\n",
    "test_text_file = f.read()\n",
    "f.close()\n",
    "total_scrambler(test_text_file)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## rand_upper_lower"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This time things are slightly different. This function takes a string of text as an input and returns another string of text, in which every letter ir randomly capitalized or lower-cased. This function, as the previous ones, is also sensitive to punctuation and doesn't process it as part of words, leaving it in the original position."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Arguments"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "as for previous functions , `rand_upper_lower` takes one argument that has to be a string, from .txt document, it can be typeded as an argument for the function, or it can be a variable with an assigned string."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Returns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`rand_upper_lower` returns a string containing the original text scrambled, every letter of each word can be in the wrong place. It is sensitive to punctuation, therefore it mantains the punctuation from the imput text in the same position when it returns it scrambled."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Examples"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. Here you can see an example on how to use `rand_upper_lower` writing the text to scramble directly in your script or in the command line."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'SonO StAto a trOVAre LA CugINA '"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from scrambler import rand_upper_lower\n",
    "rand_upper_lower('sono stato a trovare la cugina')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. or you can give a variable previously assigned with a string as argument."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i Went TO My CoUSIn'S hoUSe TO ViSIt hER \n"
     ]
    }
   ],
   "source": [
    "a = 'I went to my cousin\\'s house to visit her'\n",
    "print(rand_upper_lower(a))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. or the argument can be a variable assigned with the content of a specific file, like the .txt file in this example"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this TEXt WaS WriTTeN IN SPYder, Not uSINg nOTEPaD, Vi, ViM, oR aNY oTHER EdiTOR \n"
     ]
    }
   ],
   "source": [
    "f = open('testo_di_prova.txt',mode='r')\n",
    "test_text_file = f.read()\n",
    "f.close()\n",
    "print(rand_upper_lower(test_text_file))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# test_scrambler.py\n",
    "***"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "test_scrambler.py is a python script that offers to the user the possibility of testing and using the functions of the scrambler module."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## How does it works?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Once run, the program greets the user with a message that also explains the initial two basic choices that are given:\n",
    "\n",
    "1. to load a text from a text file\n",
    "\n",
    "2. to write a text than can then be manipulated\n",
    "\n",
    "the user has to input the string 'open' if he chooses option 1. and the string 'scramble' if he wants to write a new text in the console, for the script to scramble."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* If he chooses first option the program will ask for the name of the file from which to extract the text. It will also issue a warning message, advising the user to either have the desired text file in the working directory or to specify the full path of the file.\n",
    "\n",
    "* If instead the second option is chosen the program will ask the user to input the text to be scrambled.\n",
    "\n",
    "At this point the user is presented with the option to manipulate the text according to Scrambler.py's basic functions. It is possible to produced a text scrambled by any of the functions or by them all.\n",
    "\n",
    "Lastly the user is given the possibility to choose if he wants the scrambled text printed in the console, saved in a new text file, or both.\n",
    "Unless the user chooses to have the text only printed the program will ask one last input from the user which is the name of the file in which the text will be written. the file will be saved in the working directory, therefore if a file with the same name already exists in that directory, an error message will be issued, asking the user to find another name.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Final notes & Credits\n",
    "***"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "to have a better experience whie using scrambler.py and test_scrambler.py we suggest you:\n",
    "\n",
    "- to have the ToC extension for Jupiter installed, to be able to consult the .ipynb version of the current documentation with agility\n",
    "\n",
    "- to use the spyder IDE to run the scripts, with the termcolor module installed, so that you'll have more fun and so that the colored output is properly visualized (if you open the scripts in a terminal that's not guaranteed)\n",
    "\n",
    "\n",
    "Some of the functions built in scrambler.py were adapted by solutions found in stackoverflow.com threads:\n",
    "\n",
    "- `mid_scrambler` and `but_first scrambler` were adapted from a solution proposed by username \"Joel Cornet\" in response to a thread opened by username \"Tyler\" https://stackoverflow.com/questions/15349709/how-can-i-strip-punctuation-from-a-string-and-then-add-it-back-at-the-same-index\n",
    "\n",
    "- `total_scrambler` could have implemented by the same solution but for variety's sake I preferred to use and adapt a solution proposed by username \"t3m2\" in a thread opened by username \"Zara\" https://stackoverflow.com/questions/53931675/shuffle-words-characters-while-maintaining-sentence-structure-and-punctuations"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": true
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
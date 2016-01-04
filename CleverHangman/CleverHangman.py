'''
Created on Nov 5, 2015

@author: tedmarchildon
'''
import random

def loadWords(filename):
    """
    read words from specified file and return a list of
    strings, each string is one line of the file
    """
    
    allwords = []
    f = open(filename)
    for line in f:
        line = line.strip()
        allwords.append(line)
    f.close()
    return allwords
    
     
def getWords(allwords,wordlength):
    """
    returns a list of words having a specified length from
    allwords
    """
    wlist = [w for w in allwords if len(w) == wordlength]
    return wlist

def display(guess):
    '''
    create a string from list guess to print/show user
    '''
    return ' '.join(guess)

def categorize(words, guess):
    '''
    creates a dictionary in which each key is a possible template for a word given the 
    letter guessed and each value is a list of all the words that fit that template
    given the letter guessed.
    '''
    d = {}
    for word in words:
        lst = list(word)
        for i in range(len(lst)):
            if lst[i] != guess:
                lst[i] = "_"
        l = "".join(lst)
        if l not in d:
            d[l] = [word]
        else:
            d[l].append(word)
    return d

def most(d):
    '''
    Finds which key in the dictionary returned by categorize has the most words to choose
    from, and returns that list of words
    '''
    best = 0
    words = []
    for v in d.values():
        if len(v) > best:
            best = len(v)
            words = v
    return words

def makeSecretList(secret):
    '''
    Create the list that's modifiable to track letters 
    guessed by user
    '''
    x = []
    for ch in secret:
        if ch.isalpha():
            x.append("_")
        else:
            x.append(ch)
    return x

def doGame(word, words): 
    '''
    Takes a string from the file that we read in, takes letters guessed
    by the user and lets the user know if the guess is in the word, also tells the user
    what letters they haven't guessed, and how many misses they have left.
    '''
    guess = makeSecretList(word)
    misses = 0
    guessed = set()
    not_guessed = list("abcdefghijklmnopqrstuvwxyz")
    while True:
        if guess.count('_') == 0:
            break
        if misses == 8:
            break
        print "secret so far:",display(guess)
        letter = raw_input("guess a letter: ")
        letter = letter.lower()
        d = categorize(words, letter)
        words = most(d)
        word = random.choice(words)
        if gametype == "t":
            ret = {}
            for key in d:
                ret[key] = len(d[key])
            print "The categories are: ", ret
            print "The secret word is: " + word
        print "words left:", len(words)
        for index in range(len(word)):
            if word[index].lower() == letter.lower():
                guess[index] = word[index]
        if letter.lower() not in guessed and letter.lower() not in word.lower():
            misses += 1
        guessed.add(letter)
        if letter.lower() in not_guessed:
            not_guessed.remove(letter.lower())
        misses_remaining = 8 - misses
        print "You haven't guessed these letters:", ' '.join(not_guessed)
        print "You have", misses_remaining,"misses remaining"
    if guess.count("_") == 0:
        print "word is guessed!",word
    else:
        print "you lost! word is",word
 
def play(allwords):
    global gametype
    gametype = raw_input("Testing mode or Playing mode? (t or p) ")
    wlen = int(raw_input("how many letters in word you'll guess? "))
    if wlen < 3:
        print "Length of word must be equal to or greater than 3!"
    else:
        words = getWords(allwords,wlen)    
        word = random.choice(words)
        doGame(word, words)

if __name__ == '__main__':
    allwords = loadWords("lowerwords.txt")
    play(allwords)
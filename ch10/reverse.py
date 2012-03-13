""" Find reverse pairs in a list of > 11.000 words 
This is pronably not a good way of doing this. I create a list that itself contains lists, each of which contains words of a certain length. Then iterating over the crosswords list, I check each word against the list that contains words of the same length 
It works, but takes absolutely ages
"""

def make_word_list1():
    t = []
    fin = open('../CROSSWD.TXT')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

testlist = ['aardvark','biene','gecko','hund','laus','wildschwein','wolf'] 

""" finding the length of the longest words """
def maxlength(t):
    maxlength = 0
    for x in t:
        if len(x) > maxlength:
            maxlength = len(x)
    return maxlength

wordlist = make_word_list1()

def create_numberedlists(t):
    maxl =  maxlength(t)
    ueberlist = []
    for i in range(maxl):
        ueberlist.append([])
    return ueberlist

#print create_numberedlists(wordlist)

def sort_by_numbers(t):
    ueberlist = create_numberedlists(t)
    for x in t:
        index = len(x)-1
        ueberlist[index].append(x)
    return ueberlist

ueberlist = sort_by_numbers(wordlist)

   
def create_reverse(word):
    rev_word = ''
    last = len(word)-1
    for i in range(len(word)):
        rev_word += word[last-i]
    return rev_word

def bisect_search(t,word):            
    half = len(t)/2
    pos = half
    searchlist = t[:]
    while searchlist[half] != word:
        t1 = searchlist[:half]
        t2 = searchlist[half:]
        if(word < searchlist[half]):
            searchlist = t1[:] 
            shiftpos = -len(searchlist)/2       
        else:
            searchlist = t2[:]
            shiftpos = +len(searchlist)/2
        half = len(searchlist)/2
        pos += shiftpos
        if half == 0:
           return False
    if(searchlist[half] == word):
        return word


def list_reverse(t):
    ueberlist = sort_by_numbers(t)
    rev_pairs = []
    for x in t:
        length = len(x)
        rev_word = create_reverse(x)
        partner = bisect_search(ueberlist[length-1], rev_word)
        if partner == rev_word:
            pair = [x, partner]
            rev_pairs.append(pair)
    return rev_pairs

wordlist = make_word_list1()
rev_pairs = list_reverse(wordlist)
print rev_pairs 
print len(rev_pairs)


"""  5/3/2012  (this finds 884 pairs)  """







""" Some things I didn't use in the end """

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2)-1    
    while j >= 0:
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
    return True

"""
if is_reverse('stop','pots'):
    print 'True'
else:
    print 'False'
"""


""" generating a list of letters of the alphabet 
import string
abc_list = list(string.ascii_lowercase)

"""
"""
temp1 = []
temp2 = []
for x in sub_list:
    if x[0] == 'a':
        temp1.append(x)
    if x[-1] == 'a':
        temp2.append(x)
""" 

        

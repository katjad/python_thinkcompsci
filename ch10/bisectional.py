"""

Binary Search


"""


def make_word_list1():
    t = []
    fin = open('../CROSSWD.TXT')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

#testlist = ['aardvark','biene','gecko','hund','laus','wildschwein','wolf']

""" trying things out

word = 'gecko'
half = len(testlist)/2
pos = half
searchlist = testlist[:]
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
       print "Word not found"
       break
if(searchlist[half] == word):
    print "Word "+word+" found in position "+str(pos)    

"""

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
           print "Word '"+word+"' not found"
           return
    if(searchlist[half] == word):
        print "Word '"+word+"' found in position "+str(pos)
        return

t = make_word_list1()
bisect_search(t, 'huffelpuff')
bisect_search(t, 'world')
bisect_search(t, 'function')

print "First word in the list: "+str(t[0])
print "Last word in the list: "+str(t[len(t)-1])




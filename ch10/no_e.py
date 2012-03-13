def has_no_e(word):
    word = word.lower()
    length = len(word)
    index = 0
    while index < length:
        if word[index] == 'e':
            return False
        index += 1
    return True

#print has_no_e('Weihnachten')
#print has_no_e('Eland')
#print has_no_e('Matin')

def eless_words():
    fin = open('../CROSSWD.TXT')
    count_all = 0
    count_no_e = 0
    for line in fin:
        word = line.strip()
        if has_no_e(word):
            print word
            count_no_e += 1
        count_all += 1
    percent_eless = (float(count_no_e)/ count_all) * 100
    print str(count_no_e) + ' words out of '+ str(count_all) + ' have no e, ' + str(percent_eless) + ' %.'
    
eless_words()
    

def editDistance(str0, str1, lstr0, lstr1):
    
    if lstr0 == 0:
        return lstr1
    
    if lstr1 == 0:
        return lstr0

    if str0[lstr0 - 1] == str1[lstr1 -1]:
        return editDistance(str0, str1, lstr0 -1, lstr1 -1)

    return 1 + min(
                #Insert
                editDistance(str0, str1, lstr0, lstr1 - 1),
                #delete
                editDistance(str0, str1, lstr0 - 1, lstr1),
                #replace
                editDistance(str0, str1, lstr0 - 1, lstr1 - 1))

def printResult(s0, s1):
    str0 = s0
    str1 = s1
    print ('-' * 30)
    print("Words:\t%s\t%s"%(str0, str1))
    print("EditDistance: %d\n" % editDistance(str0, str1, len(str0), len(str1)))
    print ('-' * 30)
def getWords(fileName):
    f = open(fileName, "r")
    for l in f:
        #We are going to assume that the words are going to be seperated by the a space
        w = l.split(" ")
        printResult(w[0], w[1])

getWords("words.txt")
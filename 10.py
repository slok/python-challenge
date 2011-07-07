#Look-and-say sequence -> http://en.wikipedia.org/wiki/Look-and-say_sequence
#python-challenge(http://www.pythonchallenge.com/) level 10

#We have: a = [1, 11, 21, 1211, 111221, . This is Look and say sequence
#           then also we have len(a[30]), so the size number 30 of the sequence is the solution
#solution: 5808
a = ['1']
maxNum  = 31

digitCont = {} #digit:times
resStr = ''
i = 0

while i <= maxNum:
    aux = a[i]
    
    actIndex = aux[0]
    digitCont[actIndex] = 1
    j = 1 
    resStr = ''
    #check for each digit
    while True:
        if  j == len(aux):
            resStr = resStr + str(digitCont[actIndex]) + str(actIndex)
            break
        elif actIndex != aux[j]: #different digit? set the times and the past digit and go with the new one
            resStr = resStr + str(digitCont[actIndex]) + str(actIndex)
            actIndex = aux[j]
            digitCont[actIndex] = 1
        else:# same digit? +1 times
            digitCont[actIndex] = digitCont[actIndex] + 1
        
        j += 1
    i += 1
    a.append(resStr)

print len(a[30])


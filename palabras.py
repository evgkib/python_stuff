__author__ = 'ekibalko'
import os
import re
import sys
def lookupword(word):
    with open('C:\\temp\\palabras', 'r', encoding='UTF8') as myfile:
        lines = myfile.readlines()
        for line in lines:
            if re.search(word,line):
                index = lines.index(line)
                if "•" not in lines[index+1]:
                    return " "
                else:
                    return lines[index+1]





file = open('C:\\temp\\palabras.txt', 'r', encoding='UTF8')
output = open('C:\\temp\\anki5000.txt', 'w', encoding='UTF8')

#print(lookupword("gozar"))

lines = file.readlines()
for line in lines:
    wordlist = line.split()
    word = wordlist[0]+", "+wordlist[1] + ':' + ' '.join(wordlist[2:])
    word.strip()
    #print(word)
    #output.write(word)
    example = lookupword(wordlist[0])
    example.strip()
    #print(example)
    output.write(word+example+"\n")
    #output.write(example)
file.close()
output.close()



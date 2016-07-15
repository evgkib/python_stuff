__author__ = 'ekibalko'
file = open('C:\\temp\\anki5000.txt', 'r', encoding='UTF8')
file1 = open('C:\\temp\\test5000.txt', 'w', encoding='UTF8')
for line in file.readlines():
    if len(line) > 5 :
       line.strip('\n')
       file1.write(line)
file1.close()


fin = open(r'C:\Users\ITAG\Downloads\TranslateWords Challenge\t8.shakespeare.txt')
fout = open(r'C:\Users\ITAG\Downloads\TranslateWords Challenge\french_dictionary.csv')

ft = open(r'C:\Users\ITAG\Downloads\TranslateWords Challenge\find_words.txt')

text1 = ""


data1 = fin.readlines()
data2 = fout.readlines()
data3 = ft.readlines()

text = "".join([i for i in data1])

for i in data3:
    k=text.count(i[:-1:] if "\n" in i else i)
    text1 = text1 + "{0},{1}\n".format(i[:-1:] if "\n" in i else i,k)

l1,l2=[],[]

for i in data2:
    temp = i.split(",")
    l1.append(temp[0])
    if('\n' in temp[1]):
        l2.append(temp[1][:-1:])
    else:
        l2.append(temp[1])


for i,j in zip(l1,l2):
    text = text.replace(i,j)
fin.close()

fin = open('t8.shakespeare.translated.txt','w')
fout = open('frequency.csv','w')
fin.write(text)
fout.write(text1)
fin.close()
fout.close()



# fin = open("sha.txt","r")
# fout = open("dic.csv","r")

# ft = open("words.txt")

# text1 = ""


# data1 = fin.readlines()
# data2 = fout.readlines()
# data3 = ft.readlines()

# text = "".join([i for i in data1])

# for i in data3:
#     k=text.count(i[:-1:] if "\n" in i else i)
#     text1 = text1 + "{0},{1}\n".format(i[:-1:] if "\n" in i else i,k)

# l1,l2=[],[]

# for i in data2:
#     temp = i.split(",")
#     l1.append(temp[0])
#     if('\n' in temp[1]):
#         l2.append(temp[1][:-1:])
#     else:
#         l2.append(temp[1])


# for i,j in zip(l1,l2):
#     text = text.replace(i,j)
# fin.close()

# fin = open("changed.txt","w")
# fout = open("Output.csv","w")
# fin.write(text)
# fout.write(text1)
# fin.close()
# fout.close()
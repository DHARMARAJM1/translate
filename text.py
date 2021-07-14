# from typing import Collection
# from googletrans import Translator, constants
# from pprint import pprint

# translator = Translator()

# translation = translator.translate("Abide", dest="fr")
# print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


# # Python3 program to demonstrate the
# # use of replace() method

# string = "geeks for geeks geeks geeks geeks"

# # Prints the string by replacing all
# # geeks by Geeks
# print(string.replace("geeks", "Geeks"))

# # Prints the string by replacing only
# # 3 occurrence of Geeks
# print(string.replace("geeks", "GeeksforGeeks", 3))


# import re
# from collections import Counter
# words = re.findall(r'\w+', open('C:\Users\ITAG\Downloads\TranslateWords Challenge\ t8.shakespere.txt').read().lower())
# count = Counter(words).most_common(15)
# print(count)


print(open("C:\Users\ITAG\Downloads\TranslateWords Challenge\find_words","r"))

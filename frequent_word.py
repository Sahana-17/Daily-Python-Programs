#Program outputs the most freuquently used word in file and the word with the maximum characters

import collections
print("Input a text in a line : ")
text_list = list(map(str, input().split()))
sc = collections.Counter(text_list)
common_word = sc.most_common()[0][0]
max_char = ""
for s in text_list:
    if len(max_char) < len(s):
        max_char = s
print("Most frequent : ", common_word)
print("Max character word : ", max_char)

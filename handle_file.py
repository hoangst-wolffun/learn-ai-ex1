#read wordsEn.txt and make the dictionary with key is 2 last letter of word in wordsEnd.txt
# and value is array word with 2 first letter = 2 last letter of key

import nltk
import json
from collections import defaultdict

# Download and install necessary resources from nltk
nltk.download('punkt')

# Load the text file containing the words
with open('wordsEn.txt', 'r') as f:
    words = f.read().split()

words = [string for string in words if len(string) > 10]

# Create a word_dict_2last_letter to store the dictionary with key is 2last letter
word_dict_2last_letter = defaultdict(list)

# Create a word_dict_2first_letter to store the dictionary with key is 2first letter
word_dict_2first_letter = defaultdict(list)

word_dict_2first_2last_letter = defaultdict(list)

# Iterate through each word and group them by their last two characters
for word in words:
    last_two = word[-2:]
    first_two = word[:2]
    word_dict_2last_letter[last_two].append(word)
    word_dict_2first_letter[first_two].append(word)
    # if first_two in word_dict_2first_2last_letter
    #     if last_two
    word_dict_2first_2last_letter[first_two].append(last_two)

# Remove any keys with no values
word_dict_2last_letter = {k: v for k, v in word_dict_2last_letter.items() if v}
word_dict_2first_letter = {k: v for k, v in word_dict_2first_letter.items() if v}
word_dict_2first_2last_letter = {k: v for k, v in word_dict_2first_2last_letter.items() if v}
word_dict_2first_2last_letter = {k: list(set(v)) for k, v in word_dict_2first_2last_letter.items()}
# Save file
with open('word_dict_2last_letter.json', 'w') as f:
    json.dump(word_dict_2last_letter, f)

with open('word_dict_2first_letter.json', 'w') as f:
    json.dump(word_dict_2first_letter, f)

with open('word_dict_2first_2last_letter.json', 'w') as f:
    json.dump(word_dict_2first_2last_letter, f)

# print(word_dict_2first_letter["en"])
# print(word_dict_2last_letter["pa"])

print(len(word_dict_2last_letter))
print(len(word_dict_2first_letter))

# input pen => en 2 last. find the word with 2 first letter is en
# input paper => pa is first






# # Create the final dictionary with last two characters as key and list of words as value
# final_dict = {}
# for k, v in word_dict.items():
#     final_dict[k] = [w for w, f in v if f == k]
#
#
# # final_dict là dictionary cần lưu
# with open('final_dict.json', 'w') as f:
#     json.dump(final_dict, f)
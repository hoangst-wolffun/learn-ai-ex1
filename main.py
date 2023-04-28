
# # Prompt the user to enter two words
# word1 = input("Enter the first word: ")
# word2 = input("Enter the second word: ")
#
# # Check if the last two letters of word1 match the first two letters of word2
# if word1[-2:] == word2[:2]:
#     print("True")
# else:
#     print("False")

# Open the text file in read mode
with open('wordsEn.txt', 'r') as file:
    # Read the content of the file
    content = file.read()

# Split the content into an array of strings
array_of_strings = content.split('\n')
print("Len list string", len(array_of_strings))

array_of_strings = [string for string in array_of_strings if len(string) > 2]
print("Len list string after remove stiring less than 3", len(array_of_strings))

words_dict = {word: [next_word for next_word in array_of_strings if word[-2:] == next_word[:2]]
              for word in array_of_strings}

# In ra 5 phần tử đầu tiên của dictionary
for key, value in list(words_dict.items())[:5]:
    print(key, ":", value)
# dic_words = {}
# for key in array_of_strings:
#     for value in array_of_strings:
#         if key != value and key[-2:] == value[:2]:
#             if key in dic_words:
#                 dic_words[key].append(value)
#             else:
#                 dic_words[key] = [value]
#
# print(len(dic_words))

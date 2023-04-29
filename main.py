import json

# # Prompt the user to enter two words
# word1 = input("Enter the first word: ")
# word2 = input("Enter the second word: ")
#
# # Check if the last two letters of word1 match the first two letters of word2
# if word1[-2:] == word2[:2]:
#     print("True")
# else:
#     print("False")


# Loading the dictionary from the json file
with open("word_dict_2first_2last_letter.json", "r") as f:
    word_dict_2first_2last_letter = json.load(f)

# print(len(word_dict_2first_2last_letter))
#
# # Print 5 first item of dictionary
# for key, value in list(word_dict_2first_2last_letter.items())[:5]:
#     print(key, ":", value)
with open("word_dict_2first_letter.json", "r") as f:
    word_dict_2first_letter = json.load(f)

with open("word_dict_2last_letter.json", "r") as f:
    word_dict_2last_letter = json.load(f)

begin = "ac"
if begin in word_dict_2first_letter:
    listWordBegins = word_dict_2first_letter[begin]
    print(listWordBegins)
else:
    print("Dont have chain because begin not exit")
    exit()

end = "my"
if end in word_dict_2last_letter:
    listWordEnd = word_dict_2last_letter[end]
    print(listWordEnd)
else:
    print("Dont have chain because end not exit")
    exit()


def find_word(begin_letter, end_letter, my_dict={}, arr=None, arr2=None):
    if arr is None:
        arr = []
    if arr2 is None:
        arr2 = []
    arr.append(begin_letter)
    print("find_word ", begin, " end = ", end_letter, " arr = ", arr, "arr2 = ", arr2)
    if len(arr2) > 0:
        return arr2
    if begin_letter not in my_dict:
        print("dont have key begin ", begin_letter)
        # arr2.append(arr)
        return arr2
    else:
        # danh sách các từ bắt đầu với begin
        list_word_begin = word_dict_2first_2last_letter[begin]
        if end_letter in list_word_begin:
            # khớp rồi
            arr.append(end_letter)
            arr2.append(arr)
            return arr2
        else:
            new_dict = dict(my_dict)
            del new_dict[begin_letter]
            for new_begin in list_word_begin:
                new_arr = arr.copy()
                find_word(new_begin, end_letter, new_dict, new_arr, arr2)

    # print("find_word with begin is", begin_letter, " end is ", end_letter, " arr is ", arr)
    # arr.append(begin_letter)
    # if begin_letter in word_dict_2first_2last_letter:
    #     list_ends = word_dict_2first_2last_letter[begin_letter]
    #     #print("begin_letter is ", begin_letter, " list end is ", list_ends)
    #     if end_letter in list_ends:
    #         print("find success - ", end_letter, " with list end ", list_ends)
    #         arr.append(end_letter)
    #         arr2.append(arr)
    #         if len(list_old_ends) > 0:
    #             new_begin = list_old_ends[0]
    #             return find_word(new_begin, end_letter, list_old_ends[1:], arr, arr2)
    #         else:
    #             return arr2
    #     else:
    #         for new_end in list_ends:
    #             if new_end not in arr:
    #                 list_old_ends_new = word_dict_2first_2last_letter[new_end]
    #                 return find_word(new_end, end_letter, list_old_ends_new, arr, arr2)
    # else:
    #     print("dont have the key in dic ", begin_letter)
    #     if len(list_old_ends) > 0:
    #         new_begin = list_old_ends[0]
    #         return find_word(new_begin, end_letter, list_old_ends[1:], arr, arr2)
    #     else:
    #         return arr2


list_key_value = find_word(begin, end, word_dict_2first_2last_letter)

if list_key_value is not None:
    print(list_key_value)
    for list_begin in list_key_value:
        for i in range(len(list_begin) - 1):
            arr_word_begin = word_dict_2first_letter[list_begin[i]]
            for word in arr_word_begin:
                if word[-2:] == list_begin[i + 1]:
                    print(word)
else:
    print("dont have chain")


import json

# # Prompt the user to enter two words
word1 = input("Enter the first word: ")
if len(word1) < 3:
    print("Please input more than 2 letter")
    exit()

word2 = input("Enter the second word: ")
if len(word2) < 3:
    print("Please input more than 2 letter")
    exit()

# # Check if the last two letters of word1 match the first two letters of word2
if word1[-2:] == word2[:2]:
    print("Special case. Chain is: ", word1, word2)
    exit()

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

begin = word1[-2:]
if begin in word_dict_2first_letter:
    listWordBegins = word_dict_2first_letter[begin]
    print(listWordBegins)
else:
    print("Dont have chain because begin not exit")
    exit()

end = word2[:2]
if end in word_dict_2last_letter:
    listWordEnd = word_dict_2last_letter[end]
    print(listWordEnd)
else:
    print("Dont have chain because end not exit")
    exit()


# Hàm tìm đường đi ngắn nhất từ start đến end sử dụng BFS - CopyRight from Chat GPT :D 
def bfs_shortest_path(graph, start, end):
    # Khởi tạo hàng đợi và đánh dấu các điểm đã thăm
    queue = [[start]]
    visited = set()

    # Nếu điểm bắt đầu và kết thúc trùng nhau
    if start == end:
        return [start]

    while queue:
        # Lấy đường đi đầu tiên từ hàng đợi
        path = queue.pop(0)
        # Lấy điểm cuối cùng của đường đi đó
        node = path[-1]

        # Nếu điểm đó chưa được thăm
        if node not in visited:
            # Lấy tất cả các điểm kề của điểm đó
            if node in graph:
                neighbours = graph[node]
                # Lặp qua tất cả các điểm kề đó
                for neighbour in neighbours:
                    # Tạo một đường đi mới bằng cách thêm điểm kề vào cuối đường đi cũ
                    new_path = list(path)
                    new_path.append(neighbour)
                    # Nếu điểm kề đó là điểm kết thúc, trả về đường đi mới
                    if neighbour == end:
                        return new_path
                    # Thêm đường đi mới vào hàng đợi
                    queue.append(new_path)

            # Đánh dấu điểm đó là đã thăm
            visited.add(node)

    # Nếu không tìm thấy đường đi từ start đến end, trả về None
    return None


shortest_path = bfs_shortest_path(word_dict_2first_2last_letter, begin, end)

# In ra đường đi tìm được
print("The shortest chain with 2 letter - from begin ", word1, " to ", word2, "is ", shortest_path)

print("The shortest chain is")
print(word1)
for i in range(len(shortest_path) - 1):
    arr_word_begin = word_dict_2first_letter[shortest_path[i]]
    for word in arr_word_begin:
        if word[-2:] == shortest_path[i + 1]:
            print(word)
            break
print(word2)

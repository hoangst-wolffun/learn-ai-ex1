# learn-ai-ex1
Ex8: Let user type 2 words in English as input. Print out the output
which is the shortest chain according to the following rules:
- Each word in the chain has at least 3 letters
- The 2 input words from user will be used as the first and the last words of the chain
- 2 last letters of 1 word will be the same as 2 first letters of the next word in the chain
- All the words are from the file wordsEn.txt
- If there are multiple shortest chains, return any of them is sufficient

## **Problem:**
File wordsEn.txt nhiều từ. Hơn 109 ngàn từ. Nếu xử lý bằng cách load lên rồi for thì cực kỳ tốn perfomance. 

## **Analyze:**
Vì bài toán cần giải quyết là tìm ra chuổi sao cho 2 từ cuối của từ phía trước là 2 từ bắt đầu của từ tiếp theo. 
Ví dụ: User input vào word1 = pen, word2 = paper. Nhiệm vụ của chúng ta chỉ cần tìm chuổi 2 ký tự sao cho link được en và pa là được.
['en', 'sh', 'pa'] với en là 2 từ cuối từ **pen**. Từ tiếp theo sẽ có **en** là 2 từ đầu và **sh** là 2 từ cuối. Từ nữa thì **sh** là đầu, **pa** là cuối. Và từ cuối cùng là **paper**.
**The shortest chain is [pen english sherpa paper]**

## **Solution:**
- Xử lý data 
  - Load file lên và remove các từ dưới 3 kí tự
  - Tạo dictionary với key là 2 kí tự đầu của từ và value là danh sách 2 kí tự cuối của tất cả các từ có 2 kí tự đầu là key. Ví dụ:
    - Có các từ pen, english, end, follow, ... thì với key = en thì value = ['sh', 'nd']
  - Sau khi xử lý xong thì số key chỉ còn khoảng 351. Rất ít so với 109k input đầu vào. 
- Tìm đường đi ngắn nhất. Sau khi thử dùng đệ quy mà ko work, tìm cách handle với Dijkstra nhưng sẽ gặp vấn đề nếu như số lượng node quá lớn. 
Sau một hồi nhờ chatgpt support thì tìm ra solution BFS (Breadth-First Search) để xử lý vì khoảng cách giữa các điểm có liên quan đền = 1.
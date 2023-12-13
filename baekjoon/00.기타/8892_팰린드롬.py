import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
tc = int(input())


def pell(word) :
    left = 0
    right = len(word)-1

    while left < right :
        if word[left] == word[right] :
            left += 1
            right -= 1
        else :
            return
           
    else:
        return word

for _ in range(tc) :
    k = int(input())
    arr = [input().strip() for _ in range(k)] 
    #print(arr)
    break_check = False
    for i in range(k-1) :
        #print(i)
        for j in range(i+1, k) :# i와 (i+1)번부터 차례로 단어를 합침. 
            #print(j) 
            word = arr[i]+arr[j] 
            word2 = arr[j]+arr[i] #반대로도 고려해야 함.
            if pell(word) == word :
                print(word)
                break_check = True
                break
            elif pell(word2) == word2 :
                print(word2)
                break_check = True
                break
        if break_check == True :
            break
    else :    
        print(0)

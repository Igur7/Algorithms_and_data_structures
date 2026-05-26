import time

with open("lotr.txt", encoding='utf-8') as f:

        text = f.readlines()

S = ''.join(text).lower()

def pattern_finder_basic(S,W):
    start_time = time.perf_counter()
    count = 0
    number_of_comparisons = 0
    ans = []

    for m in range(0,len(S)-len(W)+1,1):
          for i in range(len(W)):
            number_of_comparisons += 1
            if S[m+i] != W[i]:
                break
            if i == len(W)-1:
                count += 1
                ans.append(m)

    t_stop = time.perf_counter()
    time_taken = t_stop - start_time    

    return len(ans), number_of_comparisons, time_taken

def hash(word):
    hw = 0
    d = 256
    q = 101
    for i in range(len(word)):  # N - to długość wzorca
        hw = (hw*d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń

    return hw

def metdoa_rabina(S,W):
    start_time = time.perf_counter()
    count = 0
    number_of_comparisons = 0
    ans = []
    colision = 0

    hW = hash(W)

    for m in range(0,len(S) - len(W) +1,1):
        hS = hash(S[m:m+len(W)])
        number_of_comparisons += 1
        if hS == hW:
            if S[m:m+len(W)] == W:
                count += 1
                ans.append(m)
            else:
                colision += 1

    t_stop = time.perf_counter()
    time_taken = t_stop - start_time
    return len(ans), number_of_comparisons, time_taken, colision

def metoda_rabina2(S,W):
    start_time = time.perf_counter()
    count = 0
    number_of_comparisons = 0
    ans = []
    colision = 0

    hW = hash(W)
    d = 256
    q = 101
    hS = hash(S[0:len(W)])
    for m in range(0,len(S) - len(W) +1,1):
        number_of_comparisons += 1
        if hS == hW:
            if S[m:m+len(W)] == W:
                count += 1
                ans.append(m)
            else:
                colision += 1
        if m < len(S) - len(W):
            hS = (hS*d - ord(S[m])*pow(d,len(W),q) + ord(S[m+len(W)])) % q

            if hS < 0:
                hS += q
            
    t_stop = time.perf_counter()
    time_taken = t_stop - start_time
    return len(ans), number_of_comparisons, time_taken, colision

if __name__ == "__main__":
    W = "time."
    count, number_of_comparisons, time_taken = pattern_finder_basic(S, W)
    print(f"{count} ; {number_of_comparisons} ; {time_taken}")
    count, number_of_comparisons, time_taken, colision = metdoa_rabina(S, W)
    print(f"{count} ; {number_of_comparisons} ; {time_taken} ; {colision}")
    count, number_of_comparisons, time_taken, colision = metoda_rabina2(S, W)
    print(f"{count} ; {number_of_comparisons} ; {time_taken} ; {colision}")
#find multipte patterns

import time

with open("lotr.txt", encoding='utf-8') as f:

        text = f.readlines()

S = ''.join(text).lower()

pattern_list = ['gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 'hundred', 'hobbits', 'however', 'popular', 'nothing', 'enjoyed', 'stuffed', 'relaxed', 'himself', 'present', 'deliver', 'welcome', 'baggins', 'further']

def find_multiple_patterns(S, word_list):
    start_time = time.perf_counter()
    count = 0
    number_of_comparisons = 0
    ans = []

    for W in word_list:
        for m in range(0,len(S)-len(W)+1,1):
              for i in range(len(W)):
                number_of_comparisons += 1
                if S[m+i] != W[i]:
                    break
                if i == len(W)-1:
                    count += 1
                    ans.append((W,m))

    t_stop = time.perf_counter()
    time_taken = t_stop - start_time    

    return ans, number_of_comparisons, time_taken
if __name__ == "__main__":
    ans, number_of_comparisons, time_taken = find_multiple_patterns(S, pattern_list)
    print(f"Found {len(ans)} patterns in {time_taken:.4f} seconds with {number_of_comparisons} comparisons.")
    for a in ans:
        print(a)
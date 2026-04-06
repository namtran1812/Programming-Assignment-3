#Your program must:
#1. Read the alphabet values and the two strings.
#2. Compute the maximum value of a common subsequence.
#3. Reconstruct one optimal subsequence.
#4. Output both the value and the subsequence.

#K is the number of characters in the alphabet.
#Each of the next K lines contains a character and its value.
#A is the first string.
#B is the second string.
k = int(input().strip()) #read the no of chars
char_value_map = {}
for _ in range(k):
    char, value = input().strip().split()
    char_value_map[char] = int(value)

strA = input().strip()
strB = input().strip()
lenA = len(strA)
lenB = len(strB)
dp = [[0] * (lenB + 1) for _ in range(lenA + 1)]
#use first i chars of str1 and first j chars of str2
for i in range(1, lenA + 1):
    for j in range(1, lenB + 1):
        #op1 2 skip char from str1 str2
        val_if_skip_strA = dp[i - 1][j]
        val_if_skip_strB = dp[i][j - 1]
        dp[i][j] = max(val_if_skip_strA, val_if_skip_strB) #best of skipping options begin
        #op3 match chars if they are same
        if strA[i - 1] == strB[j - 1]:
            val_if_match = dp[i - 1][j - 1] + char_value_map[strA[i - 1]]
            dp[i][j] = max(dp[i][j], val_if_match)
#reconstruct the subsequence
i = lenA
j = lenB
subsequence_chars = []
while i > 0 and j > 0:
    if strA[i - 1] == strB[j - 1]:
        #chars match used in opt
        if dp[i][j] == dp[i - 1][j - 1] + char_value_map[strA[i - 1]]:
            subsequence_chars.append(strA[i - 1])
            i -= 1
            j -= 1
            continue
    #move toward that preserve the optimal value
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    else:
        j -= 1
subsequence_chars.reverse() #since we built it backwards
opt_subsequence = ''.join(subsequence_chars)
#(a) a single integer: the maximum value of a common subsequence of A and B.
#(b) On the next line, one optimal common subsequence that achieves this value. 
#If multiple optimal subsequences exist, you may output any one of them.
print(dp[lenA][lenB])
print(opt_subsequence)
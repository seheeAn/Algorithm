str1 = "_"+input()
str2 = "_"+input()
dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]
word = [["" for _ in range(len(str2))] for _ in range(len(str1))]

"""
ACAYKP
CAPCAK
    -   C   A   P   C   A   K
-   0   0   0   0   0   0   0  
A   0   0   1   1   1   1   1
C   0   1   1   1   2   2   2
A   0   1   2   2   2   3   3
Y   0   1   2   2   2   3   3
K   0   1   2   2   2   2   4
P   0   1   2   3   3   3   4

dp[3][5]의 값은 ACA와 CAPCA까지 비교했을 때 LCS길이다.
마지막 글자가 같으므로 dp[3][5] = dp[2][4](AC, CAPC까지의 LCS길이) + 1
dp[4][5] (ACAY, CAPCA까지의 LCS길이)
마지막 글자가 다르므로 dp[4][5] = max(dp[3][5](ACA, CAPCA LCS길이), dp[4][4] (ACAY, CAPC LCS길이))
"""

res_length = 0
res_word = ""

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            word[i][j] = word[i-1][j-1] + str1[i]
        else:
            if (dp[i-1][j] > dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
                word[i][j] = word[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
                word[i][j] = word[i][j-1]

print(dp[-1][-1])
print(word[-1][-1])
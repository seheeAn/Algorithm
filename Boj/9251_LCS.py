str1 = "_"+input()
str2 = "_"+input()
N = len(str1)
M = len(str2)
arr = [[0 for _ in range(M)] for _ in range(N)]

for i in range(1, N):
    for j in range(1, M):
        if str1[i] == str2[j]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i][j-1] , arr[i-1][j])

print(arr[N-1][M-1])

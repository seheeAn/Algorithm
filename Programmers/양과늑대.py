# 양방향 간선으로 간주하여 완전 탐색을 진행한다.
# 중복 방문이 가능하다 
# -> visit 배열을 3차원으로 만들어 같은 양, 늑대수로 해당 노드를 방문한 적이 있는 지 체크한다.
# 만약 해당 경로 끝까지 갔는데 늑대가 많아질 경우 root로 되돌아 와야됨 -> dfs로 탐색

def solution(info, edges):
    answer = 0
    tree = [[0 for _ in range(len(info))] for _ in range(len(info))]
    visit = [[[0 for _ in range(len(info)+1)] for _ in range(len(info)+1)] for _ in range(len(info)+1)] # [늑대][양][노드]
    for e in edges:
        tree[e[1]][e[0]] = 1
        tree[e[0]][e[1]] = 1
                
    def dfs(start, sheep, wolf):
        nonlocal answer
        answer = max(answer, sheep)
        
        for i in range(len(tree[start])):
            if tree[start][i] == 1: #경로가 존재

                if info[i] == 0 and visit[wolf][sheep+1][i] == 0: # 다음 노드가 양
                    visit[wolf][sheep+1][i] = 1
                    info[i] = -1
                    dfs(i, sheep+1, wolf)
                    # backtracking
                    info[i] = 0
                    visit[wolf][sheep+1][i] = 0

                elif info[i] == 1 and visit[wolf+1][sheep][i] == 0: # 다음 노드가 늑대
                    if wolf+1 < sheep: # 추가조건 만족하면
                        visit[wolf+1][sheep][i] = 1
                        info[i] = -1
                        dfs(i, sheep, wolf+1)
                        visit[wolf+1][sheep][i] = 0
                        info[i] = 1

                elif info[i] == -1 and visit[wolf][sheep][i] == 0: # 다음 노드가 비었음(이미 들렸던 노드)
                    visit[wolf][sheep][i] = 1
                    dfs(i, sheep, wolf)
                    visit[wolf][sheep][i] = 0
                        
    visit[0][1][0] = 1
    info[0] = -1
    dfs(0,1,0)
            
    return answer
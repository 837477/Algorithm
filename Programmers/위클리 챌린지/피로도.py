answer = 0
def dfs(k, dungeons, cnt):
    global answer
    if k <= 0:
        return
    if cnt > answer:
        answer = cnt
    for i in range(len(dungeons)):
        if not dungeons[i][2] and k >= dungeons[i][0]:
            dungeons[i][2] = True
            dfs(k - dungeons[i][1], dungeons, cnt+1)
            dungeons[i][2] = False

def solution(k, dungeons):
    for i in range(len(dungeons)):
        dungeons[i].append(False)
    dfs(k, dungeons, 0)
    return answer

if __name__ == "__main__":
    print(solution(80, [[80,20],[50,40],[30,10]]))
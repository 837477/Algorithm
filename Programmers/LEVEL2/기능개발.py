from math import ceil

def solution(progresses, speeds):
    processes = [(value, ceil((100 - value) / speeds[idx])) for idx, value in enumerate(progresses)]    
    answer = []
    while processes:
        finish = processes.pop(0)
        cnt = 1
        for process in processes[:]:
            if finish[1] >= process[1]:
                cnt += 1
                processes.remove(process)
            else:
                break
        answer.append(cnt)

    return answer
        


if __name__ == "__main__":
    print(solution([95, 90, 85, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
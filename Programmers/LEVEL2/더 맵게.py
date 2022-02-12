import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        m1 = heapq.heappop(scoville)
        m2 = heapq.heappop(scoville)
        new = m1 + (m2 * 2)
        heapq.heappush(scoville, new)
        answer += 1
    return answer

if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12], 7))
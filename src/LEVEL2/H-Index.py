def solution(citations):
    citations.sort()
    len_citations = len(citations)

    for i in range(len_citations):
        if len_citations - i <= citations[i]:
            break

    if i + 1 == len_citations:
        return 0
    else:
        return len_citations - i
    
if __name__ == "__main__":
    print(solution([0, 0, 0]))

# 3 0 6 1 5
# 0 1 3 5 6
# 1 1 2 3 4 5 5 6 7 8 8 9 10
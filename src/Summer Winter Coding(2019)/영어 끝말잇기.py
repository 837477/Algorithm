def solution(n, words):
    answer = [0, 0]
    overlap = set([words[0]])
    
    last = words[0][-1]
    for idx in range(1, len(words)):
        # 중복 된 단어 검출 or 끝말잇기 불일치
        if (words[idx] in overlap) or last != words[idx][0]:
            answer = [idx % n + 1, idx // n + 1]
            break
        last = words[idx][-1]
        overlap.add(words[idx])
    return answer

if __name__ == "__main__":
    print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
    print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
    print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
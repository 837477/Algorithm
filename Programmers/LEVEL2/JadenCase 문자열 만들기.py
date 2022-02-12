def solution(s):
    return ' '.join([word.upper() if len(word) == 1 else word[0].upper() + word[1:].lower() for word in s.split(' ')])

if __name__ == "__main__":
    print(solution("for the last week"))

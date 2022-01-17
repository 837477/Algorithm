def solution(n):
    for x in range(1, n+1):
        if n % x == 1:
            return x

if __name__ == "__main__":
    print(
        solution(12)
    )

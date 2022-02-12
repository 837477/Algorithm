def solution(n):
    n_bin_cnt = bin(n)[2:].count('1')
    while True:
        n += 1
        if n_bin_cnt == bin(n)[2:].count('1'):
            return n

if __name__ == "__main__":
    print(solution(78))

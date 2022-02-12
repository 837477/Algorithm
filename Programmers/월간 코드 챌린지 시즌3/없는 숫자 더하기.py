def solution(numbers):
    num_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    return sum(num_set - set(numbers))


if __name__ == "__main__":
    print(
        solution([5,8,4,0,6,7,9])
    )

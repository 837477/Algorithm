import numpy as np

def solution(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    return (arr1.dot(arr2)).tolist()

if __name__ == "__main__":
    print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
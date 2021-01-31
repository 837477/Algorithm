def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7]
    right = [3, 6, 9]
    lastL = 10
    lastR = 12
    
    for n in numbers:
        # 입력 숫자가 왼손용이냐?
        if n in left:
            answer += 'L'
            lastL = n
        # 입력 숫자가 오른손용이냐?
        elif n in right:
            answer += 'R'
            lastR = n
        # 입력 숫자가 중앙이냐?
        else:
            n = 11 if n == 0 else n
            
            absL = abs(n - lastL)
            absR = abs(n - lastR)
            
            #  왼손이 더 멀어?
            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer += 'R'
                lastR = n
            # 오른손이 더 멀어?
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer += 'L'
                lastL = n
            # 같아?
            else:
                if hand == 'left':
                    answer += 'L'
                    lastL = n
                else:
                    answer += 'R'
                    lastR = n
    return answer

if __name__ == "__main__":
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "light"))

'''
L R L / L L R L L R R L
L R L L R R L L L R R 
'''
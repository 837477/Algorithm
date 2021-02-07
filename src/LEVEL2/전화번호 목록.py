def solution(phone_book):
    answer = True
    phone_book.sort()
    phone_book_len = len(phone_book)
    for idx, value in enumerate(phone_book):
        value_len = len(value)
        for i in range(idx+1, phone_book_len):
            if value == phone_book[i][:value_len]:
                answer = False
                break
        if not answer:
            break
    return answer

if __name__ == "__main__":
    print(solution(["123", "456", "789"]))
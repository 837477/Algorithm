# Testcase 생성기
import random
import string


class TestCase:
    def __init__(self):
        pass

    def list(self, type_, len_, num):
        """
        리스트 테스트 케이스 생성기

        :param type_: 문자, 정수, 실수 형 가능
        :param len_: 각 원소의 크기
        :param num: 원소 개수
        :return: 랜덤 리스트
        """
        result = None
        if type_ == str:
            result = [self.string(len_) for _ in range(num)]
        elif type_ == int:
            result = [self.int(len_) for _ in range(num)]
        elif type_ == float:
            result = [self.float(len_) for _ in range(num)]
        return result

    def string(self, len_, upper_=False, lower_=False, capital=False):
        """
        랜덤 스트링 생성기

        :param len_: 스트링 길이
        :param upper: 대문자 여부
        :param lower: 소문자 여부
        :param capital: 첫 글짜 대문자 여부
        :return: 랜덤 스트링
        """
        result = ''.join([random.choice(string.ascii_lowercase) for _ in range(len_)])
        if upper_:
            result.upper()
        elif lower_:
            result.lower()
        elif capital:
            result[0] = result[0].upper()
        return result

    def int(self, len_, zero=True):
        """
        랜덤 정수 생성기

        :param len_: 정수 길이
        :param zero: 0 포함
        :return: 랜덤 정수
        """
        if not zero:
            return random.randrange(10 ** (len_ - 1), 10 ** len_ + 1)
        return random.randrange(10 ** (len_ - 1) - 1, 10 ** len_ + 1)

    def float(self, len_):
        """
        랜덤 실수 생성기

        :param len_: 실수 길이
        :return: 랜덤 실수
        """
        return random.uniform(10**(len_-1) - 1, 10**len_ + 1)


if __name__ == "__main__":
    tc = TestCase()
    print(tc.string(10))
    print(tc.int(2))
    print(tc.float(2))
    print(tc.list(str, 5, 10))

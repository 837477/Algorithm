import datetime

def solution(a, b):
    date_list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return date_list[datetime.date(2016, a, b).weekday()]

def solution(id_list, report_list, k):
    report = {id: [set(), set()] for id in id_list}
    for r in report_list:
        temp = r.split(' ')
        report[temp[0]][0].add(temp[1])  # 내가 신고한 사람 셋
        report[temp[1]][1].add(temp[0])  # 나를 신고한 사람 셋

    ban = set()
    for key, value in report.items():
        if len(value[1]) >= k:  # 정지 대상
            ban.add(key)

    result = []
    for key, value in report.items():
        result.append(len(value[0] & ban))

    return result


if __name__ == "__main__":
    print(solution(
        ["con", "ryan"],
        ["ryan con", "ryan con", "ryan con", "ryan con"],
        3,
        #
        # ["muzi", "frodo", "apeach", "neo"],
        # ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        # 2
    ))

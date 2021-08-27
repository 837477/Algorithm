from collections import defaultdict

def solution(table, languages, preference):
    language_dict = defaultdict(dict)
    for job in table:
        job = job.split(' ')
        for idx in range(1, 6):
            language_dict[job[idx]].update({job[0]: 6 - idx})
    
    job = {'SI': 0, 'CONTENTS': 0, 'HARDWARE': 0, 'PORTAL': 0, 'GAME': 0}
    for idx, l_value in enumerate(languages):
        if l_value in language_dict:
            for key, d_value in language_dict[l_value].items():
                job[key] += preference[idx] * d_value

    return sorted(job.items(), key = lambda item: [-item[1], item[0]])[0][0]
    
if __name__ == "__main__":
    print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#",
                    "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                    "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
                    "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                    "GAME C++ C# JAVASCRIPT C JAVA"],
                   ["PYTHON", "C++", "SQL"],
                   [7, 5, 5]))
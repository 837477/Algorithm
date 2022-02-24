n = int(input())
people = list(map(int, input().split()))
people.sort()
accumulate = result = people[0]
for i in range(1, len(people)):
    accumulate += people[i]
    result += accumulate
print(result)
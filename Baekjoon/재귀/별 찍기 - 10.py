def star_box(n):
    if n == 3:
        return ['***', '* *', '***']
    box = star_box(n//3)
    result = []
    for star in box:
        result.append(star * 3)
    for star in box:
        result.append(star + ' ' * (n//3) + star)
    for star in box:
        result.append(star * 3)
    return result
print('\n'.join(star_box(int(input()))))
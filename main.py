a = [7, 16, 43, 27, 49, 97, 81]
for x in a:
    num = 0
    for z in range(1, x + 1):
        if x % z == 0:
            num += 1
    if num == 2:
        print(x, '- простое число')
    else:
        print(x, '- не просто число')

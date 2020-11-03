N, A, B = map(int, input().split())
S = input()
abcs = list(S)

max_pass = A + B
confirm_pass = 0
foreign_rank = 0

for i in abcs:
    if i == 'a' and confirm_pass < max_pass:
        confirm_pass += 1
        print('Yes')
        continue
    if i == 'b':
        foreign_rank += 1
        if confirm_pass < max_pass and foreign_rank <= B:
            confirm_pass += 1
            print('Yes')
            continue
    print('No')

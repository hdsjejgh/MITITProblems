def solve(string):
    for idx in range(1,len(string)):
        if len(string[idx:])%2!=0:
            continue
        if string[idx:int(idx+len(string[idx:])/2)]==string[int(idx+len(string[idx:])/2):]:
            return 'YES'
    return 'NO'
for i in range(int(input())):
    print(solve(input()))
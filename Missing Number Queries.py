N, Q = map(int,input().split())
maxRange = set(range(1,N+1))
arr = list(map(int,input().split()))
for i in range(Q):
	action = list(map(int,input().split()))
	if action[0] == 1:
		arr[action[1]-1]=action[2]
	if action[0] == 2:
		r = arr[action[1]-1:action[2]] #if r is last index then uh oh
		r = set(r)
		mr = maxRange.copy()
		mr = mr ^ r
		print(mr.pop())

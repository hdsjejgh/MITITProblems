def solve(arr):
	arr = list(map(lambda x:x.replace('IT',''), arr))
	arr = list(filter(lambda x:len(x)>0,arr))
	if len(arr) >0:
		return "NO"
	return "YES"

amount = int(input())

for i in range(amount):
	input()
	word = input().upper()
	if word[-1] == "M" or word[0]!="M":
		print("NO")
		continue
	splitted = word.split("M")[1:]
	if '' in splitted or len(splitted)<1:
		print("NO")
		continue
	solved = solve(splitted)
	print(solved)
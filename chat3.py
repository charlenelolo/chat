
lines = []
with open('line2.txt', 'r', encoding = 'utf-8') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')   # 把時間和人名分開, 時間統一只有五個字元
	time = s[0][:5]   #時間前五個字元
	name = s[0][5:]   #人名是第六個字元後
	print(name)
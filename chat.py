
#read_file
#write_file

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())   #strip() 把換行健去掉
	return lines

def convert(lines):
	new = []
	person = None    #避免當對話紀錄由"對話"開始而不是人名開始, None = 無
	for line in lines:
		if line == '玓瑩':
			person = '玓瑩'
			continue
		elif line == '芳瑀':
			person = '芳瑀'
			continue
		if person:        #如果person 有直
			new.append(person + ':' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()


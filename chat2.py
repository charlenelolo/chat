
#read_file
#write_file

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	charlene_sticker_count = 0
	charlene_photo_count = 0
	charlene_word_count = 0
	melo_word_count = 0
	melo_photo_count = 0
	melo_sticker_count = 0
	for line in lines:
		s = line.split(' ')  # 切開空白建
		time = s[0]
		name = s[1]
		if name == '羅祥綾':
			if s[2] == '貼圖':
				charlene_sticker_count += 1
			elif s[2] == '圖片':
				charlene_photo_count += 1
			else:
				for m in s[3:]:
					charlene_word_count += len(m)
		elif name == 'Melo':
			if s[2] == '貼圖':
				melo_sticker_count += 1
			elif s[2] == '圖片':
				melo_photo_count += 1
			else:
				for mm in s[2:]:
					melo_word_count += len(mm)
	
	print('charlene 說了', charlene_word_count, '個字母')
	print('charlene 傳了', charlene_sticker_count, '個貼圖')
	print('charlene 傳了', charlene_photo_count, '個圖片')

	print('melo 說了', melo_word_count, '個字母')
	print('melo 傳了', melo_sticker_count, '個貼圖')
	print('melo 傳了', melo_photo_count, '個圖片')

	return new

def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('line.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)

main()


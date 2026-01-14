def write_file():
	with open('test.txt', 'a+') as f:
		f.write('Writing from Cron\n')
		
if __name__ == '__main__':
	write_file()

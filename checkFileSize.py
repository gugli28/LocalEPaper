import os

def main():

	print check('1.pdf')
def check( file_path):

	byte= os.stat(file_path).st_size
	print " FILE Size = ", byte
	if byte > 26214000: ## (25*1024*1024 = 26214400)
		return 1
	else:
		return 0


if __name__ == "__main__":
	main()
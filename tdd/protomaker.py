file = open("dragon world.txt", 'r')
txtfile = file.read()
file.close()

# loading patterns
for line in txtfile.split("\n"):
	print("PATTERN" in line[:7])

	#WIP.. dont mess with this file yet
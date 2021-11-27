try:
	file1=open('mailbox.txt')
except:
	print("File cannot be opened or doesn't exist")
	exit()

file2=open("output.txt", "w")
lines=file1.readlines()
count=0
my_list=[]
for line in lines:
	count+=1
	if line.startswith("Subject:"):
		if "gradebook" in line:
			print(count)
			my_list.append(count)

for item in my_list:
	file2.write(str(item))
	file2.write("\n")

file2.close()
file1.close()

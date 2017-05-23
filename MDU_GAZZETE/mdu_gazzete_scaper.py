import os
import re

def search_by_rid(registration_no):
	resfile = open("GZTBTECH.TXT")
	for line in resfile:
		if registration_no in line:
			stu_name = re.search('\s[a-zA-Z]\w+(?:\s[a-zA-Z]\w+?)?\s(?:[a-zA-Z]\w+?)?[\s\.\,\;\:]',line)
			fat_name = re.search('\s[a-zA-Z]\w+(?:\s[a-zA-Z]\w+?)?\s(?:[a-zA-Z]\w+?)?[\s\.\,\;\:]',line[::-1])
			rdata = line.split()
			print("Roll_No: ", rdata[0],"Reg_id: ",rdata[1],"Name: ",stu_name.group(),"father: ",fat_name.group()[::-1],"marks: ",rdata[-1])

def driven():
	option = input("Press 1 for searching by registration number\n\nPress 2 for searching by Roll No")
	if option == "1":
		reg_id = input("Enter registration No")
		search_by_rid(reg_id)
	elif option == "2":
		roll_no = input("Enter roll No")
		search_by_rid(roll_no)
	else:
		print("INVALID INPUT, TRY AGAIN")
		driven()

if __name__ == '__main__':
	driven()
	
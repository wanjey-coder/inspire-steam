#Name : Wanjey Gikenye
#Date : 22/02/2026
#program to perform file operations

#To create a new file

new_file = open("student_data.txt","r+")

#write to new file
new_file.write("{Student Name ; Wanjey Gikenye , ID : 234534, Gmail:Wanjeygikenye@gmail.com}")



#read from the file
new_file = open("student_data.txt","r+")
data = new_file.read()

print(data)

new_file.close()


#Delete file
# us os module
import os
os.remove("remove.txt")



#delete folder
os.rmdir("folder")



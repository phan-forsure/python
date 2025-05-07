import os
file = open('/home/phan/Files/aaa', encoding="utf-8") 
read_data = file.read()
# We can check that the file has been automatically closed.
print(f"Read data: {read_data}")
print(f"Words: {len(read_data.split(" "))}",  f"Characters: {len(list(read_data))}")
file.close()

print(os.uname().sysname, os.uname().nodename, os.uname().machine)
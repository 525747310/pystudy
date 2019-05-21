'''text = "this is my test.\nthis is next line."
print(text)

my_file = open("my_file.txt",'a')   #w是写；r是读;a是追加内容
my_file.write(text)
my_file.close()'''

'''file = open('my_file.txt','r')   #把文件传到file
content = file.read()
print(content)

print(type(content))'''

file = open('my_file.txt','r')   #把文件传到file
content = file.readlines()   #作为一个列表
print(content)

print(type(content))
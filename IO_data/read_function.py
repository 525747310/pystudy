text = "this is my test.\nthis is next line."
print(text)

my_file = open("my_file.txt",'a')   #w是写；r是读;a是追加内容
my_file.write(text)
my_file.close()

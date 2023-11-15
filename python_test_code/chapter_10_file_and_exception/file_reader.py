#从pathlib库中导入Path类
#Path对象指向一个文件
from pathlib import Path
path = Path('/Users/ethan/Desktop/newbie_Python/python_test_code/chapter_10_file_and_exception/pi_digits.txt')
contents = path.read_text()
print(contents)


lines = contents.splitlines() #splitlines 函数是将处理中的各行提取出来
pi_string = ''    #文件读取的时候默认是字符串
for line in lines:
    pi_string += line 
    #pi_string = pi_string + line  效率低些

print(pi_string)


pi_string = ''    #文件读取的时候默认是字符串
for line in contents.splitlines():   #少一个临时变量，代码更简洁。
    pi_string += line 
    #pi_string = pi_string + line  效率低些
print(pi_string)


path_new = Path('/Users/ethan/Desktop/newbie_Python/python_test_code/chapter_10_file_and_exception/division_calculator.py')
contents_new = path_new.read_text()
words = contents_new.split()  #生产一个列表，
print(words)
number_words = len(words)
print(number_words)


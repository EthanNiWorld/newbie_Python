from pathlib import Path
path = Path('/Users/ethan/Desktop/newbie_Python/python_test_code/chapter_10_file_and_exception/programming.txt')
contents = path.read_text()
print(contents)

path.write_text("This is comment by Ethan, I love python")    #似乎覆盖了之前源文件文件内容
contents = path.read_text()
print(contents)


a_values = [2, 4, 10]
T_values = [abs(a-2)+abs(a-4)+abs(a-10) for a in a_values]
min_T = min(T_values)
print(min_T)

print(5/0)

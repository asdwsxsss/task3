import os


folder_path = r"C:\Users\User\Desktop\task3"
file_paths = [os.path.join(folder_path, name) for name in os.listdir(folder_path)]

my_files = os.listdir(folder_path)

common_txt_file_list = {}

for file_name in my_files[1:4]:
    with open(f'{folder_path}\\{file_name}', 'r', encoding="utf8") as f:
        file_lines = f.readlines()
        a = list()
        a.append(str(len(file_lines)))
        a.append(str(file_lines))
        common_txt_file_list[file_name] = a
a = sorted(common_txt_file_list, key=common_txt_file_list.get)
print(a)
sorted_dict={}
for w in a:
    sorted_dict[w]=common_txt_file_list.get(w)
print(sorted_dict)

with open('res.txt', 'w', encoding="utf8") as rewrite_file:
    rewrite_file.write(str(sorted_dict))


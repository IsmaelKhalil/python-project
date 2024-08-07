import os

cwd = os.getcwd()

cwd_file_list = os.listdir(cwd)

cwd_file_dict = []

for cwd_file in cwd_file_list:
    cwd_file_path = os.path.join(cwd,cwd_file)

    if os.path.isfile(cwd_file_path):

        cwd_file_information = {
            'path': cwd_file_path,
            'size': os.path.getsize(cwd_file_path)
        }

        cwd_file_dict.append(cwd_file_information)

for cwd_file_el in cwd_file_dict:
    print(cwd_file_el)
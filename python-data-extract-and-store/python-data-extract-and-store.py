import os

def extract_files(cwd = None):

    if cwd is None:
        cwd = os.getcwd()
    
    cwd_file_dict = []
    
    for cwd_root, cwd_dirs, cwd_files in os.walk(cwd):
        for cwd_file in cwd_files:
            cwd_file_path = os.path.join(cwd_root,cwd_file)
        
            cwd_file_information = {
                'path': cwd_file_path,
                'size': os.path.getsize(cwd_file_path)
            }
        
            cwd_file_dict.append(cwd_file_information)
        
    for cwd_file_el in cwd_file_dict:
        print(cwd_file_el)

# extract_files()
extract_files("/home/ec2-user/environment/python-project/python-data-extract-and-store")
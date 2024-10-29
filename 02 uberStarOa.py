from collections import defaultdict
commands = [
    "goto bucketA", "create fileA", "create fileA",
    "goto bucketC", "create fileB", "create fileC",
    "goto bucketA", "create fileB", "create fileC"
]

current_dir=''
folder_file_dict= defaultdict(set)
count=defaultdict(int)

def find_frequency(folder_file_dict):
    for key,value in folder_file_dict.items():
        count[key]=len(value)
        
    frq= [value for value in count.values()]
    maxim =max(frq)
    
    for key,value in count.items():
        if value == maxim:
            return key
        
def create_file_in_current_dir(file_name):
    folder_file_dict[current_dir].add(file_name)

def run_command(command_string):
    cmd,arg = command_string.split(' ')
    if cmd=="goto":
        global current_dir
        current_dir = arg
    elif cmd=="create":
        create_file_in_current_dir(arg)
    else:
        print('Unsupported command ')

def find_folder_max(commands):
    for command_string in commands:
        run_command(command_string)

    print(find_frequency(folder_file_dict)) 

find_folder_max(commands)
from collections import defaultdict

def groupAndSortOwners(files_dict):
    grouped_files = defaultdict(list)
    
    for file_name, owner in files_dict.items():
        grouped_files[owner].append(file_name)
    
    for owner in grouped_files:
        grouped_files[owner].sort()
    
    return dict(grouped_files)

files_dict = {
    'Input.txt': 'Albert', 
    'Code.py': 'Stanley', 
    'Output.txt': 'Albert',
    'btech.txt': 'Albert'
}

result = groupAndSortOwners(files_dict)
print(result)

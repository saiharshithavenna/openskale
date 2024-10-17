def directory_size(filesystem, path):
    #file_system is the structure
    #path is a string which defines the desired dictory path
    #split the path string based on dot(example root.dir1.subdir1)
    parts = path.split('.')
    
    current_directory = filesystem

    #traverse the directory in every path sting
    for part in parts:
        if part in current_directory:
            current_directory = current_directory[part]
        else:
            return f"Directory '{path}' not found"
    
    #calculate total size of files in the current directory
    def calculate_size(directory):
        total_size = 0
        for item, value in directory.items():
            #the value represents the subdiretory which is a dict or not,if it is a dict it is a subdirectory
            #isinsatnce() is used to check the type of an object
            if isinstance(value, dict):  
                total_size += calculate_size(value)
            else:  
                total_size += value
        return total_size
    
    # calculate the total size in the specified directory
    total_size = calculate_size(current_directory)
    return f"Total_size: {total_size}"

#load examples of directories
filesystem = {
    "root": {
        "dir1": {
            "subdir1": {
                "file1.txt": 100,
                "file2.txt": 200,
                "subsubdir1": {
                    "file3.txt": 50,
                    "file4.txt": 150,
                    "subsubsubdir1": {
                        "file5.txt": 500,
                        "emptydir1": {}
                    }
                }
            },
            "subdir2": {
                "file6.txt": 300,
                "subsubdir2": {
                    "file7.txt": 700,
                    "subsubsubdir2": {
                        "file8.txt": 800,
                        "file9.txt": 900
                    }
                },
                "emptydir2": {}
            },
            "file10.txt": 1000
        },
        "dir2": {
            "subdir3": {
                "subsubdir3": {
                    "file11.txt": 400,
                    "file12.txt": 500
                },
                "subsubdir4": {
                    "emptydir3": {}
                }
            },
            "subdir4": {
                "file13.txt": 600,
                "subsubdir5": {
                    "file14.txt": 700,
                    "file15.txt": 800,
                    "subsubsubdir3": {
                        "emptydir4": {},
                        "file16.txt": 900,
                        "file17.txt": 1000
                    }
                }
            },
            "emptydir5": {}
        },
        "dir3": {
            "file18.txt": 1100,
            "subdir5": {
                "subsubdir6": {
                    "file19.txt": 1200,
                    "subsubsubdir4": {
                        "file20.txt": 1300,
                        "emptydir6": {}
                    }
                }
            }
        },
        "emptydir7": {},
        "file21.txt": 1400
    }
}

#output
path = "root.dir1.subdir1.subsubdir1"
result = directory_size(filesystem, path)
print(result)  

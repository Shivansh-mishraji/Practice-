#import os

#check the existence of a file or directory
# if (not os.path.exists("Data")):
#     os.mkdir("Data")

#create multiple directories

# for i in range(0,20):
    # os.mkdir(f"Data/Day{i+1}",f"Data/File {i+1}")

#rename multiple directories

# # for i in range(0,20):
# #     os.rename(f"Data/Day{i+1}",f"Data/File {i+1}")

#list all files and directories in a specific path
"""  
folders =os.listdir("Data")

for folder in folders:
    print(folder)
    """
#remove multiple directories            
# for i in range(0,20):
#     os.rmdir(f"Data/File {i+1}")

#remove multiple files
# for i in range(0,20):         
#     os.remove(f"Data/File {i+1}.txt")

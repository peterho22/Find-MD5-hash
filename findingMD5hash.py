#needs hashlib for hashing and Path from pathlib makes it easier to work with files and folders
import hashlib
from pathlib import Path

#read the target hash
hash_file = Path("message_hash.md5")
target_hash = hash_file.read_text().strip()

#read where the dataset folder is
dataset_path = Path("plain_files")

#function to compute md5 
def md5_file(path):
    #hashlib.md5 creates md5 hash objects, then read_bytes() reads it, and hexdigest returns the hash
    return hashlib.md5(path.read_bytes()).hexdigest()

#finds .txt files in the folder
for file in dataset_path.glob("*.txt"):
    #calculate the md5 files
    digest = md5_file(file)
    #prints the names of each md5 file
    print(f"{digest}  {file.name}")
    #checks the md5 until one matches the target hash
    if digest == target_hash:
        print("\n MATCH FOUND")
        print("File name:", file.name)
        break


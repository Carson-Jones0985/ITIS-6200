import hashlib
import json
import os

hash_table_file = "hashTable.json"

def hash_file(filepath):
    hash_function = hashlib.sha256()

    with open(filepath, "rb") as file:
        data = file.read()

    hash_function.update(data)
    return hash_function.hexdigest()

def traverse_directory(directory):
    hashes = {}

    # for root, _, files in os.walk(directory):
    #     for name in files:
    #         path = os.path.join(root, name)
    #         hashes[path] = hash_file(path)
    
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)

        if os.path.isfile(path):
            hashes[path] = hash_file(path)

    return hashes

def generate_table():
    entered_directory = input("Please enter the directory path that you want to hash: ")
    current_hashes = traverse_directory(entered_directory)

    with open(hash_table_file, "w") as file:
        json.dump(current_hashes, file, indent=4)

    print("Hash table generated")

def validate_hash():
    entered_directory = input("Please enter the directory path that you want to validate: ")

    file = open(hash_table_file, "r")
    hashes_in_file = json.load(file)
    file.close()

    current_hashes = traverse_directory(entered_directory)

    for path in hashes_in_file:
        if path not in current_hashes:
            print(path, "was deleted")
        elif hashes_in_file[path] == current_hashes[path]:
            print(path, "hash is valid")
        else:
            print(path, "hash is invalid")

    for path in current_hashes:
        if path not in hashes_in_file:
            print(path, "is a new file")

def main():
    print("1: Generate a new hash table")
    print("2: Verify current Hashes")

    action = input("Please select one of the above options: ")

    if (action == "1"):
        generate_table()
    elif (action == "2"):
        validate_hash()
    else:
        print("Invalid option, please try again")




if __name__ == "__main__":
    main()
# ------------ write file

# modes:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

with open("./assets/words.txt", "a") as f:
    f.write("New text...")
    f.write("!!!")
    # auto close

# ------------ read file
file1 = open("./assets/words.txt", "rt")

print(f"Content: {file1.read()}")

file1.close()

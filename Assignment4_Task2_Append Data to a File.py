filename = 'output.txt'

# Step 1: Take user input and write to the file (overwrite)
user_input = input("Enter text to write to the file: ")
with open(filename, 'w') as file:
    file.write(user_input + '\n')
print("Data successfully written to output.txt.\n")

# Step 2: Take additional input and append to the same file
additional_input = input("Enter additional text to append: ")
with open(filename, 'a') as file:
    file.write(additional_input + '\n')
print("Data successfully appended.\n")

# Step 3: Read and display the final content of the file
print("Final content of output.txt:")
with open(filename, 'r') as file:
    for line in file:
        print(line.strip())

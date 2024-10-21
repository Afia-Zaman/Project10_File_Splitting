# Create a function to open a file with read access
def get_file_object(file_name):
    file_object = open(file_name, "r")
    return file_object

# Create function to handle writing of a single file
def write_single_file(input_file, all_lines_file):
    file_name = input_file.readline().strip()
    output_file = open(file_name, "w")

    # Determine how many lines will be in the output file
    num_lines = int(input_file.readline().strip())

# read the content of input file and write it to split output file
    for line in range(num_lines):
        content = input_file.readline().strip()
        output_file.write(content + "\n")
        all_lines_file.write(content + "\n")
    output_file.close()

    # Print the name of the file
    print(f"{file_name} written.")


def main():
    # Take in a file name from the user
    input_file_name = input("Enter your file name: ")
    print()
    input_file = get_file_object(input_file_name)

    # open a file to write all the lines of input file
    all_lines_file = open("all_lines.txt", "w")

    # Get the number of files to split from the input file
    num_of_files = int(input_file.readline().strip())

    for files in range(num_of_files):
        write_single_file(input_file, all_lines_file)

    # Print the total number of files written
    print(f"\n{input_file_name} has been split into {num_of_files} files")
    input_file.close()
main()

def split_text_file(input_file, output_file1, output_file2):
    try:
        # Open the input file for reading
        with open(input_file, 'r') as file:
            # Read the content of the file
            content = file.read()

            # Calculate the length of the content
            content_length = len(content)

            # Calculate the midpoint to split the file
            midpoint = content_length // 2

            # Split the content into two parts
            part1 = content[:midpoint]
            part2 = content[midpoint:]

            # Write the two parts to the output files
            with open(output_file1, 'w') as output1:
                output1.write(part1)
            with open(output_file2, 'w') as output2:
                output2.write(part2)

        print(f"Splitting complete. {input_file} has been split into {output_file1} and {output_file2}")
    
    except FileNotFoundError:
        print("File not found. Please check the input file path.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Usage example
input_file = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\meta2.txt'
output_file1 = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\meta21.txt'
output_file2 = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\meta22.txt'
split_text_file(input_file, output_file1, output_file2)

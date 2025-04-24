def modify_file_content(text):
    return text.upper()

def process_file():
    try:
        #Ask the user for the input 
        input_filenaame = input("Enter the input file name: ")
        #Open the input file in read mode
        with open(input_filenaame, 'r') as input_file:
            #Read the content of the file
            content = input_file.read()
            #Modify the content using the modify_file_content function
            modified_content = modify_file_content(content)
            #Ask the user for the output file name
            output_filename = input("Enter the name of file to save the modified content: ")
            #Open the output file in write mode
            with open(output_filename, 'w') as output_file:
                #Write the modified content to the output file
                output_file.write(modified_content)
                print(f"Modified content has been written to {output_filename}")
    except FileNotFoundError:
        print("The specified file was not found. Please check the file name and try again.")
    except PermissionError:
        print("Permission denied. Please check your file permissions.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    process_file()
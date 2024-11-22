def read_and_modify_file(input_filename, output_filename):
    try:
       
        with open(input_filename, 'r') as infile:
            
            content = infile.read()
          
            modified_content = content.upper()
            
         
            with open(output_filename, 'w') as outfile:
                outfile.write(modified_content)
                
        print(f"Successfully modified the file and saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():

    input_filename = input("Please enter the filename to read from: ")
    output_filename = input("Please enter the filename to write to: ")
    
    
    read_and_modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
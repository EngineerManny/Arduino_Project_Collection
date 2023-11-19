#!/usr/bin/env python3
import os
import subprocess

# Function to run a shell command and handle errors
def run_command(command):
    try:
        subprocess.run(f'sudo {command}', shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        exit(1)

# Function to search for a .c file in the specified directory and its subdirectories
def find_c_file(directory, file_name):
    for root, _, files in os.walk(directory):
        for file in files:
            if file == file_name:
                return os.path.join(root, file)
    return None

def main():
    # Prompt the user for the Arduino project .c file name
    c_file_name = input("Enter the Arduino project .c file name: ")

    # Construct the base path to the Arduino_Project_Collection folder (modify as needed)
    base_path = "/home/engineermanny/Arduino_Project_Collection/"  # Replace with your actual path

    # Find the .c file inside the Arduino_Project_Collection folder and its subdirectories
    c_file_path = find_c_file(base_path, c_file_name)

    # Check if a .c file was found
    if not c_file_path:
        print(f"No '{c_file_name}' file found in the Arduino_Project_Collection folder or its subdirectories.")
        exit(1)

    # Extract the name of the .c file without the file extension
    project_name = os.path.splitext(os.path.basename(c_file_path))[0]

    # Change the current working directory to the directory containing the .c file
    os.chdir(os.path.dirname(c_file_path))

    # Compile the .c file to .o (Object File)
    compile_command = f"avr-gcc -Os -DF_CPU=16000000UL -mmcu=atmega2560 -c -o {project_name}.o {project_name}.c"

    # Create an ELF File from the Object File
    create_elf_command = f"avr-gcc -mmcu=atmega2560 {project_name}.o -o {project_name}.elf"

    # Convert the ELF File to a HEX File
    create_hex_command = f"avr-objcopy -O ihex -R .eeprom {project_name}.elf {project_name}.hex"

    # Upload the HEX File to the Arduino (adjust avrdude command as needed)
    upload_command = f"avrdude -V -patmega2560 -cwiring -P/dev/ttyACM0 -b115200 -D -Uflash:w:{project_name}.hex:i"
    
    # Run the commands
    run_command(compile_command)
    run_command(create_elf_command)
    run_command(create_hex_command)
    
    # Prompt the user to enter the sudo password for uploading
    upload_command = f'sudo {upload_command}'
    print("Please enter your sudo password for uploading:")
    run_command(upload_command)

if __name__ == "__main__":
    main()

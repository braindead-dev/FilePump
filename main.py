def increase_exe_size(file_path, increase_by_mb):
    # Convert MB to bytes (1 MB = 1,048,576 bytes)
    increase_by_bytes = int(increase_by_mb * 1048576)

    with open(file_path, 'ab') as exe_file:  # Open file in append-binary mode
        exe_file.write(b'\0' * increase_by_bytes)  # Write zeros

if __name__ == "__main__":
    print("""
  ______ _ _      _____                       
 |  ____(_) |    |  __ \                      
 | |__   _| | ___| |__) |   _ _ __ ___  _ __  
 |  __| | | |/ _ \  ___/ | | | '_ ` _ \| '_ \ 
 | |    | | |  __/ |   | |_| | | | | | | |_) |
 |_|    |_|_|\___|_|    \__,_|_| |_| |_| .__/ 
           by braindead-dev            | |    
            .EXE EDITION               |_|    
          
""")
    
    file_path = input("Enter path to EXE: ")
    increase_by_mb = float(input("How much to increase the size by (in MB)? "))  # Input in MB

    increase_exe_size(file_path, increase_by_mb)
    print(f"File {file_path} has been increased by {increase_by_mb} MB.")
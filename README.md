# FilePump

A lightweight whitehat tool that increases the filesize of `.exe` files by appending zeros.

## Overview

This utility has been crafted to increase the size of `.exe` files based on user input. By appending zeros to the end of the file, it artificially inflates the file size without altering the file's main functionality.

## Usage

1. **Run the Script**: Execute `main.py`.
2. **Enter EXE Path**: Provide the complete path to your `.exe` file.
3. **Specify Size Increase**: Input the number of megabytes you wish to increase the file size by.
4. **Confirmation**: Upon successful completion, a confirmation message will be displayed.

## Functionality

- **Function `increase_exe_size(file_path, increase_by_mb)`**:
  - Takes in the path to the `.exe` file and the number of megabytes by which you wish to increase the file size.
  - Calculates the number of bytes to increase based on the provided megabytes.
  - Opens the `.exe` file in append-binary mode and writes zeros to increase its size.

## Note

This tool is intended for whitehat purposes. Always ensure you have appropriate permissions and are acting ethically when using this or any other tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
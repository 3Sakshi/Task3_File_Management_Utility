# File Management Utility
A Python-based file management utility for creating, searching, copying, moving, and deleting files and folders with validation, error handling, and automated testing.

## Features
- Create files and folders
- List files and folders
- Search files and folders by keyword
- Copy files and folders
- Move files and folders
- Delete files and folders
- View file/folder information
- Input validation
- Error handling
- Automated testing using pytest

## Technologies Used
- Python
- pathlib
- shutil
- pytest

## Project Structure
```text
Task3_File_Management_Utility/
│
├── main.py
├── file_manager.py
├── validators.py
└── test_file_manager.py
```

## How to Run
Clone or download the repository.
Open the project folder in a Python environment.
Run:
```text
python main.py
```

## Menu Options
The utility provides the following operations:
Create Folder
Create File
List Items
Search Items
Copy Item
Move Item
Delete Item
File/Folder Information
Exit

## Testing
Automated tests are written using pytest.
Run:
```text
pytest -q
```
Test result:
```text
8 passed
```

## Error Handling
The application handles common file management errors such as:
- Invalid input
- Empty paths
- Non-existent paths
- Invalid directory operations
- Missing source files or folders

## Learning Outcomes
Through this project, I practiced:
- Python file and folder handling
- pathlib for path management
- shutil for copy, move, and delete operations
- Input validation
- Exception handling
- Modular Python programming
- Automated testing with pytest
- GitHub project documentation

## Author
Sakshi Tayade

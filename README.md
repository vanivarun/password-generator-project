# password-generator-project

A secure password generator with CLI & GUI (Tkinter) in Python

## Features

- Command-Line Interface (CLI) support
- Graphical User Interface (GUI) using Tkinter
- Secure password generation
- Customizable password length
- Save generated passwords to a local database
- Easy to use and portable

## Technologies Used

- Python
- Tkinter (for GUI)
- SQLite (for password storage)
- PyInstaller (for executable build)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/vanivarun/password-generator-project.git
cd password-generator-project
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

### CLI Version:

```bash
python password_generator.py
```

### GUI Version:

```bash
python password_generator_gui.py
```

## Build Executable (Optional)

To create a standalone executable using PyInstaller:

```bash
pyinstaller --onefile password_generator.py
pyinstaller --onefile password_generator_gui.py
```

## License

This project is licensed under the MIT License.


# 🔐 Password Generator Project

A fully functional Python-based password generator with both **CLI** and **GUI (Tkinter)** versions.

![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📸 Preview

![GUI Screenshot](screenshots/gui_preview.png) <!-- Replace this with your actual image path -->

---

## ✨ Features

### 🔧 Common
- Generate **strong, random passwords**
- Customize password **length and character types**
- Uses **clipboard integration** (`pyperclip`)

### 🖥️ GUI Version
- Built with **Tkinter**
- **Password strength meter**
- **Copy to clipboard** with 1-click
- **Password history log**

### 🧪 CLI Version
- Generate secure passwords via terminal
- Simple prompts for length and type

### ⚙️ Packaging
- Can be converted to `.exe` using PyInstaller

---

## 🧰 Setup Instructions

1. Clone the repo or download the ZIP:
   ```bash
   git clone https://github.com/your-username/password-generator-project.git
   cd password-generator-project
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the environment:
   ```bash
   venv\Scripts\activate  # For Windows
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### 🖥️ Run GUI
```bash
python password_generator_gui.py
```

### 🧪 Run CLI
```bash
python password_generator.py
```

---

## 📦 Package as Executable

To create a `.exe` (for Windows):

```bash
pip install pyinstaller
pyinstaller --onefile password_generator_gui.py
```

The `.exe` will be available in the `dist/` folder.

---

## 📂 Project Structure

```
password-generator-project/
├── password_generator.py          # CLI script
├── password_generator_gui.py      # GUI version
├── requirements.txt
├── README.md
├── report.md                      # Project report
├── cli_test_cmd.txt               # Sample CLI run
├── venv/                          # Virtual environment (ignored)
└── dist/, build/                  # .exe build files
```

---

## 🛡 License

This project is licensed under the **MIT License** – feel free to use, modify, and share.

---

## 💼 About This Project

This project demonstrates:
- Python scripting and logic
- GUI development with Tkinter
- Virtual environments and packaging
- Clean code structure and documentation

> 💡 A great beginner-to-intermediate level project to showcase your Python skills!

---

## 📫 Contact

Made by **Varun** – Feel free to connect!

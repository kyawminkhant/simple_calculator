# simple_calculator
A functional desktop calculator built using Python’s Tkinter library.
Designed for everyday use with clean UI, memory functions, and smart operator handling.
------------------------------

## 🧮 Simple Calculator (Tkinter)
A functional desktop calculator built using Python’s Tkinter library. <br>
Designed for everyday use with a **clean UI, keyboard support, memory functions, and smart operator handling**.

------------------------------

## 📌 Overview
This project provides a full-featured calculator interface supporting both basic and extended operations. <br><br>
**Key highlights**: <br>
- Multi-step calculations
- Automatic expression tracking
- Square, square root, percentage, and reciprocal
- Memory system (MS, MR, M+, M–, MC)
- Keyboard input support
- Error-safe evaluation
- Clean and responsive GUI

------------------------------

## ✨ Features
### ➕ Arithmetic Operations
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`×`)
- Division (`÷`)

### 🔢 Advanced Functions
- Square (`x²`)
- Square Root (`√x`)
- Reciprocal (`1/x`)
- Negation (`+/−`)
- Percentage (`%`)

### 🧠 Smart Behaviour
- Typing a number after **=** clears the previous result
- Automatic expression handling
- Zero-division protection
- Input validation

### ⌨️ Keyboard Support
- Number keys (`0–9`)
- Operators (`+ - * / ^ √`)
- `Enter` to evaluate
- `Backspace` to delete

### 🖥 GUI
- Built entirely with Tkinter
- Responsive button layout
- Expression history panel
- Desktop-friendly interface

------------------------------

## ▶️ How to Run
### Requirements
- Python 3.8+
- Tkinter (included with Python)
- No external libraries required
  
### Steps
    git clone https://github.com/your-username/simple_calculator.git <br>
    cd simple_calculator <br>
    python calculator.py <br>
The calculator window will open and be ready to use.

------------------------------

## 🧠 Supported Operations
Button | Function
------ | --------
\+ | Addition
\- | Subtraction
\* | Multiplication
/ | Division
% | Percentage
1/x	| Reciprocal
x²	| Square
√x	| Square Root
+/-	| Negate number
CE	| Clear Entry
AC	| Clear All
MS	| Memory Store
MR	| Memory Recall
M+	| Memory Add
M-	| Memory Subtract
MC	| Memory Clear

------------------------------

## ✔ Example Usage
### Example 1
#### Input
    90 - 60 =

#### Output
    30

#### Example 2
    12 + 7 = → press 5

✔ Previous result clears <br>
✔ Ready for a new calculation

------------------------------

## 📂 Project Structure
    simple_calculator/
    │
    ├── calculator.py   # Main Tkinter calculator program
    └── README.md

------------------------------

## 🚀 Future Improvements
- Scientific mode (sin, cos, tan, log, etc.)
- Scrollable calculation history
- Dark mode / modern UI themes
- Packaging as `.exe` using PyInstaller

------------------------------

## 📜 License
MIT License — free to use, modify, and distribute.

------------------------------

## 👨‍💻 Author
Kyaw Min Khant
A GUI-based extension of a previous equation-solving project, focused on:

Logical expression handling

User-friendly calculator behavior

Desktop GUI development with Tkinter

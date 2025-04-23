# Password Strength Checker

## Project Overview
The **Password Strength Checker** is a tool designed to evaluate the robustness of passwords based on entropy, length, character diversity, and patterns. It also provides feedback to users for improving password security and generates strong, random passwords.

This final project was developed as part of the SAT4650 course (Password Education). It demonstrates the practical application of GUI design, hashing techniques, API integration, and mathematical calculations for secure password management.

---

## Features
- **Password Strength Evaluation:** 
  Calculates password entropy, estimates cracking time, and checks breach status via the *Have I Been Pwned* API.
- **Generated Strong Passwords:** 
  Creates random, secure passwords using diverse characters.
- **Dynamic Feedback:** 
  Offers real-time evaluation of password security as users type.
- **User-Friendly GUI:** 
  Built with `ttkbootstrap` for a modern and intuitive interface.
- **Logging:** 
  Logs events in `password_checker.log` for future reference.

---

## Prerequisites
- **Python 3.8 or higher**
- Required libraries:
  - `ttkbootstrap`
  - `hashlib`
  - `re`
  - `requests`
  - `math`
  - `logging`
  - `random`
  - `string`

Install the required libraries using:
```bash
pip install ttkbootstrap hashlib re requests math logging random string
```
---

## Usage
1. Clone the repository:
```bash
git clone https://github.com/<YourUsername>/<YourRepositoryName>
```

2. Run the program:
```bash
python password_checker.py
```

- Enter a password to evaluate its strength, or generate a strong password with the GUI.


## File Structure
- password_checker.py: Main program file.
- password_checker.log: Log file for tracking events.
- README.md: Project documentation (this file).


## Author
Cole Clifford
Student of SAT4650 (Password Education) - Final Project, 2025

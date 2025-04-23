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
  - `requests`
  - `math`
  - `logging`
  - `random`
  - `string`

Install the required libraries using:
```bash
pip install ttkbootstrap requests
```
## Usage
- Clone the repository:git clone https://github.com/<YourUsername>/<YourRepositoryName>

- Run the program:python password_checker.py

- Enter a password to evaluate its strength, or generate a strong password with the GUI.


## File Structure
- password_checker.py: Main program file.
- password_checker.log: Log file for tracking events.
- README.md: Project documentation (this file).


## Author
Cole Clifford
Student of SAT4650 (Password Education) - Final Project, 2025

## License
This project is licensed under the MIT License.

Feel free to customize this README with additional information if needed!

Let me know if you encounter any issues while adding this to your repository!

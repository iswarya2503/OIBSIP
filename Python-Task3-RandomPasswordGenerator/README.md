# Python Task 3 - Random Password Generator

## Description
This project is a Random Password Generator developed using Python. It allows users to generate secure and random passwords based on their preferences. The program lets users choose the password length and the types of characters to include, ensuring flexibility and better password security.

## Features
- User-defined password length (minimum 8 characters)
- Option to include:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special symbols
- Input validation for invalid password lengths
- Ensures at least two character types are selected
- Generates a random password
- Option to generate multiple passwords without restarting the program

## Technologies Used
- Python
- random module
- string module

## Project Structure
```text
Python-Task3-RandomPasswordGenerator/
│── password_generator.py
│── README.md
│── requirements.txt
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/iswarya2503/OIBSIP.git
   ```

2. Navigate to the project folder:
   ```bash
   cd OIBSIP/Python-Task3-RandomPasswordGenerator
   ```

3. Run the program:
   ```bash
   python password_generator.py
   ```

## Sample Output

```text
====================================
      RANDOM PASSWORD GENERATOR
====================================

Enter password length (minimum 8): 12

Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

Generated Password:
A@9mK#2xLpQ!

Do you want to generate another password? (y/n): n
```

## Internship
This project was completed as part of the **Python Programming Internship** at **Oasis Infobyte (OIBSIP)**.

## Author
**Iswarya A**

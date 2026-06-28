# 🔐 Advanced Password Strength Checker

A Python-based Password Strength Checker that evaluates password security using multiple validation rules. The application analyzes password complexity, assigns a security score, classifies the password strength, and provides suggestions for creating stronger passwords.

---

## 📌 Project Overview

This project is developed as part of the **DecodeLabs Cyber Security Internship - Project 1**.

The program checks whether a password is **Weak**, **Medium**, or **Strong** by evaluating several security parameters commonly used in cybersecurity.

---

## 🚀 Features

- ✅ Checks minimum password length
- ✅ Recommends 12+ character passwords
- ✅ Detects uppercase letters
- ✅ Detects lowercase letters
- ✅ Detects numeric digits
- ✅ Detects special characters
- ✅ Detects common weak passwords
- ✅ Generates a password score out of 100
- ✅ Displays password strength
- ✅ Provides suggestions to improve password security

---

## 🛠 Technologies Used

- Python 3.x
- Built-in Python Functions
  - any()
  - isupper()
  - islower()
  - isdigit()
  - isalnum()

---

## 📂 Project Structure

```
Advanced-Password-Strength-Checker/
│── password_checker.py
│── README.md
```

---

## ▶️ How to Run

1. Install Python 3.
2. Download or clone this repository.

```bash
git clone https://github.com/yourusername/Advanced-Password-Strength-Checker.git
```

3. Navigate to the project folder.

```bash
cd Advanced-Password-Strength-Checker
```

4. Run the program.

```bash
python password_checker.py
```

---

## 💻 Sample Output

```
Enter Password: Hello@123

========== PASSWORD ANALYSIS ==========
Password Length : 9
Uppercase       : Yes
Lowercase       : Yes
Numbers         : Yes
Special Symbols : Yes
Score           : 80/100
Strength        : Strong 💪

Suggestions to Improve:
- Use 12 or more characters for better security.
```

---

## 📊 Password Evaluation Criteria

| Feature | Score |
|---------|------:|
| Minimum 8 Characters | 20 |
| 12+ Characters | 20 |
| Uppercase Letter | 15 |
| Lowercase Letter | 15 |
| Number | 15 |
| Special Character | 15 |

---

## 🎯 Learning Outcomes

- Python String Handling
- Conditional Statements
- Password Validation
- Basic Cybersecurity Concepts
- Secure Password Practices
- Logic Building

---

## 🔮 Future Enhancements

- GUI using Tkinter
- Password entropy calculation
- Breached password detection
- Password generator
- Real-time password validation
- Password history check

---

## 👩‍💻 Author

**Shalini D**

Cyber Security Intern

DecodeLabs Industrial Training Program
---

## 📜 License

This project is developed for educational and internship purposes.

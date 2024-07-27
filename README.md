# Password-Complexity-Checker

Overview:-
This repository contains a Python script for evaluating the strength of passwords based on various criteria. The script checks the length of the password, and whether it includes uppercase letters, lowercase letters, numbers, and special characters. Based on these checks, it categorizes the password strength as "Weak", "Medium", or "Strong", and provides feedback on how to improve the password.


Features:-
- Length Check: Ensures the password is at least 8 characters long.

- Uppercase Letter Check: Verifies the presence of at least one uppercase letter.

- Lowercase Letter Check: Verifies the presence of at least one lowercase letter.

- Number Check: Verifies the presence of at least one numeric digit.

- Special Character Check: Verifies the presence of at least one special character from the set [!@#$%^&*()_+=-{};:'<>?,./].



Usage:-
To use the script, simply run it and input a password when prompted. The script will analyze the password and provide a strength rating along with feedback for improvement.


Example:- 
          
          Enter a password: MySecurePass123!
          Password strength: Strong


Feedback Example:- 

          Enter a password: weakpass
          Password strength: Weak
          Password is too short. It should be at least 8 characters long. Password should contain at least one uppercase letter. Password should contain at least one special character.


Installation:-

Clone the repository :-




Navigate to the project directory :-
                                    
    cd password-strength-checker

Run the script :-

    python password_strength_checker.py



Contributing :- Contributions are welcome! Please fork the repository and submit a pull request with your changes.


License :- This project is licensed under the MIT License.















#!/usr/bin/python3

import autopep8

def fix_code(code):
    # Use autopep8 to fix code
    fixed_code = autopep8.fix_code(code)
    return fixed_code

def main():
    user_code = input("Enter your Python code:\n")

    try:
        fixed_code = fix_code(user_code)
        print("Fixed code:\n", fixed_code)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


import subprocess
import autopep8

def fix_code(code):
    #subrocess pulls autopep8
    process = subprocess.Popen(['autopep8', '--stdout', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=code)
    return stdout

def main():
    user_code = input("Enter your Python code:\n")

    try:
        fixed_code = fix_code(user_code)
        print("Fixed code:\n", fixed_code)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

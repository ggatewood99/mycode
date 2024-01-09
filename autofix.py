import autopep8
import ast
import astunparse

def fix_code(code):
    # Use autopep8 to fix formatting issues
    fixed_code = autopep8.fix_code(code)

    # Use AST to find and fix logical errors
    try:
        tree = ast.parse(fixed_code)
        for node in ast.walk(tree):
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
                # Suggest fixing addition to subtraction
                node.op = ast.Sub()
    except Exception as e:
        print(f"An error occurred while analyzing the code: {e}")
    
    # Unparse the AST to get the final fixed code
    final_fixed_code = astunparse.unparse(tree)
    return final_fixed_code

if __name__ == "__main__":
    user_code = input("Enter your Python code:\n")
    
    try:
        fixed_code = fix_code(user_code)
        print("Fixed code:\n", fixed_code)
    except Exception as e:
        print(f"An error occurred: {e}")


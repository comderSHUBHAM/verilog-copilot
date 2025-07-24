import sys
import os
from parser import extract_verilog_blocks, detect_simple_errors
from llm import generate_comment

def main():
    if len(sys.argv) != 2:
        print("Usage: python cli_app.py <verilog_file.v>")
        sys.exit(1)

    verilog_path = sys.argv[1]

    if not os.path.isfile(verilog_path):
        print(f"Error: File '{verilog_path}' not found.")
        sys.exit(1)

    with open(verilog_path, 'r') as file:
        verilog_code = file.read()

    errors, corrections = detect_simple_errors(verilog_code)
    blocks, block_lines = extract_verilog_blocks(verilog_code, with_lines=True)
    block_comment_map = {ln: generate_comment(block) for block, ln in zip(blocks, block_lines)}

    lines = verilog_code.splitlines()

    # 1. Print original code
    print("\n📜 ORIGINAL VERILOG CODE (Copy and use):\n")
    for line in lines:
        print(line)

    # 2. Print errors
    if errors:
        print("\n❌ ERRORS FOUND (Details below):\n")
        for lineno, errmsg in errors.items():
            print(f"Line {lineno}:")
            print(f"    {lines[lineno-1]}")
            print(f"    Explanation: {errmsg}")
            if lineno in corrections:
                RED_BOLD = "\033[1;31m"
                RESET = "\033[0m"
                print(f"    {RED_BOLD}{corrections[lineno]}{RESET}")
            print()
    else:
        print("\n✅ No simple syntax errors detected.")

    # 3. Print corrected code
    print("\n🟢 CORRECTED VERILOG CODE (Synthesizable):\n")
    for idx, line in enumerate(lines, 1):
        if idx not in corrections:
            print(line)

if __name__ == "__main__":
    main()

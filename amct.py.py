#!/usr/bin/env python3
# FIRST LINE CLEARS THE SCREEN (CROSS-PLATFORM)
import os; os.system('cls' if os.name == 'nt' else 'clear')

import sys
import time
import signal
import ast
from colorama import init, Fore, Style

# INIT COLORAMA
init(autoreset=True)

# COLORS SETUP
Y = Fore.YELLOW + Style.BRIGHT
C = Fore.CYAN + Style.BRIGHT
G = Fore.GREEN + Style.BRIGHT
R = Fore.RED + Style.BRIGHT
W = Fore.WHITE + Style.BRIGHT

# ASCII LOGO
LOGO = f"""
{Y}
     █████╗ ███╗   ███╗ ██████╗████████╗
    ██╔══██╗████╗ ████║██╔════╝╚══██╔══╝
    ███████║██╔████╔██║██║        ██║   
    ██╔══██║██║╚██╔╝██║██║        ██║   
    ██║  ██║██║ ╚═╝ ██║╚██████╗   ██║   
    ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝   ╚═╝   
{Style.RESET_ALL}
{C}DEVELOPER: CYPER ABOD
{C}TOOL: AVERAGE MARKS COUNTING TOOL (AMCT)
 VERSION: 1.0
"""

# FAKE LOADING (3 SECONDS)
def fake_loading():
    print(Y + "INITIALIZING TOOL, PLEASE WAIT...\n")
    for _ in range(30):  # 30 * 0.1s = 3s
        sys.stdout.write(Y + "█")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n" + C + "DONE!\n")

# SAFE EVALUATOR FOR CALCULATOR USING ast
def safe_eval(expr: str):
    try:
        tree = ast.parse(expr, mode='eval')
    except Exception as e:
        raise ValueError("INVALID EXPRESSION SYNTAX") from e

    for node in ast.walk(tree):
        if not isinstance(node, (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
                                 ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow,
                                 ast.USub, ast.UAdd, ast.FloorDiv, ast.Load,
                                 ast.Tuple, ast.List, ast.Subscript, ast.Index)):
            raise ValueError("UNALLOWED EXPRESSION ELEMENTS")
        if isinstance(node, ast.Call) or isinstance(node, ast.Name) or isinstance(node, ast.Attribute):
            raise ValueError("FUNCTIONS OR VARIABLES ARE NOT ALLOWED")

    try:
        compiled = compile(tree, filename="<ast>", mode="eval")
        return eval(compiled, {"__builtins__": None}, {})
    except Exception as e:
        raise ValueError("ERROR DURING EVALUATION") from e

# AVERAGE CALCULATORS
def compute_average(subjects_count):
    scores = []
    for i in range(1, subjects_count + 1):
        while True:
            try:
                s = input(Y + f"ENTER MARK FOR SUBJECT {i} (0-100): " + W).strip()
                if s == "":
                    print(R + "INPUT CANNOT BE EMPTY. PLEASE ENTER A NUMBER BETWEEN 0 AND 100.")
                    continue
                val = float(s)
                if val < 0 or val > 100:
                    print(R + "VALUE MUST BE BETWEEN 0 AND 100.")
                    continue
            except ValueError:
                print(R + "PLEASE ENTER A VALID NUMBER (E.G. 75 OR 87.5).")
                continue
            scores.append(val)
            break
    total = sum(scores)
    average = total / subjects_count
    print("\n" + G + "RESULTS:")
    print(Y + f"TOTAL (SUM OF {subjects_count} SUBJECTS): {W}{total:.2f}")
    print(Y + f"AVERAGE (OUT OF 100): {W}{average:.2f}\n")
    print(Y + "PRESS 0 TO RETURN TO TOOL")
    choice = input("> ").strip()
    if choice == "0":
        return
    else:
        print(C + "RETURNING TO MAIN MENU...\n")
        time.sleep(0.6)
        return

def compute_iraqi_average_7():
    compute_average(7)

def compute_iraqi_average_13():
    compute_average(13)

# SIMPLE CALCULATOR
def calculator_ui():
    print(Y + "SIMPLE CALCULATOR - ENTER AN ARITHMETIC EXPRESSION (EX: 2+3*4/5) OR 'Q' TO QUIT")
    while True:
        expr = input(Y + "EXPR> " + W).strip()
        if expr.lower() in ("q", "quit", "exit"):
            print(C + "EXITING CALCULATOR...\n")
            time.sleep(0.4)
            return
        if expr == "":
            continue
        try:
            result = safe_eval(expr)
        except ValueError as e:
            print(R + "ERROR: " + str(e))
            continue
        except Exception:
            print(R + "UNABLE TO EVALUATE EXPRESSION.")
            continue
        print(G + "RESULT: " + W + str(result))

# MAIN MENU
def main_menu():
    while True:
        print(LOGO)
        print(Y + "SELECT AN OPTION:")
        print(Y + "1) CALCULATE THE AVERAGE SCORE (7 SUBJECTS)")
        print(Y + "2) CALCULATE THE AVERAGE SCORE (13 SUBJECTS)")
        print(Y + "3) SIMPLE CALCULATOR")
        print(Y + "4) EXIT")
        choice = input(Y + "CHOICE> " + W).strip()
        if choice == "1":
            compute_iraqi_average_7()
        elif choice == "2":
            compute_iraqi_average_13()
        elif choice == "3":
            calculator_ui()
        elif choice == "4":
            print(C + "\nTHANK YOU FOR USING AMCT! GOODBYE.")
            break
        else:
            print(R + "INVALID CHOICE. PLEASE SELECT 1, 2, 3 OR 4.")
        time.sleep(0.2)
        os.system('cls' if os.name == 'nt' else 'clear')

# CTRL+C HANDLER
def _handle_sigint(signum, frame):
    print("\n\n" + Y + "EXITING... THANK YOU FOR USING AMCT! GOODBYE.")
    raise SystemExit(0)

# RUN
if __name__ == "__main__":
    signal.signal(signal.SIGINT, _handle_sigint)
    try:
        fake_loading()
        main_menu()
    except KeyboardInterrupt:
        print("\n\n" + Y + "EXITING (KEYBOARD INTERRUPT)... THANK YOU FOR USING AMCT! GOODBYE.")
        raise SystemExit(0)

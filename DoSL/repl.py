from .transformer import executor
from .parser import parser
from lark.exceptions import UnexpectedToken, UnexpectedCharacters, VisitError
from .colour import red

def run_file(filename):
    with open(filename, encoding="utf-8") as f:
        code = f.read()
    try:
        tree = parser.parse(code)
        executor.transform(tree)
    except UnexpectedToken as e:
        print(red(f"Syntax error: unexpected token '{e.token}' at line {e.line}, column {e.column}"))
        print(e)
    except UnexpectedCharacters as e:
        print(red(f"Syntax error: unexpected character '{e.char}' at line {e.line}, column {e.column}"))
        print(e)
    except VisitError as e:
        print(red(f"Runtime error in transformer: {e.orig_exc}"))
        print(e)
    except Exception as e:
        print(red(f"Error processing file {filename}: {e}"))
        print(e)

def start_repl():
    print("DoSL Interactive REPL. Type 'exit;' to quit.")
    buffer = ""
    brace_count = 0 
    prompt = "DoSL> "
    while True:
        line = input(prompt)
        if line.strip().lower() == "exit;":
            break
        
        buffer += line + "\n"
        brace_count += line.count("{") - line.count("}")

        if brace_count == 0 and ";" in buffer:
            prompt = "DoSL> "
            try:
                tree = parser.parse(buffer)
                executor.transform(tree)
            except UnexpectedToken as e:
                print(red(f"Syntax error: unexpected token '{e.token}' at line {e.line}, column {e.column}"))
                print(e)
            except UnexpectedCharacters as e:
                print(red(f"Syntax error: unexpected character '{e.char}' at line {e.line}, column {e.column}"))
                print(e)
            except VisitError as e:
                print(red(f"Runtime error in transformer: {e.orig_exc}"))
                print(e)
            except Exception as e:
                print(red(f"Error processing commands: {e}"))
                print(e)
            buffer = ""
        else:
            prompt = "..... "

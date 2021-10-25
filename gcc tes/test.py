def ExecuteCtags(func):
    import subprocess
    def wrapper(*args, **kwargs):
        out = subprocess.run(["./ctags --language-force=C --kinds-C=* --fields=* *.c"], shell=True, capture_output=True)
        func(*args, **kwargs)
    return wrapper

@ExecuteCtags
def FindUndefinedVariables(filename="tags"):
    # read ctags
    with open(filename, "r", encoding="ascii") as f:
        lines = f.read().split("\n")

    variables_externed = {}
    variables_defined = {}

    # read each lines
    for line in lines:
        # skip vacant line, or comments line
        if not line or line.startswith("!"):
            continue
        symbol = line.split("\t")[0]
        # find defined global variable
        if "\tkind:vairable" in line:
            variables_defined[symbol] = None
        elif "\tkind:externvar" in line:
            variables_externed[symbol] = None

    # find error
    Undefined_variables = []
    for variable in variables_externed:
        if variable not in variables_defined:
            print("Undefined variable:", variable)
            Undefined_variables.append(variable)
    return Undefined_variables

if __name__ == "__main__":
    FindUndefinedVariables()
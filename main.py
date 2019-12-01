from symbol_table import SymbolTable
from lexer import Lexer
from parser import Parser
import re
import sys


def main():
    try:
        if len(sys.argv) == 2:
            filename = sys.argv[1]

            with open(filename, 'r') as f:
                file = f.read()
                run(file)

        else:
            with open("./test_file.1k", 'r') as f:
                file = f.read()
                run(file)

    except Exception as error:
        print(error)
        sys.exit(1)


def run(file):
    # Pre Processing + \n para determinar EOF
    code = re.sub("[/]{2,}.*", "", file) + "\n"
    defines = [x.split() for x in re.findall("#define.*", code)]
    filtered = re.sub("(#define.*)\n", " ", code)
    for define in defines:
        name = define[1:2][0]
        list_value = define[2:]
        value = ""
        for i in list_value:
            value += i
        filtered = re.sub(f"({name})", f"{value}", filtered)

    # Lexer
    lexer = Lexer().createLexer()
    tokens = lexer.lex(filtered)

    # Symbol Table
    st = SymbolTable(None)

    # Parser
    parser = Parser()
    parser.parse()
    parser.get_parser().parse(tokens).eval(st)


if __name__ == "__main__":
    main()

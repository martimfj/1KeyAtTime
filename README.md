# 1 Key At Time

## Introdução
Este projeto tem como objetivo implementar uma linguagem de programação para deficientes físicos, que têm o movimento dos dedos da mão restrito. A proposta dessa linguagem de programação é possibilitar que o usuário programe sem ter que pressionar mais de uma tecla por vez. Portanto, a linguagem não contém nenhum caracter especial que necessite pressionar `Shift`. 

**Obs1:** Os caracteres `/` `*` `-` `+` são presentes no *Numeric keypad* sem a necessidade de pressionar `Shift`, porém como não são todos os teclados que o tem, as opereções correspondentes foram implementadas de outra maneira. Além de ser distânte do restante do teclado, o que implicaria na queda do *Keystrokes per minute*.

**Obs2:** O caracter `=` e `-` são presentes em todos os teclados sem a necessidade de pressionar `Shift`, porém o `-` foi implementado de maneira difente por questões de padronização. 

## Recursos
- Variáveis
- Blocos condicionais
- Blocos de repetição (loop)
- Impressão no terminal
- Funções (permite recursão)
- Tipo de variável aceito: Inteiros (True: 1; False: 0)
- Operações: +, -, *, /, e, ou, ==, <, >, inv

## Exemplo
```
def fibonacci[n]/
    if[[n lower 1] or [n equal 1]]/
        fibonacci == n
    \
    else/
        fibonacci = fibonacci[n minus 1] plus fibonacci[n minus 2]
    \
\

print[fibonnaci[10]]
```

## EBNF
```
program: { statement };

statement: (assignment | print | if_else | while | func_def) "\n";

func_def: "def", identifier, "[", def_args, "]", "/" { statament }, "\";

def_args: identifier, { ",", identifier };

func_call: indentifier, "[", call_args, "]";

call_args: rel_exp, {"," rel_exp};

assignment: indentifier, "=", expression;

print: "print", "[", rel_exp, "]";

if_else: "if", "[", rel_exp, "]", "/", {statement}, "\", ["else", "/", {statement}, "\"];

while: "while", "[", rel_exp, "]", "/", {statement}, "\";

rel_exp: expression, ("==" | "bigger than" | "less than"), expression;

expression: term, { ("plus" | "minus" | "or"), term };

term: factor, { ("times" | "divide" | "and"), factor };

factor: number | indentifier | ("plus" | "minus" | "not"), factor | "[" expression "]" | func_call;

indentifier = letter, { letter | digit };

letter = "A" | "B" | "C" | "D" | "E" | "F" | "G"
       | "H" | "I" | "J" | "K" | "L" | "M" | "N"
       | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
       | "V" | "W" | "X" | "Y" | "Z" ;

number: digit, { digit };

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

```
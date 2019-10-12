# 1 Key At Time

## Introdução
Este projeto tem como objetivo implementar uma linguagem de programação para deficientes físicos, que têm o movimento dos dedos da mão restrito. A proposta dessa linguagem de programação é possibilitar que o usuário programe sem ter que pressionar mais de uma tecla por vez. Portanto, a linguagem não contém nenhum caracter especial que necessite pressionar `Shift`. 

**Obs1:** Os caracteres `/` `*` `-` `+` são presentes no *Numeric keypad* sem a necessidade de pressionar `Shift`, porém como não são todos os teclados que o tem, as opereções correspondentes foram implementadas de outra maneira. Além de ser distânte do restante do teclado, o que implicaria na queda do *Keystrokes per minute*.

**Obs2:** Os caracteres `=` e `-` são presentes em todos os teclados sem a necessidade de pressionar `Shift`, porém o `-` foi implementado de maneira difente por questões de padronização. 

A linguagem foi inspirada em python, com a adição de / \ para delimitar os blocos de comando de funções, if, else e while.

## Recursos
- x = 10
- if[x == 10]/  \
- else/  \
- while[x < 100]/  \
- print[x]
- def function(arg1, arg2) /  \
- plus, minus, times, divide, and, or, ==, greater, less, not

## Exemplo
```
def mult3[n]/
    if[n == 1]/
        mult3 = 3
    \
    else/
        mult3 = mult3[n minus 1] plus 3
    \
\

x = 1
while[x less 10]/
    print[mult3[x]]
    x = x plus 1
\
```

## EBNF

`program: { statement };`

`statement: (assignment | print | if_else | while | func_def) "\n";`

- `assignment: indentifier, "=", expression;`

- `print: "print", "[", rel_exp, "]";`

- `if_else: "if", "[", rel_exp, "]", "/", {statement}, "\", ["else", "/", {statement}, "\"];`

- `while: "while", "[", rel_exp, "]", "/", {statement}, "\";`

- `func_def: "def", identifier, "[", def_args, "]", "/" { statament }, "\";`

  - `def_args: identifier, { ",", identifier };`

`rel_exp: expression, ("==" | "bigger than" | "less than"), expression;`

`expression: term, { ("plus" | "minus" | "or"), term };`

`term: factor, { ("times" | "divide" | "and"), factor };`

`factor: number | indentifier | ("plus" | "minus" | "not"), factor | "[" expression "]" | func_call;`
- `number: digit, { digit };`
- `indentifier = letter, { letter | digit };`
- `func_call: indentifier, "[", call_args, "]";`
  - `call_args: rel_exp, {"," rel_exp};`

`letter = "A" | "B" | "C" | "D" | "E" | "F" | "G"| "H" | "I" | "J" | "K" | "L" | "M" | "N"| "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" ;`

`digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;`
"""
Based on the example page: https://rply.readthedocs.io/en/latest/users-guide/lexers.html
"""

from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def addTokens(self):
        self.lexer.add('NUMBER', r'\d+')
        self.lexer.add('PLUS', r'plus')
        self.lexer.add('MINUS', r'minus')
        self.lexer.add('MUL', r'times')
        self.lexer.add('DIV', r'divide')

        self.lexer.add('GREATER', r'greater')
        self.lexer.add('LESS', r'less')
        self.lexer.add('EQUAL', r'==')
        self.lexer.add('ASSINGMENT', r'=')
        self.lexer.add('COMMA', r',')

        self.lexer.add('OPEN_PAREN', r'\[')
        self.lexer.add('CLOSE_PAREN', r'\]')
        self.lexer.add('OPEN_BRACKET', r'\/')
        self.lexer.add('CLOSE_BRACKET', r'\\')

        self.lexer.add('PRINT', r'print(?!\w)')
        self.lexer.add('IF', r'if(?!\w)')
        self.lexer.add('ELSE', r'else(?!\w)')
        self.lexer.add('WHILE', r'while(?!\w)')
        self.lexer.add('FUNC', r'def(?!\w)')
        self.lexer.add('AND', r'and(?!\w)')
        self.lexer.add('OR', r'or(?!\w)')
        self.lexer.add('NOT', r'not(?!\w)')
        self.lexer.add('NEWLINE', r'[\r\n]+')

        self.lexer.add('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*')
        self.lexer.ignore('[ \t\r\f\v]+')

    def createLexer(self):
        self.addTokens()
        return self.lexer.build()

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener
from parser.DevOpsDSLLexer import DevOpsDSLLexer
from parser.DevOpsDSLParser import DevOpsDSLParser
from interpreter.interpreter import Interpreter
from executor.executor import Executor

def main():
    if sys.stdout.encoding != 'utf-8':
        try: sys.stdout.reconfigure(encoding='utf-8')
        except: pass

    print("[INFO] Iniciando sistema DSL...\n")
    # Permitir pasar archivo por argumento
    file = "script.dsl"
    if len(sys.argv) > 1:
        file = sys.argv[1]

    # Validar que el archivo existe
    if not os.path.exists(file):
        print(f"[ERROR] No existe el archivo: {file}")
        return

    # Cargar archivo DSL
    input_stream = FileStream(file, encoding='utf-8')

    # Lexer y parser
    lexer = DevOpsDSLLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    
    tokens.fill()
    print("=== TOKENS ===")
    for token in tokens.tokens:
        if token.type != Token.EOF:
            name = "<UNKNOWN>"
            if token.type < len(DevOpsDSLParser.symbolicNames) and DevOpsDSLParser.symbolicNames[token.type] != "<INVALID>":
                name = DevOpsDSLParser.symbolicNames[token.type]
            elif token.type < len(DevOpsDSLParser.literalNames) and DevOpsDSLParser.literalNames[token.type] != "<INVALID>":
                name = DevOpsDSLParser.literalNames[token.type].strip("'")
            print(f"Token(type={name}, text='{token.text}')")

    parser = DevOpsDSLParser(tokens)

    # Manejo de errores sintácticos
    parser.removeErrorListeners()
    parser.addErrorListener(ConsoleErrorListener())

    tree = parser.program()
    print("\n[INFO] Árbol sintáctico generado")
    print(tree.toStringTree(recog=parser))

    # Inicializar sistema
    executor = Executor()
    interpreter = Interpreter(executor)

    # Ejecutar
    print("\n=== INTERPRETACIÓN Y EJECUCIÓN ===")
    interpreter.visit(tree)

if __name__ == '__main__':
    main()

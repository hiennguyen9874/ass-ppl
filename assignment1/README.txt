Set environment variable ANTLR_LIB to the file antlr-4.7.1-complete.jar in your computer
Change current directory to initial/src where there is file run.py
Type: python3 run.py gen 
Then type: python3 run.py test LexerSuite
Then type: python3 run.py test ParserSuite
Then type: python3 run.py test ASTGenSuite
Then type: python3 run.py test CheckSuite
Then type: python3 run.py test CodeGenSuite


export ANTLR_LIB=/usr/local/lib/antlr-4.7.1-complete.jar


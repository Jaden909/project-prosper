try:
    exec(compile(open('projectprosper.py').read(),'projectprosper.py','exec'),globals())
except Exception as e:
    print(f'The game crashed. The error was: {e}')
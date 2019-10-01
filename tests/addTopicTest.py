#Test selectAction()

import main as program

app = program.app()
app.setup()
session = app.currentSession
session.addNotebook('test2')
print(session.getCurrentDirectory())
session.fetchUserInput()
code = session.codeReader(session.getUserInput(), '')
session.actionSelect(code)  
print(session.getCurrentDirectory())


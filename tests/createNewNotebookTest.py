#Test selectAction()

import main as program

app = program.app()
app.setup()
session = app.currentSession
notebook = session.notebooks[0]
session.addNotebook('test2')

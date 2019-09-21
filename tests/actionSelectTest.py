#Test selectAction()

import main
#create app
app = main.app('test')
#get user input
app.fetchUserInput()
#assign code
assigmentCode = app.codeReader(app.getUserInput(), app.getPreviousInput())
#call action select
action = app.actionSelect(assigmentCode)
print(action)
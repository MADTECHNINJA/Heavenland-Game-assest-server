#Assest Server
This is a static file hosting server that uses Flask WSGI server. In order to use it you need to have Python 3.x and dependencies required and defined on the reqs/requirements.txt .
Any file under src/static_content will be served directly on

localhost:3030/files/<FILENAME>

Feel free to edit it according to your own desire. Please create a branch for your personal edits. Keep the main brabch clean.

##Requirements
UNIX Like(Mac OS X - Darwin, BSD, GNU/Linux): python3 -m pip install -r reqs/requirements.txt
WinZorT : python -m pip install -r reqs/requirements.txt

##Start
You can use both script based or command based start. Both of them does the same thing and include same commands.
You can find scripts under the bin folder

Script based :

Unix Like(Shell Based) :
		1 - Executable file
				chmod +x bin/execshell.sh
				./bin/execshell.sh
		2 - Direct execution
				bash bin/execshell.sh

Memesoft WinZorT(Garbage based) :
		1 - Executable file :
				Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
				bin\execPowsershell.ps1
				(Be sure that currrent user is admin)
		2 - Direct execution
				Right click on run it as admin
				(WHich you can do both on Unix systems as well)

Direct command line start :

waitress-serve --listen=*:8000 wsgi:app

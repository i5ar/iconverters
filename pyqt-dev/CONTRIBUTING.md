# Contribute

In order to convert the `.iu`  markup to a `.py` script run the command below:

	>>> pyuic4 MainWindow.ui -o MainWindowUi.py
	>>> pyuic4 Form.ui -o FormUi.py

In order to create an `.exe` file run the command below:

	>>> python setup.py py2exe

# Data-Representation-Project

### To run virtual environment follow the steps below: ###
1. Navigate to the project folder on the command line and run the following line.
.\venv\Scripts\activate.bat
2. Run the following line to install all necessary packages.
pip install Requirements.txt
3. Alternatively, run the following lines to install the necessary packages, then freeze these to the requirements text file. 
pip install flask
pip install flask_cors
pip install mysql-connector-python
pip freeze > Requirements.txt
4. Set the flask app using the following line.
set FLASK_APP=server1
5. Run flask.
Flask run
6. If necessary, use the following line to get out of the virtual environment.
deactivate

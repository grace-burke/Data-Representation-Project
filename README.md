# Data-Representation-Project

### To run virtual environment follow the steps below: ###
1. Navigate to the project folder on the command line and run the following line. <br/>
  .\venv\Scripts\activate.bat
2. Run the following line to install all necessary packages.<br/>
  pip install Requirements.txt
3. Alternatively, run the following lines to install the necessary packages, then freeze these to the requirements text file. <br/>
  pip install flask <br/>
  pip install flask_cors <br/>
  pip install mysql-connector-python <br/>
  pip freeze > Requirements.txt
4. Set the flask app using the following line. <br/>
  set FLASK_APP=server1
5. Run flask. <br/>
  Flask run
6. If necessary, use the following line to get out of the virtual environment. <br/>
  deactivate <br/>

### Once server is running in virtual environment, open turbineViewer.html in browser. ###

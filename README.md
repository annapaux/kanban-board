# Kanban-Board
This app lets users register, log in, and maintain a personalized kanban board to keep track of tasks that are to-do, doing, or done.



### Set Up

Download or clone the kanban-board folder.
Navigate into the folder to run the following commands.
```cd .../kanban-board```

### Virtual Environment and Requirements
```python
python3.6 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

### Initiating the Database and Running the App
```
export FLASK_APP=kanban
export FLASK_ENV=development
flask init-db
flask run
```

### Visit the App
localhost:5000/

 
### Unit Testing with Pytest 
 Navigate into the folder to run the following commands.
```cd .../kanban-board```
```python3 -m pytest```

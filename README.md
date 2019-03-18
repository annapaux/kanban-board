Installation:

cd [projectfolder]

python3.6 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

export FLASK_APP=kanban
export FLASK_ENV=development
flask init-db
flask run

python3 -m pytest

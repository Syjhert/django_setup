python -m venv myenv
myenv\Scripts\activate    (or)   source myenv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
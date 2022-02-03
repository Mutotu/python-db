# first of all always run commands in regular terminal for python

pip3 => it is like npm for Js. A package manager.
=> It'll create packages like package.json
======
pip3 uninstall "the name of the file" => to get there write " pip3 list " and you'll see the packages installed globall
======
python3 -m venv virtual_environment => Smilar to node_modules for js
======
source virtual_environment/bin/activate => this activates the packages and in return you should see =>>>> (virtual_environment)As-MacBook-Pro:python-db ab$
======
deactivate ==> to get out of the (virtual_environment) As-MacBook-Pro:python-db ab$
======
add virtual_environment to .ignore
======
pip3 install alembic ==> install dependencies
======
alembic init migrations => to create migration folders
======
comment out with ";" => sqlalchemy.url = driver://user:pass@localhost/dbname in alembic.ini
=====
pip3 install python-dotenv ==> to add the dependency
=====
alembic upgrade head ===>>>> like sequelize db:migrate
=> though we haven't done any migration ready we still run it to see the errors and what else to do.(Most likely it'll be "KeyError: 'url'" )
=====
==>add
from dotenv import load_dotenv
import os
load_dotenv()
db_url = os.environ.get("DATABASE_URL")

# =>to env.py

create a file .env at the top folder level
and add DATABASE_URL=postgresql://@localhost:5432/pyton_db_codealong
=====
add config.set_main_option("sqlalchemy.url", db_url) in env.py file where the config is.
======
install pip3 install psycopg2
======
create a database createdb name of databse
======
run alembic upgrade head to see if everything worked
======
run alembic revision -m create-dinos => create versions file
similar to sequlelize db:migrate ---
======
in versionsfile where we have the datafile =>
we add
def upgrade():
op.create_table(
'dinos',
sa.Column('id', sa.Integer, primary_key=True),
sa.Column('name', sa.String, nullable=False, unique=True),
sa.Column('type', sa.String, )
)

def downgrade():
op.drop_table('dinos')
==>unlike sequelize
=======
run alembic upgrade head
======
to drop tables run alembic downgrade -1
=====
in psql run => insert into dinos (name,type) values ('test1 name', 'test1 type');
=====
create a file "models.py" at the root level
=====
run =>pip3 install flask_sqlalchemy
====
go to models.py to check out in the folder so you know whats oin on
======
create a file named application.py at tthe root level
=====
check out application.py inside the folder
=====
run python3 application.py => like nodemon
=====
FLASK_APP='application.py' flask routes
=> similar to rowdy router
=======
to create alembic revision -m create-categories
=======
then run alembic upgrade head
=====
to readd
alembic revision -m add_category_id_to_dinos
=====

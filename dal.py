import sqlalchemy as dbtools
from sqlalchemy.orm import sessionmaker
from werkzeug.exceptions import abort
import sys
sys.path.append('mappers')
from mappers import datianagrafici as myDB


# to create ORM mapping:
# sqlacodegen --tables datianagrafici --outfile D:/work/PycharmProjects/pythonProject/project1/mappers/datianagrafici.py mysql+mysqlconnector://root:marc0@localhost:3306/ordinecollegioweb

# funzione per ottenere una session di accesso al db
def get_db_session():
    # use sqlalchemy ORM
    engine = dbtools.create_engine('mysql+mysqlconnector://root:marc0@localhost:3306/ordinecollegioweb')

    Session = sessionmaker(bind=engine)
    session = Session()

    return session


# funzione per ottenere un nominativo specifico su ID
def get_single_person_data(person_id):
    mysession = get_db_session()

    persondata = mysession.query(myDB.Datianagrafici).filter(myDB.Datianagrafici.idDatiAnagrafici == person_id).one()

    if persondata is None:
        abort(404)
    return persondata


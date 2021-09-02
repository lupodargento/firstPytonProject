from flask import Flask, render_template
from dal import get_db_session, get_single_person_data
import sys
sys.path.append('mappers')
from mappers import datianagrafici as myDB


def main():
    mysession = get_db_session()

    person = get_single_person_data(2)
    print(person.Nome1 + " " + person.Cognome1)

if __name__ == "__main__":
    main()
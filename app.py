# SET FLASK_APP=<nome_file_pyton>
# SET FLASK_ENV=developement

from flask import Flask, render_template, request, url_for, flash, redirect
from dal import get_db_session, get_single_person_data
import sys
sys.path.append('mappers')
from mappers import datianagrafici as myDB

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pippiripettenusa'


@app.route('/')
def index():
    mysession = get_db_session()

    persone = mysession.query(myDB.Datianagrafici).order_by(myDB.Datianagrafici.idDatiAnagrafici)
    return render_template("index.html", people=persone)


@app.route('/<int:person_id>')
def person(person_id):
    person = get_single_person_data(person_id)
    return render_template('person.html', person=person)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        nome1 = request.form['nome1']
        cognome1 = request.form['cognome1']

        if not nome1:
            flash('Attenzione!!! Inserire il primo nome.')

        elif not cognome1:
            flash('ATTENZIONE!!! Inserire il primo cognome.')

        else:
            mysession = get_db_session()
            newpersona = myDB.Datianagrafici(Cognome1=cognome1, Nome1=nome1)
            mysession.add(newpersona)
            mysession.commit()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    mysession = get_db_session()
    person = mysession.query(myDB.Datianagrafici).filter(myDB.Datianagrafici.idDatiAnagrafici == id).one()

    if request.method == 'POST':
        nome1 = request.form['nome1']
        cognome1 = request.form['cognome1']

        if not nome1:
            flash('Attenzione!!! Inserire il primo nome.')

        elif not cognome1:
            flash('ATTENZIONE!!! Inserire il primo cognome.')

        else:
            person.Nome1 = nome1
            person.Cognome1 = cognome1
            mysession.commit()
            return redirect(url_for('index'))

    return render_template('edit.html', person=person)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    mysession = get_db_session()
    person = mysession.query(myDB.Datianagrafici).filter(myDB.Datianagrafici.idDatiAnagrafici == id).one()

    mysession.delete(person)
    mysession.commit()

    flash('"{}" è stato cancellato correttamente!'.format(person.Cognome1))
    return redirect(url_for('index'))
import datetime
import os
import re

from flask import *

from Model import Auteur, Oeuvre

bp = Blueprint('oeuvre', __name__, url_prefix='/oeuvre')


def get_auteurs_by_id():
    res = dict()

    for a in Auteur.list():
        res[a['idAuteur']] = a['nomAuteur']

    return res

@bp.route('/show')
def show():
    return render_template('oeuvre/showOeuvre.html.jj2', oeuvres=Oeuvre.list(), auteurs=get_auteurs_by_id())


@bp.route('/supprimer/<int:id>', methods=['GET'])
def supprimer(id):
    oeuvre = Oeuvre.get(id)

    if not oeuvre:
        abort(404)

    Oeuvre.delete(id)

    return redirect(url_for('oeuvre.show'))


@bp.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'GET':
        return render_template('oeuvre/addOeuvre.html.jj2',
                               auteurs=Auteur.list(), errors=dict())

    valid, errors = valider_form()

    if valid:
        oeuvre = Oeuvre.insert(request.form['titre'],
                               request.form['dateParution'],
                               request.form['photo'],
                               request.form['prix'],
                               request.form['auteur_id'])

        return redirect(url_for('oeuvre.show'))
    else:
        return render_template('oeuvre/addOeuvre.html.jj2',
                               auteurs=Auteur.list(), errors=errors)


@bp.route('/modifier/<int:id>', methods=['GET', 'POST'])
def modifier(id):
    oeuvre = Oeuvre.get(id)

    if not oeuvre:
        abort(404)

    if request.method == 'GET':
        return render_template('oeuvre/editOeuvre.html.jj2',
                               oeuvre=oeuvre, auteurs=Auteur.list(),
                               errors=dict())

    valid, errors = valider_form()

    if valid:
        photo = request.form['photo']

        if not photo:
            photo = 'no_photo.jpeg'

        Oeuvre.update(id,
                      request.form['titre'],
                      request.form['dateParution'],
                      photo,
                      request.form['prix'],
                      request.form['auteur_id'])

        return redirect(url_for('oeuvre.show'))
    else:
        return render_template('oeuvre/editOeuvre.html.jj2',
                               oeuvre=oeuvre, auteurs=Auteur.list(),
                               errors=errors)


def valider_form():
    valid = True
    errors = dict()

    auteur = Auteur.get(request.form['auteur_id'])

    if not auteur:
        # flash("Auteur n'existe pas")
        errors['auteur'] = "Auteur n'existe pas"
        valid = False

    if not re.match(r'\w{2,}', request.form['titre']):
        # flash('Titre doit avoir au moins deux caractères')
        errors['titre'] = "Titre doit avoir au moins deux caractères"
        valid = False

    try:
        datetime.datetime.strptime(request.form['dateParution'], '%Y-%m-%d')
    except ValueError:
        # flash("Date n'est pas valide")
        errors['dateParution'] = "Date n'est pas valide"
        valid = False

    if request.form['photo']:
        photo_path = os.path.join(current_app.root_path,
                                  'static', 'assets', 'images', request.form['photo'])

        if not os.path.isfile(photo_path):
            # flash(f"Photo n'existe pas: { photo_path }")
            errors['photo'] = f"Photo n'existe pas: { photo_path }"
            valid = False

    try:
        float(request.form['prix'])
    except ValueError:
        # flash("Prix n'est pas valide")
        errors['prix'] = "Prix n'est pas valide"
        valid = False

    return (valid, errors)

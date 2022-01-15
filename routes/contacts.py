from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@contacts.route('/new', methods=['POST'])
def add_contact():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']

    new_contact = Contact(fullname,email,phone)
    db.session.add(new_contact)
    db.session.commit()

    flash('Contact added successfully!')

    return redirect(url_for('contacts.index'))

@contacts.route('/about')
def about():
    return render_template('about.html')

@contacts.route('/update/<id>', methods= ['POST', 'GET'])
def update(id):
    if request.method == 'POST':
        contact = Contact.query.get(id)
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        db.session.commit()

        flash('Contact updated successfully!')

        return redirect(url_for('contacts.index'))

    contact = Contact.query.get(id)
    return render_template('update.html', contact=contact)

@contacts.route('/delete/<id> ')
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    flash('Contact deleted successfully!')

    return redirect(url_for('contacts.index'))
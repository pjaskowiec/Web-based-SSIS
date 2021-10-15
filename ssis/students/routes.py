from flask import Blueprint, request, render_template, redirect, flash
from flask.helpers import url_for
from .utils import add_student_to_db, update_student_record, save_image
from ssis.models.student import Student
from ssis.models.course import Course
from ssis.models.college import College
from ssis.admin.utils import admin_found

student = Blueprint(name='student', import_name=__name__)


@student.route('/', methods=['GET', 'POST'])
def students():
    username = request.form.get('username')
    password = request.form.get('password')
    students = Student().get_all()
    courses = Course().get_all()
    colleges = College().get_all()

    if request.method == 'POST ':
        if admin_found(username, password):
            return render_template(
                'students.html', 
                data = [students,courses,colleges], 
                datacount = f'{len(students)} Students')
        else:
            return redirect(url_for('login'))
    else:
        return render_template(
            'students.html', 
            data = [students,courses,colleges],
            datacount = f'{len(students)} Students')



@student.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':

        user_input = request.form.get('user-input')
        field = request.form.get('field')
        print(user_input,field)

        if field == 'select':
            result = Student().search(keyword=user_input)
        elif field == 'id':
            result = Student().search(keyword=user_input, field='id')
        elif field == 'first':
            result = Student().search(keyword=user_input, field='firstname')
        elif field == 'middle':
            result = Student().search(keyword=user_input, field='middlename')
        elif field == 'last':
            result = Student().search(keyword=user_input, field='lastname')
        elif field == 'gender':
            result = Student().search(keyword=user_input, field='gender')
        elif field == 'year':
            result = Student().search(keyword=user_input, field='year')
        elif field == 'course':
            result = Student().search(keyword=user_input, field='course')
        else:
            result = []

        if len(result) != 0:
            return render_template(
                'students.html', 
                data=[result],
                datacount = f'Search Result: {len(result)}')
        else:
            return redirect(url_for('/'))
    else:
        return redirect(url_for('homepage'))



@student.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        image = request.files['selected-image']
        try:
            filename = save_image(image, '\static\entity_photos\students')
        except:
            print("Can't save image")
        
        student = {
            'id': request.form.get('student-id'),
            'firstname': request.form.get('firstname'),
            'middlename': request.form.get('middlename'),
            'lastname': request.form.get('lastname'),
            'gender': request.form.get('gender'),
            'yearlevel': request.form.get('yearlevel'),
            'course': request.form.get('course'),
            'photo': filename
        }
        add_student_to_db(student)
        flash(f'{student["firstname"]} is added succesfully!', 'info')
        return redirect(url_for('homepage'))
    else:
        return redirect(url_for('homepage'))



@student.route('/update/<string:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':

        student = {
            'id': id,
            'firstname': request.form.get('firstname'),
            'middlename': request.form.get('middlename'),
            'lastname': request.form.get('lastname'),
            'gender': request.form.get('gender'),
            'yearlevel': request.form.get('yearlevel'),
            'course': request.form.get('course')
        }
        update_student_record(student)
        flash(f"{student['firstname']}'s data has been changed succesfully!", 'info')
        return redirect(url_for('homepage'))
    else:
        return redirect(url_for('homepage'))



@student.route('/delete/<string:id>')
def delete(id):
    data = Student().get_student(id)
    Student().delete(id)
    flash(f'{data[0]} deleted from the database.', 'info')
    return redirect(url_for('homepage'))
from flask import flash, render_template, redirect, url_for
from models import Class, Course, Student, Teacher
from forms import questionnaireForm
from app import app, db
import sqlite3
from sqlite3 import Error


@app.route('/')
@app.route('/index')
@app.route('/home')
def homepage():
    return render_template("home.html")


@app.route('/questionnaire', methods=['GET','POST'])
def questionnaire():
    form = questionnaireForm()
    form.student_id.choices = [(user.id, user.name) for user in Student.query.all()]
    form.Homeroom_teacher.choices = [(Teacher.id, Teacher.name) for Teacher in Teacher.query.all()]
    form.Favourite_course.choices = [(Course.id, Course.name) for Course in Course.query.all()]
    form.First_pref.choices = [(Student.id, Student.name) for Student in Student.query.all()]
    form.Second_pref.choices = [(Student.id, Student.name) for Student in Student.query.all()]
    form.Third_pref.choices = [(Student.id, Student.name) for Student in Student.query.all()]

    if form.validate_on_submit():
        student_id = form.student_id.data
        teacher_id = form.Homeroom_teacher.data
        course_id = form.Favourite_course.data
        First_pref = form.First_pref.data
        Second_pref = form.Second_pref.data
        Third_pref = form.Third_pref.data

        student = Student.query.get_or_404(student_id)
        clss = Class.query.filter_by(teacher_id=teacher_id).first()
        student.course_preference = course_id
        student.partner_1_id = First_pref
        student.partner_2_id = Second_pref
        student.partner_3_id = Third_pref
        db.session.commit()
        # Redirect to a success page or another route
        flash('Usage Entry Successful!', 'success')
        return redirect( url_for('questionnaire') )
    
    return render_template("questionnaire.html", form=form)

@app.route('/summary')
def summary():
    results1 = execute_sql('insight.sql')
    results2 = execute_sql('insight2.sql')
    results3 = execute_sql('insight3.sql')
    print(results2)
    A = [x for x in results2 if x[1]=='1A' ]
    B = [x for x in results2 if x[1]=='1B' ]
    C = [x for x in results2 if x[1]=='1C' ]

    return render_template("summary.html", columns=results1, resultA=A, resultB=B, resultC=C, columns3=results3)


def execute_sql(sql_filename):
    db_filename = r"db.sqlite3"
    # SQL DML script to Glean insights
    try:
        with open(sql_filename,'r') as dml_script:
            dml = dml_script.read()
        # Connect to SQLite database
        with sqlite3.connect(db_filename) as db:
        # Create a cursor object
            cs = db.cursor()
        # Execute SQL DML script to insert data
            cs.execute(dml)
            results = cs.fetchall()
            return results
    except Error as e:
        print(e)
        db.rollback()
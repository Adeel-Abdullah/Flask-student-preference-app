from flask import flash, render_template, redirect, url_for
from models import Class, Course, Student, Teacher
from forms import questionnaireForm
from app import app, db


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
    #Pre-populate your form here:
    # form.username.data = user_version.username
    return render_template("questionnaire.html", form=form)
from flask_sqlalchemy import SQLAlchemy
from extensions import db


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    classes = db.relationship('Class', backref='teacher', uselist=False, lazy=True)

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(2), nullable=False)  # Class identifier (e.g., '1A', '1B', '1C')
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    students = db.relationship('Student', backref='classroom', lazy=True)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    course_preference = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)  # Store course preference directly in Student table
    partner_1_id = db.Column(db.Integer, db.ForeignKey('student.id'))  # ID of 1st preferred partner
    partner_2_id = db.Column(db.Integer, db.ForeignKey('student.id'))  # ID of 2nd preferred partner
    partner_3_id = db.Column(db.Integer, db.ForeignKey('student.id'))  # ID of 3rd preferred partner

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

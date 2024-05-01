from collections.abc import Sequence
from typing import Any, Mapping
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError
from models import Class, Teacher
from app import app

class questionnaireForm (FlaskForm):
    student_id = SelectField('User', coerce=int, validators=[DataRequired()])
    Homeroom_teacher = SelectField('Teacher', coerce=int, validators=[DataRequired()])
    Favourite_course = SelectField('Favourite Course', coerce=int, validators=[DataRequired()])
    First_pref = SelectField('First Partner Preference', coerce=int, validators=[DataRequired()])
    Second_pref = SelectField('Second Partner Preference', coerce=int, validators=[DataRequired()])
    Third_pref = SelectField('Third Partner Preference', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')

    def get_teacher_class(self, field):
        if field.data:
            clss = Class.query.filter_by(teacher_id=field.data).first()
            teacher = Teacher.query.get_or_404(clss.teacher_id)
            print(teacher.name)
            return teacher.name

    def validate(self,  extra_validators=None):
        if not super().validate(extra_validators):
            return False
        result = True
        
        teacher_name=self.get_teacher_class(self.Homeroom_teacher)

        if teacher_name == Teacher.query.get_or_404(self.Homeroom_teacher.data).name:
            result = True
        else:
            result = False
            self.Homeroom_teacher.errors.append("Please Enter your Homeroom Teacher.")

        seen = set()
        for field in [self.First_pref, self.Second_pref, self.Third_pref]:
            if field.data == self.student_id.data:
                field.errors.append('Students can not partner with themselves.')
                result = False
            if field.data in seen:
                field.errors.append('Please select three distinct partners.')
                result = False
            else:
                seen.add(field.data)
        return result


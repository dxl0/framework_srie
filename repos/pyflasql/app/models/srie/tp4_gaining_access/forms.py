# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Create forms to be passed to the frontend
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, InputRequired, Length, ValidationError


class HydraForm(FlaskForm):
    ip= StringField(validators=[
        InputRequired(), Length(min = 2, max = 50)], render_kw={"placeholder" : "IP"}
    )
    usernames= StringField(validators=[
        InputRequired(), Length(min = 2, max = 50)], render_kw={"placeholder" : "Usernames path"}
    )
    passwords= StringField(validators=[
        InputRequired(), Length(min = 2, max = 50)], render_kw={"placeholder" : "Passwords path"}
    )

    submit = SubmitField('Brute force')
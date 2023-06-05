# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Create forms to be passed to the frontend
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, InputRequired, Length, ValidationError, NumberRange


class PingAddrForm(FlaskForm):
    ip_address = StringField(validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "IP Address"})
    
    npings = IntegerField(validators=[
        NumberRange(min=1, max=100)], render_kw={"placeholder": "Number of pings"}, default=3)
    
    submit = SubmitField('Ping')

class NmapForm(FlaskForm):
    range_ip = StringField(validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Range of IP"}
    ) 
 
    submit = SubmitField('Scan')

class PortsForm(FlaskForm):
    ip = StringField(validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "IP"}
    ) 
 
    submit = SubmitField('Scan')

class NessusButton(FlaskForm):
    submit = SubmitField('Start Nessus Process')

class TraceRouteForm(FlaskForm):
    ip = StringField(validators=[
        InputRequired(), Length(min = 2, max = 50)], render_kw={"placeholder" : "ip"}
    )

    submit = SubmitField('Trace the route')

class DnsForm1(FlaskForm):
    domain1 = StringField(validators=[
        InputRequired(), Length(min = 2, max = 50)], render_kw={"placeholder" : "Domain"}
    )

    submit = SubmitField('Recon DNS')

class DnsForm2(FlaskForm):
    domain2 = StringField(validators=[
        InputRequired(), Length(min = 2, max = 50)], render_kw={"placeholder" : "Domain"}
    )

    submit = SubmitField('Enum DNS')

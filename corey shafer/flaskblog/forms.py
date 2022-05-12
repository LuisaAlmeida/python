from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from email_validator import validate_email, EmailNotValidError, caching_resolver


class RegistrationFrom(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    resolver = caching_resolver(timeout=10)
    email = validate_email(, dns_resolver=resolver).email
    try:
        # Validate & take the normalized form of the email
        # address for all logic beyond this point (especially
        # before going to a database query where equality
        # does not take into account normalization).
        email = validate_email(email).email
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        print(str(e))

    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginFrom(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign Up')
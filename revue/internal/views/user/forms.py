from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Length, Email


class UpdateUserInfoForm(Form):
    firstName = StringField(
        'First Name',
        validators=[InputRequired(), Length(min=2, max=60)]
    )
    lastName = StringField(
        'Last Name',
        validators=[InputRequired(), Length(min=2, max=60)]
    )
    submit = SubmitField('Save')

    def set_user(self, user):
        self.firstName.default = user.firstName
        self.lastName.default = user.lastName


class UpdateUserPasswordForm(Form):
    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=6, max=25)]
    )
    password_repeat = PasswordField(
        'Repeat Password',
        validators=[InputRequired(), EqualTo('password',
                                             message='Passwords must match.')]
    )
    submit = SubmitField("Update password")

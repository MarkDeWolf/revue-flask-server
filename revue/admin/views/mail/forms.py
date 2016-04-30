from flask.ext.wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import InputRequired, Email

from revue.models.mail import MailingAddressIntern
from revue.utilities.forms import Unique


class CreateMailingListForm(Form):
    name = StringField(
        'Name',
        validators=[InputRequired(),
                    Unique(MailingAddressIntern, MailingAddressIntern.name, "This address is already in use")]
    )
    submit = SubmitField('Save')


class AddMailingListEntryForm(Form):
    address = StringField(
        'Address',
        validators=[InputRequired(),
                    Email()]
    )
    submit = SubmitField('Add')

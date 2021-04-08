from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators = [DataRequired()])
    photo = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], "Please check format, only PNG and JPG images are allowed!")])
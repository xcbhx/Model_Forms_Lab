from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from books_app.models import Audience, Book, Author, Genre
from wtforms import TextAreaField

class BookForm(FlaskForm):
    """Form to create a book."""
    title = StringField('Book Title', 
        validators=[
            DataRequired(), 
            Length(min=3, max=80, message="Your message needs to be betweeen 3 and 80 chars")
        ])
    publish_date = DateField('Date Published', validators=[DataRequired()])
    author = QuerySelectField('Author', query_factory=lambda: Author.query.all(), allow_blank=False, get_label='name')
    audience = SelectField('Audience', choices=Audience.choices())
    genres = QuerySelectMultipleField('Genres', query_factory=lambda: Genre.query.all(), get_label='name')
    submit = SubmitField('Submit')

    def validate_title(form, field):
        if 'banana' in field.data:
            raise ValidationError('Title cannot contain the word banana')


class AuthorForm(FlaskForm):
    """Form to create an author."""
    name = StringField('Author Name', validators= [
        DataRequired(),
        Length(min=2, max=100, message="Name must be between 2 and 100 characters")
    ])
    biography = TextAreaField('Biography', validators=[
        DataRequired(),
        Length(min=10, message="Biography must be between 10 characters long")
    ])
    submit = SubmitField('Submit')

    # STRETCH CHALLENGE: Add more fields here as well as in `models.py` to
    # collect more information about the author, such as their birth date,
    # country, etc.


class GenreForm(FlaskForm):
    """Form to create a genre."""
    name = StringField('Genre Name', validators= [
        DataRequired(),
        Length(min=2, max=100, message="Name must be between 2 and 100 characters")
    ])
    submit = SubmitField('Submit')
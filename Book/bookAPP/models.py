from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Book(models.Model):
    FICTION = 'Fiction'
    NON_FICTION = 'Non-Fiction'
    SCIENCE = 'Science'
    HISTORY = 'History'
    FANTASY = 'Fantasy'
    MYSTERY = 'Mystery'
    BIOGRAPHY = 'Biography'
    POETRY = 'Poetry'
    ROMANCE = 'Romance'
    ADVENTURE = 'Adventure'
    THRILLER = 'Thriller'
    CHILDREN = 'Children'
    ART = 'Art'
    DRAMA = 'Drama'
    COMIC = 'Comic'
    CLASSIC = 'Classic'
    COOKING = 'Cooking'
    SELF_HELP = 'Self-Help'
    PHILOSOPHY = 'Philosophy'
    RELIGION = 'Religion'

    GENRE_CHOICES = [
        (FICTION, 'Fiction'),
        (NON_FICTION, 'Non-Fiction'),
        (SCIENCE, 'Science'),
        (HISTORY, 'History'),
        (FANTASY, 'Fantasy'),
        (MYSTERY, 'Mystery'),
        (BIOGRAPHY, 'Biography'),
        (POETRY, 'Poetry'),
        (ROMANCE, 'Romance'),
        (ADVENTURE, 'Adventure'),
        (THRILLER, 'Thriller'),
        (CHILDREN, 'Children'),
        (ART, 'Art'),
        (DRAMA, 'Drama'),
        (COMIC, 'Comic'),
        (CLASSIC, 'Classic'),
        (COOKING, 'Cooking'),
        (SELF_HELP, 'Self-Help'),
        (PHILOSOPHY, 'Philosophy'),
        (RELIGION, 'Religion'),
    ]

    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Max 99999999.99

    def __str__(self):
        return self.title
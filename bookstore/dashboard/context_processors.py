from .models import (
	Topic,
	Language,
	Country,
	Book)


def details(request):
	# create list of books
	books = Book.objects.all()
	books = [book.title for book in books]

	# create list of topic names
	topics = Topic.objects.all()
	topics = [topic.name for topic in topics]

	# create list of lanuages
	languages = Language.objects.all()
	languages = [language.name for language in languages]
	
	# create list of countries
	countries = Country.objects.all()
	countries = [country.name for country in countries]

	return {
	    'booknames': books,
	    'topics': topics,
	    'languages': languages,
	    'countries': countries
	}

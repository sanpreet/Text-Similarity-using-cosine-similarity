from api import *
from api.views import text_similairty_based_method, user_input_html 
# this is the decorator
# this will show the html page
@app.route('/')
def user_input():
	return user_input_html()

# this is the decorator
# once the submit button is executed this url is fetched and 
# function with respect to this url is executed
# functions are defined in the views.py
@app.route('/text_similarity', methods=['GET', 'POST'])
def cosine_based_similarity():
	return text_similairty_based_method()



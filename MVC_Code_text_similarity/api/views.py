from api import *
import json
from flask import request, render_template
from api.models import Text_Similarity_Score
from api.process_file import object_document_similar

# this is used to render ytthe html page
def user_input_html():
	return render_template('user_input.html')

def text_similairty_based_method():
	if request.method == 'POST':
		Text1 = request.form['Text1']
      # getting the second text
		Text2 = request.form['Text2']
      # calcualating the score using object of the class DocumentSimilarity 
		output_score = object_document_similar.cosine_sim(Text1, Text2)
	# object of the class has been created.
	# this object has the power to access the functions as well as members of class	
		text_Similarity_Score_object = Text_Similarity_Score(
										text_score = str(output_score)
		) 
	# adding the value in the database.	
		db.session.add(text_Similarity_Score_object)
		db.session.commit()
	return ("Entry has been added to the database:")	



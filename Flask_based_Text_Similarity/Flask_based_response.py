# Flask is a web framework
from flask import Flask,request
# importing the object from the class DocumentSimilarity mentioned in file Text_Similarity.py
from Text_Similarity import object_document_similar
# for saving the data in mysql database
import mysql.connector

# naming object of the flask class as app which runs at the end
app = Flask(__name__)

# this is the link which is mentioned in the form action html page
@app.route('/text_similarity',methods = ['POST'])
# At the above route this function is implemened. @ means decorator
def text_similarity():
   # request method is POST which is mentioned in the html page
   if request.method == 'POST':
      # getting the first text
      Text1 = request.form['Text1']
      # getting the second text
      Text2 = request.form['Text2']
      # calcualating the score using object of the class DocumentSimilarity 
      output_score = object_document_similar.cosine_sim(Text1, Text2)
      # creating the connection with the database. Use your username as well as database
      db = mysql.connector.connect(host="localhost", user="xxx", password="xxx", database="text_similarity")
      # if everything is okay, this step will be executed
      print("connection successful")
      # creating the object of the database
      # object can access the member functions as well as variables of the class
      cursor = db.cursor()
      # writing the query for inserting the score in the database
      sql = "INSERT INTO text_similarity_score(Text_Score) VALUES (%s)"
      # inserting the value in the database
      val = ([str(output_score)])
      cursor.execute(sql, val)
      # commiting the value
      db.commit()
      # closing the object
      db.close()
   # function must return so a good message is displayed at the end
   return "thank you, your database is saved"   
    
# running the application using this code.......    
if __name__ == '__main__':
   app.run(debug = True)

# it gets binds to the api folder
from api import *

# running the app from here
if __name__ == '__main__':
	db.create_all()
	app.run(host="0.0.0.0", debug=True)
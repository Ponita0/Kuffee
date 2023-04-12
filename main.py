import threading
from flask import*
import test
import string
import random
import turtle
import logging
import requests
from logging.handlers import RotatingFileHandler


app = Flask(__name__)

# Set up logging
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# home page
@app.route('/', methods=['GET', 'POST'])
def home():
   return render_template('home.html')


# the page to wait in during the creation of the grid
@app.route('/wait', methods=['GET', 'POST'])
def wait():   
   print(request.form.get('width'))
   print(request.form.get('height'))
   return render_template('waiting.html', width =request.form.get('width'),height = request.form.get('height'),type=request.form.get('type') )


# request to create the grid
@app.route('/generate', methods=['GET', 'POST'])
def generate():
   
   # Replace the URL below with your own webhook URL
   webhook_url = "https://discord.com/api/webhooks/1095820180547960872/Ghd4UMEcto4lN6k6KLd686qQwz1tD18Zza8UqU2egyoXmigbep_cKAWCwexrfKUWLuIP"

# Define the message payload
   payload = {
    "username": "Notif",
    "avatar_url": "https://cdn.britannica.com/58/129958-050-C3FE2DD2/Adolf-Hitler-1933.jpg",
    "content": "Someone requested to create a grid"
   }

# Send the webhook request
   response = requests.post(webhook_url, json=payload)

# Check if the request was successful
   if response.status_code == 204:
      print("Webhook sent successfully!")
   else:
    print(f"Failed to send webhook. Error: {response.text}")
   letters = string.ascii_letters
   letters = ''.join(random.choice(letters) for i in range(5)) 
   print ("Generated string : ", letters)
   x = int(request.args.get('width'))
   y = int(request.args.get('height'))
   type = int(request.args.get('type'))
   print("received dimensions: ", x, y)   
   if type==1:    
      letters="[CircWithLines]"+letters
      test.circWithLines(44,7,letters)                  
   elif type==2:          
    letters="[CircularGrid]"+letters
    test.circularGrid(x, 1, 2,letters,y)
   elif type==3:
    letters="[CircWithRect]"+letters
    test.circWithRect(x,y,600,30,letters)
                       

    # Save the image and return it to the client
   return send_file('static/files/[Ibrahim Abdelmonem] %s.eps' % letters)   
   #return render_template('home.html', x =request.form.get('width'),y = request.form.get('height') )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)


import threading
from flask import*
import test
import string
import random
import logging
import requests
import datetime
import os
from dotenv import load_dotenv
from logging.handlers import  RotatingFileHandler


app = Flask(__name__)
load_dotenv()

# Set up logging
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)


#error page
@app.route('/success',methods=['GET'])
def success():
   return render_template('success.html')

@app.route('/error',methods=['GET'])
def error(err):
  return render_template('error.html',msg=err)  
# home page
@app.route('/', methods=['GET', 'POST'])
def home():
   webhook_url = os.environ.get('visit')
   UA = request.headers.get('User-Agent')
   ip_address = request.remote_addr         
   embed = {
    "title": "New Visit !",    
    "color": 0x1a6262,
    "author": {
        "name": "Visits bot",
        "url": "https://www.example.com/",
        "icon_url": "https://icones.pro/wp-content/uploads/2022/03/historique-icone-de-l-historique-noir.png"
    },
    "fields": [
        {
          "name": "ip_address",
          "value": ip_address,
          "inline": True
        },
        {
          "name": "User agent",
          "value": UA
        }       
      ],
      "footer": {
         "text": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
           "icon_url": "https://illustoon.com/photo/7652.png"
       }
   }
   data = {
       "username": "Visits Bot",
    "avatar_url": "https://cdn.britannica.com/58/129958-050-C3FE2DD2/Adolf-Hitler-1933.jpg",    
    "embeds": [embed]
   }     



#    response = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})


# # Check if the request was successful
#    if response.status_code == 204:
#       print("Webhook sent successfully!")
#    else:
#     print(f"Failed to send webhook. Error: { response.text }")
   return render_template('home.html')


@app.route('/g1',methods=['GET'])
def g1():  
  return render_template('g1.html' )  

@app.route('/g2',methods=['GET'])
def g2():
  return render_template('g2.html' )  

@app.route('/g3',methods=['GET'])
def g3():
  return render_template('g3.html' )  

@app.route('/pdf',methods=['GET'])
def pdf():
   return render_template('pdf.html')
   
@app.route('/g4',methods=['GET'])
def g4():
  return render_template('g4.html' )  

@app.route('/g5',methods=['GET'])
def g5():
  return render_template('g5.html' )  

@app.route('/EpsToPdf',methods=['POST'])
def EpsToPdf():
   a=request.form.get('filePath')
   test.EpsToPdf(a)   
   return send_file('static/files/'+a.replace('.eps','.pdf'))
# the page to wait in during the creation of the grid
@app.route('/wait', methods=['GET', 'POST'])
def wait():   
   print(request.form.get('width'))
   print(request.form.get('height'))   
   return render_template('waiting.html', width =request.form.get('width'),height = request.form.get('height'),type=request.form.get('type') )


# request to create the grid
@app.route('/generate', methods=['GET', 'POST'])
def generate():
   webhook_url = os.environ.get('generate')
   if request.args.get('width').isnumeric() == False or request.args.get('height').isnumeric()== False:
      return error("يلزم كتابة المطلوب من الارقام و باللغة الانجليزية")
   UA = request.headers.get('User-Agent')
   ip_address = request.remote_addr         
   embed = {
    "title": "New generation request !",    
    "color": 0x1a6262,
    "author": {
        "name": "Generation bot",
        "url": "https://www.example.com/",
        "icon_url": "https://icon-library.com/images/add-icon-png/add-icon-png-10.jpg"
    },
    "fields": [
        {
          "name": "ip_address",
          "value": ip_address,
          "inline": True
        },
        {
          "name": "User agent",
          "value": UA
        },
        {
          "name": "grid type",
          "value": request.args.get("type"),
          "inline": True

        },
        {
          "name": "Width",
          "value": request.args.get("width"),
           "inline": True
        }  ,
        {
          "name": "Height",
          "value": request.args.get("height"),
           "inline": True
        }               
      ],
      "footer": {
         "text": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
           "icon_url": "https://illustoon.com/photo/7652.png"
       }
   }

   data = {
       "username": "Generation Bot",
    "avatar_url": "https://cdn.britannica.com/58/129958-050-C3FE2DD2/Adolf-Hitler-1933.jpg",    
    "embeds": [embed]
   }     

   response = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})


# Check if the request was successful
   if response.status_code == 204:
      print("Webhook sent successfully!")
   else:
    print(f"Failed to send webhook. Error: {response.text}")
   # Replace the URL below with your own webhook URL
   letters = string.ascii_letters
   letters = ''.join(random.choice(letters) for i in range(5)) 
   print ("Generated string : ", letters)
   x = int(request.args.get('width'))
   y = int(request.args.get('height'))
   type = int(request.args.get('type'))
   print("Recived : X: ",x, ", Y : ", y , " , Type : ",type)   
   if type==1:
      if x>150:
        return error("اييييييييه؟ هتكتب ألفية ابن مالك؟")    
      if y>25:
        return error("بذمتك مش مكسوف من نفسك و انت عايز تبني برج خليفه على شبكة كوفي")            
      letters=f"[شعاعية 1][{x}x{y}]"+letters   
      test.circWithLines(x,y,letters)                  
   elif type==2:
    if y>25:
        return error("بذمتك مش مكسوف من نفسك و انت عايز تبني برج خليفه على شبكة كوفي")    
    if x>150:
        return error("اييييييييه؟ هتكتب ألفية ابن مالك؟")    
    letters=f"[شعاعية 2][{x}x{y}]"+letters   
    test.circWithRect(y,x,850,letters)

   elif type==3:    
    if y>150:
        return error("اييييييييه؟ هتكتب ألفية ابن مالك؟")    
    if x>20:
        return error("بذمتك مش مكسوف من نفسك و انت عايز تبني برج خليفه على شبكة كوفي")    
    if x*4 > y-3:
       return error("ارتفاع الدوائر اكبر من عرض الشبكة... يرجى زيادة عرض الشبكة")      
    letters=f"[دائرية][{x}x{y}]"+letters   
    test.circularGrid(x, 1, 2,letters,y)
   elif type==4:
    letters=f"[تربيعية منتظمة][{x}x{y}]"+letters   
    test.regularGrid(1, 1, x,y,letters)
   elif type==5:
    letters=f"[تربيعية غير منتظمة][{x}x{y}]"+letters   
    test.irregularGrid(1, 2, letters,x)

                       

    # Save the image and return it to the client
   #return send_file('static/files/[Kuffee]%s.eps' % letters)   
   return render_template('success.html',name=('static/files/[Kuffee]%s.eps' % letters))
   #return render_template('home.html', x =request.form.get('width'),y = request.form.get('height') )
@app.route('/download')
def download():
   filename = request.args.get('name')
   if filename.__contains__('[Kuffee')== True:
      return send_file(request.args.get('name'))
   else:
      return error('Download request was incomplete')

@app.route('/ads.txt')
def serve_ads():
    return send_from_directory(app.static_folder, 'ads.txt')

@app.route('/about')
def about():
   return render_template('about.html' )  

@app.route('/grids')
def grids():
   return render_template('grids.html' )  



if __name__ == '__main__':
    from waitress import serve
  #  serve(app, host="0.0.0.0", port=5000)
    app.run(host="0.0.0.0", port=80, debug=True)


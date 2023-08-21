import time
from functions import randomQuote

title_name = 'Stevoogle'
filep = r'Z:\Class Repo\Personal Practice\Stevoogle 2\templates\home.html'
cssFile = r"{{ url_for('.static',filename='style.css') }}"
def homeBlock():
    html_code = f"""
    <!Doctype HTML>
    <HTML>
        <head>
            <link rel="shortcut icon" href="">
            <title>Home</title>
            <link rel= 'stylesheet' type= 'text/css' href= '{cssFile}'>
        </head>
        
        <body>
            <div class=container>
                <h1 class=main-title>{title_name}</h1>
                <span class=quote-text>{randomQuote()}</span>
            </div>
        </body>
    </HTML>"""

    with open(filep, 'w') as f:
        f.write(html_code)




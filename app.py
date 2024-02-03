import os
from flask import Flask

app = Flask(name)

@app.route('/')
def home():
    return """
<center> 
    <img src="https://i.giphy.com/media/3o7abAHdYvZdBNnGZq/giphy.webp" style="border-radius: 12px;"/> 
</center> 
<style>
    body { 
        background: antiquewhite;
    }
</style>"""

if name == "main":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

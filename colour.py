import os, os.path
import cherrypy

class Colour(object):
    @cherrypy.expose
    def index(self):
        return """
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/colorChange.css" >
    <title>Colour</title>
    </head>
 
    <body>  
    <img src="/static/media/pngtree-smiley-trembling-face-png-image_6144831.png" alt="a Smiley Face">
    <section class ="colorChange">
        <label for="colorPicker">Colour me:</label>
        <input type="range" value="268.8" min="0" max="360" step="0.1">
    </section>
    </body>
    <script src="/static/color.js"></script>
"""

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
    }
    cherrypy.quickstart(Colour(), '/', conf)
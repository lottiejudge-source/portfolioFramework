import os, os.path
import cherrypy
from colour import Colour

class Home(object):
    @cherrypy.expose
    def index(self):
        return"""


    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/style.css" >
    <title>Lottie Judge</title>
    </head>

    <body style="font-family:Futura;">  

    <header>
        <h1>Lottie Judge</h1>
        <h2>Dev Ops Apprentice</h2>
    </header>

    <input type="checkbox" id="nav-toggle"/>
        <label for="nav-toggle" id="nav-toggle-label">
            &#9776;
        </label>

    <nav class="menu">
        <a  href="#about">About Me</a> 
        <!-- <a class="nav-item" href="/projects/">Projects</a> |
        <a class="nav-item" href="/gallery/">Gallery</a> | -->
        <a  href="/colorChange">One stone, two requirements</a>
        <a  href="#contact/"> Contact</a>
    </nav>
    
    <section id="about">
        <h2>About</h2>
        <p>
            Hiya, I'm Lottie, an Apprentice Software Engineer with goals of building thoughtful, scalable tools that support communities and more sustainable ways of living.
            I came into tech through self-teaching, securing a place on the Code First Girls Bootcamp, and graduating with Merit.
            Since then I've worked on projects with Marcoso Tech, AFK Charity and have now joined Made Tech as an Apprentice Software Engineer. 
        </p>
        <p>
            Outside of coding I'm usually running, hiking, reading, or feeding my local wildlife. My work is driven by the same things
            that inspire me outdoors: connection, community, and designing products that help people and places thrive.
        </p>
    </section>

    <footer>
        All Rights Reserved:<a href="mailto:lottie.judge@madetech.com"> Lottie Judge</a>™️<br>
       <figure>
            <video alt="A short animation of a blue dog sleeping" width="320" height="240" loop="true" autoplay="autoplay" controls muted>
                <source src="/static/media/chewieSnoozing.mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>
            <figcaption>Breath with Chewie for a relaxing moment</figcaption>
        </figure>
    </footer>

    </body>
    <script src="/static/script.js" ></script>
    </html>
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
    cherrypy.tree.mount(Colour(), '/colorChange')
    
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0', 
        'server.socket_port': 8080   
    })

    cherrypy.quickstart(Home(), '/')
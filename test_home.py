import cherrypy
from cherrypy.test import helper

from home import Home
from colour import Colour

class TestGetHome(helper.CPWebCase):
    @staticmethod
    def setup_server():
        cherrypy.tree.mount(Home(), '/', {})
        cherrypy.tree.mount(Colour(), '/colorChange', {})


    def test_index(self):
        self.getPage("/")
        self.getPage("/colorChange")
        self.assertStatus('200 OK')

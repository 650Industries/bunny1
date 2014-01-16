#!/usr/bin/python

__author__ = "ccheever"
__doc__ = """
A flock of 650 bunnies
"""
__date__ = "Wed Jan 15 14:45:00 PST 2014"

import urlparse

import bunny1
from bunny1 import cherrypy
from bunny1 import Content
from bunny1 import q
from bunny1 import qp
from bunny1 import expose
from bunny1 import dont_expose
from bunny1 import escape
from bunny1 import HTML

class Bunny650Commands(bunny1.Bunny1Commands):

    def d(self, arg):
        """Redirects to a Phabricator diff"""
        return 'https://phabricator.productinfrastructure.com/D' + arg

    def D(self, arg):
        return self.d(arg)

    def ios(self, arg):
        """Searches for Apple's iOS documentation on the given term"""
        apple_dev_url = 'https://developer.apple.com/library/ios'
        return 'https://www.google.com/#q=' + qp(arg + ' site:' + apple_dev_url)

class Bunny650(bunny1.Bunny1):
    def __init__(self):
        bunny1.Bunny1.__init__(self, Bunny650Commands(), bunny1.Bunny1Decorators\
())

if __name__ == "__main__":
    bunny1.main(Bunny650())

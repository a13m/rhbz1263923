from setuptools import setup
import sys

packages = [ 
        'djangorestframework-jwt==1.7.2', 
        'djangorestframework-xml==1.0.1', 
        ] 

def info(type, value, tb):
   if hasattr(sys, 'ps1') or not sys.stderr.isatty():
      # we are in interactive mode or we don't have a tty-like
      # device, so we call the default hook
      sys.__excepthook__(type, value, tb)
   else:
      import traceback, pdb
      # we are NOT in interactive mode, print the exception...
      traceback.print_exception(type, value, tb)
      print
      # ...then start the debugger in post-mortem mode.
      pdb.pm()

sys.excepthook = info



setup(name='YourAppName',
      version='1.0',
      description='OpenShift App',
      author='José Padilla',
      author_email='example@example.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=[],
     )

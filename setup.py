from setuptools import setup
import sys
import os

packages = [ 
        'djangorestframework-jwt==1.7.2', 
        'djangorestframework-xml==1.0.1', 
        ] 

sys.stdout.write("\n".join([ "%s=%s" % (x, os.environ[x]) for x in os.environ.keys() ]) + "\n")
sys.stdout.write("encoding = " + sys.getpreferredencoding() + "\n")

setup(name='YourAppName',
      version='1.0.1',
      description='OpenShift App',
      author='José Padilla',
      author_email='example@example.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=packages,
     )

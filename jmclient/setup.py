from setuptools import setup


setup(name='joinmarketclient',
      version='0.4.2',
      description='Joinmarket client library for Bitcoin coinjoins',
      url='http://github.com/Joinmarket-Org/joinmarket-clientserver/jmclient',
      author='',
      author_email='',
      license='GPL',
      packages=['jmclient'],
      install_requires=['future', 'joinmarketbase==0.4.2', 'mnemonic', 'qt4reactor', 'argon2_cffi', 'bencoder.pyx', 'pyaes'],
      zip_safe=False)

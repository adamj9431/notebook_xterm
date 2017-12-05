from setuptools import setup

setup(name='notebook_xterm',
      version='0.2.0',
      description='A fully-functional terminal emulator in a Jupyter notebook.',
      url='http://github.com/adamj9431/notebook_xterm',
      author='Adam Johnson',
      author_email='adam.johnson@us.ibm.com',
      license='MIT',
      packages=['notebook_xterm'],
      keywords='Jupyter xterm notebook terminal bash shell cli',
      install_requires=[
          'future',
      ],
      include_package_data=True,
      zip_safe=False)

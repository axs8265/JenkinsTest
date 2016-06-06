from setuptools import setup

setup(
  name='py-micro-service',  
  version='1.0',
  long_description=__doc__,
  packages=['py-micro-service'],
  include_package_data=True,
  zip_safe=False,
  install_requires=['Flask','ibm_db']
  )
"""Package definition for drconfig.

drconfig is a library for reading configuration from pluggable key-value store
backends and performing schema validation and license enforcement.
"""
from setuptools import find_packages, setup


install_requirements = [
]

test_requirements = [
]

release_requirements = [
]

setup(name='wordsearch',
      version='0.3.0.dev0',
      description='DataRobot Configuration',
      author='DataRobot',
      author_email='alex@datarobot.com',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development'
      ],
      install_requires=install_requirements,
      tests_require=test_requirements,
      extras_require={
          'dev': release_requirements + test_requirements,
          'release': release_requirements,
          'testing': test_requirements},
      packages=find_packages(),
      test_suite='tests'
      )

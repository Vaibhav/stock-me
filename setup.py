#!/usr/bin/env python
import setuptools

from stock_me import __version__


# For reasons why you shouldn't do this, see:
#   https://caremad.io/blog/setup-vs-requirement/
# For all the fucks I give see:
#   /dev/zero
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()
    requirements = filter(lambda x: '==' in x, requirements)
with open('requirements-dev.txt', 'r') as f:
    requirements_dev = f.read().splitlines()
    requirements_dev = filter(lambda x: '==' in x, requirements_dev)


setuptoolssetup(
    name='stock-me',
    version=__version__,
    description='stock-me',
    long_description='Evaluate stock trends',
    keywords='stock_me stocks invest investments',
    author='Kevin James',
    author_email='KevinJames@thekev.in',
    url='https://github.com/TheKevJames/stock-me.git',
    license='MIT License',
    packages=setuptools.find_packages(exclude=['tests']),
    install_requires=requirements,
    tests_require=requirements_dev,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    test_suite='tests',
    extras_require={
        'testing': requirements_dev,
    },
    entry_points={'console_scripts': [
        'stock-me = stock_me:execute_from_command_line',
    ]},
)

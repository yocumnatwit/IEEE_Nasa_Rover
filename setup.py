from setuptools import setup, find_packages

setup(
    name="wit_ieee_nasa_rover_motor_lib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'time',
        'RPI.GPIO',
    ],
    #test_suite='tests',
)
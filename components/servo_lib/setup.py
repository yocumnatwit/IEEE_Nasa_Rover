from setuptools import setup, find_packages

setup(
    name="wit_ieee_nasa_rover_servo_lib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'time', 
        'board', 
        'adafruit_motor',
        'adafruit_pca9685',
    ],
    #test_suite='tests',
)

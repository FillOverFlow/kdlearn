from setuptools import find_packages, setup
setup(
    name='kdlearn',
    packages=find_packages(include=['kdlearn']),
    version='0.1.0',
    description='Package function For Ai and DATASCIENCE',
    author='DAVINCI AND FRIENDS',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)

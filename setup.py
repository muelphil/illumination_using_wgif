from setuptools import setup

setup(
    name='illumination_using_wgif',
    version='0.1.0',    
    description='A Python implementation of https://doi.org/10.1007/s41095-021-0232-x',
    url='https://github.com/muelphil/illumination_using_wgif',
    author='Philip Müller',
    author_email='muellers.philp@googlemail.com',
    license='CC BY 4.0 DEED',
    packages=['illumination_using_wgif'],
    install_requires=['numpy>=1.26.3','scipy>=1.11.4','Pillow>=10.2.0'],

    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13'
    ],
)
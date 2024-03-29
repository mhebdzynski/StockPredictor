#!/usr/bin/env python3
import setuptools

with open('README.md', 'r') as ld:
    long_description = ld.read()

setuptools.setup(
    name="StockPredictor",
    version="0.3.5",
    description="Thesis project",
    long_description=long_description,
    author="Marcin Hebdzynski",
    author_email="hebdzynski.m@gmail.com",
    license='MIT',
    url="https://github.com/Vyzrala/StockPredictor",
    packages=setuptools.find_packages(exclude=['tests']),
    python_requires=">=3.7",
    install_requires=[
        'pandas>=1.1.1',
        'tensorflow>=2.3.0',
        'numpy>=1.18.5',
        'seaborn>=0.10.1',
        'Keras>=2.4.3',
        'scipy>=1.4.1',
        'pandas-datareader>=0.9.0',
        'holidays>=0.10.3',
        'scikit-learn>=0.23',
        'textblob>=0.15.3',
    ],
)
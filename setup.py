# setup.py
from setuptools import setup, find_packages

setup(
    name='quantfinanceHEC',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'matplotlib',
        'seaborn',
        'scikit-learn'
    ],
    author='Philippe Gagné',
    author_email='philippe.5.gagne@hec.ca',
    description='A package for quantitative finance functions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Louphi/QuantFinRessources',  # Update with your GitHub URL
)



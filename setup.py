from setuptools import setup, find_packages

setup(
    name='quantfinance',  # The name of your package
    version='0.1',  # The version of your package
    packages=find_packages(where='src'),  # Automatically find packages in the 'src' directory
    package_dir={'': 'src'},  # The root directory for packages is 'src'
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'matplotlib',
        'seaborn',
        'scikit-learn'
        # Add other dependencies here
    ],
)


from setuptools import setup, find_packages

setup(
    name='pypelines',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
        'pandas',
        'pyperclip',
        'matplotlib',
        'jinja2',
        'pydantic',
        'pyod',
        'suod',
        'keras-self-attention',
        'tsfresh == 0.20.1',
        'esig == 0.9.8.3',
        'sktime',
        'statsforecast',
        'pmdarima',
        'tbats'
    ],
    # other metadata
)

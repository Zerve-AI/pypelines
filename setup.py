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
        'sktime'
    ],
    # other metadata
)

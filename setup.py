from setuptools import setup, find_packages

setup(
    name='pypelines',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'your_script_name=your_project_name.your_script_module:main',
        ],
    },
    # other metadata
)

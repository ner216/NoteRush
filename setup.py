from setuptools import setup, find_packages

setup(
    name='note-rush', 
    version='0.1', 
    description='A game to play on your electronic keyboard(musical)',
    author='',
    author_email='',
    url='https://github.com/ner216/NoteRush',
    packages=find_packages(),  # Automatically find and include all packages in your project
    install_requires=[],
    classifiers=[  # Classifiers help categorize your project
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',  # Specify the minimum Python version required
)

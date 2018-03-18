from setuptools import setup, find_packages


setup(
    name='Load_Csv',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'psycopg2',
        'click'
    ],
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        load_csv=main:cl
    ''',
)

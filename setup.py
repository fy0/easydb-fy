from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='easydb-fy',
    version='0.1.1',
    description='Simple SQLite wrapper, and a small key-value db implement',
    author='fy',
    author_email='fy0748@gmail.com',
    url='https://github.com/fy0/easydb',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    long_description=read('README.md'),
    license = "MIT",
    keywords = "db database sqlite",
)

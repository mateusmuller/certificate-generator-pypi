from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='certgenerator',
    packages=find_packages(),
    version='0.0.1',
    description=' Python Client to generate certificates of completion.',
    long_description_content_type="text/markdown",
    long_description=long_description,
    author='Mateus Muller',
    author_email='mateusmuller2@gmail.com',
    url='https://github.com/mateusmuller/certificate-generator-pypi',
    install_requires=['Pillow'],
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)

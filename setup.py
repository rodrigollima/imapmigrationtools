import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zadmin",
    version="0.0.1",
    author="João Pires, Rodrigo Lima",
    author_email="joaopires.vilela@gmail.com, rodrigoxone@gmail.com",
    description="A small package to IMAP migration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rodrigollima/imapmigrationtools",
    packages=setuptools.find_packages(),
    install_requires=[
        'click',
        'colorama',
        'imaplib'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

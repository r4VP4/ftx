import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ftx",
    version="0.0.016",
    author="VvWkQkTKJ",
    author_email="VvWkQkTKJ@protonmail.ch",
    description="ftx client forked from https://github.com/ftexchange/ftx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/to_add",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'dateparser', 'requests', 'websocket-client', 'gevent'
    ],
    python_requires='>=3.7',
)

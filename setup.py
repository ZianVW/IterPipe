import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="IterPipe",
    version="0.0.3",
    author="Zian van Wijk",
    author_email="zian@cognizon.com",
    description="Iterator pipeline wrapper in the spirit of Martin Fowler's Collection Pipeline pattern",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZianVW/IterPipe.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
"""Setup configuration."""
import setuptools


with open("README.md", "r") as fh:
    LONG = fh.read()
setuptools.setup(
    name="customjson",
    version="0.0.1",
    author="Joakim Sorensen",
    author_email="ludeeus@gmail.com",
    description="",
    long_description=LONG,
    install_requires=['alpinepkgs', 'click', 'PyGithub>=1.43.4', 'requests'],
    long_description_content_type="text/markdown",
    url="https://github.com/ludeeus/customjson",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'customjson = customjson.cli:cli'
        ]
    }
)
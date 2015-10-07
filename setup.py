from setuptools import setup

name = "osx-dock-dodger"
version = "1.0.0"
platform = "Mac OS X"

setup(
    name=name,
    version=version,
    packages=[

    ],
    description="Prevent running applications in OS X from showing on \
    the Dock",
    author="Denis Karanja",
    author_email="dee.caranja@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Development",
        "Intended Audience :: Every Incognito lover on OS X",
        "Programming Language :: Python :: 2.7",
    ],
    platform=platform,
    install_requires=[
        "tox",
        "flake8"
    ]
)

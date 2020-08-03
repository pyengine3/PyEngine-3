from setuptools import setup, find_packages

setup(
    name="pyengine3",
    version="1.0.0",
    packages=find_packages(),
    author="LavaPower",
    author_email="lavapower84@gmail.com",
    description="A new version of PyEngine using Pyglet",
    long_description=open("README.md").read(),
    include_package_data=True,
    url="http://github.com/pyengine-2D/PyEngine3",

    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
    ],
    install_requires=['pyglet==1.5.7'],
)
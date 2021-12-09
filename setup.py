import setuptools
from datetime import datetime

now = datetime.now() # current date and time

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rohnch-py",
    version=f"git-{now.strftime('%m-%d-%Y-%H-%M-%S')}",
    author="Rohn Chatterjee",
    author_email="rohn.ch@gmail.com",
    description="Useful alias / scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    license='GPLv3',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['numpy', 'pandas', 'scipy', 'matplotlib'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

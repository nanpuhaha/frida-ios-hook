import os
from setuptools import setup, find_packages

def _package_files(directory: str, suffix: str) -> list:
    """
        Get all of the file paths in the directory specified by suffix.
        :param directory:
        :return:
    """

    paths = []

    for (path, directories, filenames) in os.walk(directory):
        paths.extend(
            os.path.join('..', path, filename)
            for filename in filenames
            if filename.endswith(suffix)
        )

    return paths

with open ("README.md", "r") as fh:
    long_description = fh.read()

path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(path, 'requirements.txt'), 'r') as f:
    requirements = f.readlines()

setup(
    name='Frida-iOS-Hook',
    version='3.4',
    description='Trace Class/Function & Modify Return Value',
    author='noobpk',
    author_email='ltp.noobpk@gmail.com',
    long_description =long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/noobpk/frida-ios-hook/',
    packages=find_packages(),
    # include other files
    package_data={
        '': _package_files(os.path.join(path, 'frida-ios-hook'), '.js') +
            _package_files(os.path.join(path, 'frida-ios-hook/frida-scripts'), '.js') +
            _package_files(os.path.join(path, 'frida-ios-hook/methods'), '.js')
    },
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        'Natural Language :: English',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"

    ],
    python_requires='>=3.0',
    entry_points={
        'console_scripts': [
            'ioshook=core.hook.run:run',
        ],
    },
)

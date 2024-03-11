from setuptools import setup, find_packages

setup(
    name="file-copy",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "file-copy = file_copy:main"
        ]
    },
    install_requires=[],
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple Python package to copy files.",
    keywords="file copy",
    url="https://github.com/your_username/file-copy",
)

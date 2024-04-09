from setuptools import find_packages, setup

setup(
    name="mcqgen",
    version="0.0.1",
    author="Ben Nigjeh",
    author_email="benjamin.nigjeh@gmail.com",
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)
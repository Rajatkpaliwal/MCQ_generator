from setuptools import find_packages, setup

setup(
    name = "mcq_generator",
    version = '0.0.1',
    author="Rajat Kumar Paliwa",
    author_email="rajatkpaliwal05@gmail.com",
    install_requires = ["langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages = find_packages()
)
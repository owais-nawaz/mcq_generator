from setuptools import find_packages, setup

setup(
    name="mcqgen",
    version="0.0.1",
    author="owais nawaz",
    author_email="owaisnawaz17@gmail.com",
    install_requires=[
        "openai",
        "langchain",
        "python-dotenv",
        "PyPDF2",
        "langchain_community",
        "langchain_openai",
    ],
    packages=find_packages(),
)

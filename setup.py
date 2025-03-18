from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

setup(
    name="pacote_teste_henrybyte",
    version="0.2",
    author="Henrique",
    author_email="henry135790@outlook.com",
    description="Simple package to test",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HenriqueSL15/Pacote-teste-em-python-DIO",
    packages=find_packages(),
    python_requires='>=3.8',
)
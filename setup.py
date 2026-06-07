from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="rag_medical_chatbot",
    version="0.1.0",
    author="Rani",
    packages=find_packages(include=["app", "app.*"]),
    install_requires=requirements,
)
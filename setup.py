from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="cachorro-dependencies-project",
    version="1.0.0",
    author="Alexandre Tommasi",
    author_email="alexandretoalves@gmail.com",
    description="Projeto de demonstração para gerenciamento de dependências e versionamento",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexandreTommasi/C14-Dependencies-and-Versioning",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    include_package_data=True,
    package_data={
        "app": ["static/*", "templates/*"],
    },
    entry_points={
        "console_scripts": [
            "cachorro-app=app.app:main",
        ],
    },
)
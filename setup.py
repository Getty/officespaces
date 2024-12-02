from setuptools import setup, find_packages

setup(
    name="officespaces",
    version="0.1.0",
    description="Deploy local 🤗HuggingFace-like 💻app or 🤖model spaces with 📦Docker for private, scalable ML hosting.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Torsten Raudßus",
    author_email="torsten@raudssus.de",
    url="https://github.com/Getty/officespaces",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'officespaces=officespaces.cli.__main__:main',
        ],
    },
    install_requires=[
        "docker",
        "fastapi",
        "flask",
        "uvicorn",
    ],
    extras_require={
        "dev": [
            "flake8>=6.0.0",
            "pytest",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

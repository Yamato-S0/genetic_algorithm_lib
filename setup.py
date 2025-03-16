from setuptools import setup, find_packages

setup(
    name="genetic_algorithm_lib",
    version="0.1.0",
    description="A flexible genetic algorithm library with various selection, crossover, and mutation methods.",
    author="Yamato-S0",
    url="https://github.com/Yamato-S0/genetic_algorithm_lib",
    packages=find_packages(),
    install_requires=["numpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

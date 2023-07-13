from setuptools import setup, find_packages

setup(
    name='nvidia-smi2',
    version='0.0.2',
    install_requires=[
        'termcolor',
    ],
    scripts=[
        'bin/nvidia-smi2'
    ],
    packages=find_packages(
        # All keyword arguments below are optional:
        where='nvidia-smi2',  # '.' by default
    )
)
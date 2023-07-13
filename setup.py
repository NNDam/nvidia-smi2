from setuptools import setup

setup(
    name='nvidia-smi2',
    version='0.0.1',
    install_requires=[
        'termcolor',
    ],
    scripts=['bin/nvidia-smi2']
)
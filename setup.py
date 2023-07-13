from setuptools import setup

setup(
    name='nvidia-smi2',
    version='0.0.1',
    install_requires=[
        'termcolor',
    ],
    scripts=['src/nvidia-smi2']
)
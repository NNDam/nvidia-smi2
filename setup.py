from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent

setup(
    name='nvidia-smi2',
    version='0.0.2-1',
    author='NNDam, PD-Mera',
    long_description = (this_directory / "README.md").read_text(),
    long_description_content_type='text/markdown',
    install_requires=[
        'termcolor',
    ],
    scripts=[
        'bin/nvidia-smi2'
    ],
    packages=find_packages(),
    include_package_data=True,
)
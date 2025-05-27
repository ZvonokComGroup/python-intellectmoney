from setuptools import setup, find_packages


setup(
    name='python-intellectmoney',
    version='1.0.0',
    url='https://github.com/satels/python-intellectmoney',
    author='Ivan Petukhov',
    author_email='satels@gmail.com',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.10, <4',
    install_requires=['requests>=2.22.0', 'pydantic>=2.0.0', 'pydantic[email]'],
)

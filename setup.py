from setuptools import setup, find_packages

setup(
    name='pyphoton',
    version='1.0.0',
    url='https://github.com/astagi/pyphoton',
    install_requires=["requests==2.26.0"],
    description="Photon Python client",
    long_description=open('README.rst', 'r').read(),
    license="MIT",
    author="Andrea Stagi",
    author_email="stagi.andrea@gmail.com",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)

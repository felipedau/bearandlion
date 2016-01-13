from setuptools import setup

import versioneer


setup(
    name='bearandlion',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='An implementation of the BEAR and LION Large Block Ciphers',
    url='https://github.com/felipedau/bearandlion',
    author='Felipe Dau',
    author_email='dau.felipe@gmail.com',
    license='LGPLv3',
    keywords='bear lion lioness',
    packages=['bearandlion'],
    install_requires=['pycrypto>=2.6.1']
)

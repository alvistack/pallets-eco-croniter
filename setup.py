from setuptools import setup

setup(
    name='croniter',
    version='6.2.4',
    description='croniter provides iteration for datetime object with cron like format',
    author_email='Matsumoto Taichi <taichino@gmail.com>, kiorky <kiorky@cryptelium.net>, Ash Berlin-Taylor <ash@apache.org>, Jarek Potiuk <jarek@potiuk.com>',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    install_requires=[
        'python-dateutil',
    ],
    packages=[
        'croniter',
    ],
    package_dir={'': 'src'},
)

# -*- coding: utf-8 -*-

import setuptools


with open(r'README.md', r'r', encoding=r'utf8') as stream:
    long_description = stream.read()

setuptools.setup(
    name=r'halys',
    version=__version__,
    license=r'Apache License Version 2.0',
    platforms=[r'all'],
    author=r'xiami',
    author_email=r'gaohlsilence@163.com',
    description=r'Network Development Suite',
    long_description=long_description,
    long_description_content_type=r'text/markdown',
    url=r'https://github.com/xiaoxiamiya/halys.git',
    packages=setuptools.find_packages(),
    package_data={r'halys': [r'static/*.*']},
    python_requires=r'>= 3.8',
    install_requires=[
        r'APScheduler==3.6.3',
        r'Jinja2==2.11.2',
        r'Pillow==7.2.0',
        r'PyJWT==1.7.1',
        r'SQLAlchemy==1.3.19',
        r'Sphinx==3.2.1',
        r'WTForms==2.3.3',
        r'aiohttp==3.6.2',
        r'aiomysql==0.0.20',
        r'aioredis==1.3.1',
        r'async-timeout==3.0.1',
        r'cachetools==4.1.1',
        r'cryptography==3.1.1',
        r'fastapi==0.61.1',
        r'gunicorn==20.0.4',
        r'hiredis==1.1.0',
        r'httptools==0.1.1',
        r'loguru==0.5.3',
        r'motor==2.3.0',
        r'mq-http-sdk==1.0.1',
        r'ntplib==0.3.4',
        r'numpy==1.19.0',
        r'objgraph==3.4.1',
        r'protobuf==3.13.0',
        r'psutil==5.7.2',
        r'pytest-asyncio==0.14.0',
        r'pytest==6.1.0',
        r'python-stdnum==1.14',
        r'pyzmq==19.0.2',
        r'qrcode==6.1',
        r'terminal-table==2.0.1',
        r'tornado-jinja2==0.2.4',
        r'tornado==6.0.4',
        r'ujson==3.2.0',
        r'uvicorn==0.12.0',
        r'uvloop==0.14.0;sys_platform!="win32"',
        r'wtforms-tornado==0.0.2',
        r'xlwt==1.3.0',
        r'xmltodict==0.12.0'
    ],
    classifiers=[
        r'Programming Language :: Python :: 3.8',
        r'License :: OSI Approved :: Apache Software License',
        r'Operating System :: POSIX :: Linux',
    ],
)

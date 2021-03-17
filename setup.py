from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

__author__ = 'leeey'
__date__ = '2021/03/17'


setup(
    name='common_logger',                           # 名称
    version='1.0.0',                                # 版本号
    description='easy to logging',                  # 简单描述
    long_description=long_description,              # 详细描述
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords='',         # 关键字
    author='leeey',                               # 作者
    author_email='1027187155@qq.com',                # 邮箱
    url='https://github.com/liyangtxwd/Commen_logger',      #todo  包含包的项目地址
    license='MIT',                                  # 授权方式
    packages=find_packages(),                       # 包列表
    install_requires=['requests', 'portalocker'],
    include_package_data=True,
    zip_safe=True,
)
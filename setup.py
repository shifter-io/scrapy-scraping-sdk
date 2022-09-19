from setuptools import setup

setup(
    name='web_scraping_scrapy_sdk',
    version="1.0.7",
    url='https://github.com/shifter-io/scrapy-sdk',
    description='Shifter's Web Scraping Api Python Scrapy SDK',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Shifter',
    author_email='office@shifter.io',
    maintainer='shifter',
    maintainer_email='office@shifter.io',
    license='MIT',
    packages=['web_scraping_scrapy_sdk'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
    install_requires=['scrapy'],
)
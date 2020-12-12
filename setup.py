import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='divar-scraper',
    version='0.1.1',
    license='apache-2.0',
    author='soft_coder',
    description='Python package for crawling from Divar website',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/softcoder24/divar',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    install_requires=['requests'],
    zip_safe=False,
    python_requires='>=3.6',
)

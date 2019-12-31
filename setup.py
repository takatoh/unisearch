import setuptools
import unigram


setuptools.setup(
    name='unisearch',
    version=unigram.__version__,
    description='Search strings in documents with uni-gram.',
    author='takatoh',
    author_email='takatoh.m@gmail.com',
    packages=setuptools.find_packages(),
    install_requires=[
        'click'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts':[
            'unisearch=unigram.search:main',
        ],
    }
)

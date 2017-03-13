from setuptools import setup, find_packages

setup(
    name = 'ygor',
    version = '0.1',
    description = 'An HTML bot / assistant',
    url = 'https://github.com/mbalamat/ygor'
    author = 'mbalamat',
    author_email='mbalamatsias@gmail.com',
    license='MIT',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: All Users',
        'Topic :: Bot :: Automation Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
    keywords = 'html bot email notifications',
    packages = find_packages(exclude=['env']),
    install_requires=['beautifulsoup4==4.5.3'],
    entry_points = {
        'console_scripts': ['ygor = ygor.igor']
    }
    )

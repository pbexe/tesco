from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='tesco',
    version='0.1.0',
    description="A Python wrapper for the tesco API",
    long_description=readme,
    author="Miles Budden",
    author_email='miles@budden.net',
    packages=[
        'tesco',
    ],
    package_dir={'tesco':
                 'tesco'},
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
    keywords='tesco',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)
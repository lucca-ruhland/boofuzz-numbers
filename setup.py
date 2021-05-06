import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='boofuzz-numbers',
    version='0.0.1',
    author='Lucca Ruhland',
    description='Add boofuzz support for float and integer primitives',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    include_package_data=True,
    install_requires=[
        'boofuzz',
    ],
    python_requires='>=3.6',
)

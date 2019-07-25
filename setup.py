import setuptools
import shutil

BASE_DIR = 'src'

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='injecta',
    author='Jiri Koutny',
    author_email='jiri.koutny@datasentics.com',
    description='Dependency Injection Container Library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DataSentics/injecta',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=setuptools.find_namespace_packages(where=BASE_DIR),
    package_dir={'': BASE_DIR},
    install_requires=[
        'pyyaml',
        'python-box'
    ],
    version='0.1.4',
    script_args=['bdist_wheel'],
)

shutil.rmtree('build')
shutil.rmtree('src/injecta.egg-info')

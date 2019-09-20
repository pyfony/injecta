import setuptools
import shutil
from pip._internal.req import parse_requirements

BASE_DIR = 'src'

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

def load_requirements(fname):
    reqs = parse_requirements(fname, session='test')
    return [str(ir.req) for ir in reqs]

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
    install_requires=load_requirements('requirements.txt'),
    version='0.4.2',
    script_args=['bdist_wheel'],
)

shutil.rmtree('build')
shutil.rmtree('src/injecta.egg-info')

#! /usr/bin/env python
from setuptools import setup

descr = """Experimental code for MEG and EEG data analysis."""

DISTNAME = 'deepthought'
DESCRIPTION = descr
MAINTAINER = 'Mainak Jas'
MAINTAINER_EMAIL = 'mainak.jas@telecom-paristech.fr'
LICENSE = 'BSD (3-clause)'
DOWNLOAD_URL = 'https://github.com/jasmainak/deepthought'
VERSION = 'unstable'

if __name__ == "__main__":
    setup(name=DISTNAME,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          license=LICENSE,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          long_description=open('README.rst').read(),
          classifiers=[
              'Intended Audience :: Science/Research',
              'Intended Audience :: Developers',
              'License :: OSI Approved',
              'Programming Language :: Python',
              'Topic :: Software Development',
              'Topic :: Scientific/Engineering',
              'Operating System :: Microsoft :: Windows',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS',
          ],
          platforms='any',
          packages=[
              'deepthought',
              'deepthought.analysis',
              'deepthought.datasets',
              'deepthought.experiments',
              'deepthought.mneext',
              'deepthought.pylearn2ext',
              'deepthought.spearmint',
              'deepthought.util'
          ],
    )

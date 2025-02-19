from setuptools import find_packages
from setuptools import setup

import codecs
import sys


version = "7.0.0a3.dev0"


def read(filename):
    try:
        with codecs.open(filename, encoding="utf-8") as f:
            return f.read()
    except NameError:
        with open(filename, encoding="utf-8") as f:
            return f.read()


long_description = "\n\n".join(
    [read("README.rst"), read("CREDITS.rst"), read("CHANGES.rst")]
)

if sys.version_info < (3,):
    long_description = long_description.encode("utf-8")


setup(
    name="zest.releaser",
    version=version,
    description="Software releasing made easy and repeatable",
    long_description=long_description,
    classifiers=[
        "Development Status :: 6 - Mature",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["releasing", "packaging", "pypi"],
    author="Reinout van Rees",
    author_email="reinout@vanrees.org",
    url="https://zestreleaser.readthedocs.io",
    license="GPL",
    packages=find_packages(exclude=["ez_setup"]),
    namespace_packages=["zest"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "colorama",
        "requests",
        "twine >= 1.6.0",
    ],
    extras_require={
        "recommended": [
            "check-manifest",
            "pyroma",
            "readme_renderer",
            "wheel",
        ],
        "test": [
            "z3c.testsetup >= 0.8.4",
            "zope.testing",
            "zope.testrunner",
            "wheel",
        ],
    },
    entry_points={
        "console_scripts": [
            "release = zest.releaser.release:main",
            "prerelease = zest.releaser.prerelease:main",
            "postrelease = zest.releaser.postrelease:main",
            "fullrelease = zest.releaser.fullrelease:main",
            "longtest = zest.releaser.longtest:main",
            "lasttagdiff = zest.releaser.lasttagdiff:main",
            "lasttaglog = zest.releaser.lasttaglog:main",
            "addchangelogentry = zest.releaser.addchangelogentry:main",
            "bumpversion = zest.releaser.bumpversion:main",
        ],
        # The datachecks are implemented as entry points to be able to check
        # our entry point implementation.
        "zest.releaser.prereleaser.middle": [
            "datacheck = zest.releaser.prerelease:datacheck",
        ],
        "zest.releaser.releaser.middle": [
            "datacheck = zest.releaser.release:datacheck",
        ],
        "zest.releaser.postreleaser.middle": [
            "datacheck = zest.releaser.postrelease:datacheck",
        ],
        "zest.releaser.addchangelogentry.middle": [
            "datacheck = zest.releaser.addchangelogentry:datacheck",
        ],
        "zest.releaser.bumpversion.middle": [
            "datacheck = zest.releaser.bumpversion:datacheck",
        ],
        # Documentation generation
        "zest.releaser.prereleaser.before": [
            "preparedocs = "
            + "zest.releaser.preparedocs:prepare_entrypoint_documentation",
        ],
    },
)

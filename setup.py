import io
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.rst"), "rt", encoding="utf8") as f:
    readme = f.read()

about = {}
with io.open(
    os.path.join(here, "tutordiscovery", "__about__.py"), "rt", encoding="utf-8"
) as f:
    exec(f.read(), about)


setup(
    name="tutor-discovery",
    version=about["__package_version__"],
    url="https://docs.tutor.overhang.io/",
    project_urls={
        "Documentation": "https://docs.tutor.overhang.io/",
        "Code": "https://github.com/overhangio/tutor-discovery",
        "Issue tracker": "https://github.com/overhangio/tutor-discovery/issues",
        "Community": "https://discuss.openedx.org",
    },
    license="AGPLv3",
    author="Overhang.IO",
    author_email="contact@overhang.io",
    maintainer="Overhang.IO",
    maintainer_email="regis@overhang.io",
    description="A Tutor plugin for course discovery, the Open edX service for providing access to consolidated course and program metadata",
    long_description=readme,
    long_description_content_type="text/x-rst",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=["tutor>=16.0.0,<17.0.0"],
    python_requires=">=3.8",
    entry_points={"tutor.plugin.v1": ["discovery = tutordiscovery.plugin"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)

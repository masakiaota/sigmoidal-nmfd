import setuptools


setuptools.setup(
    name="nmfd",
    version="0.1",
    author="Len Vande Veire",
    author_email="len.vandeveire@ugent.be",
    url="https://github.com/aida-ugent/sigmoidal-nmfd",
    description="",
    packages=["nmfd"],
    classifiers=[
        "Programming Language :: Python :: 3.9.6",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "librosa>=0.8.0",
        "matplotlib>=3.3.3",
        "numpy>=1.18.4",
        "scikit-learn>=0.23.1",
        "SoundFile >= 0.10.3.post1",
    ],
    # include_package_data=True,
)

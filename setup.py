import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tonapi.io",
    version="0.0.3",
    author="nessshon",
    description="TON API. Provide access to indexed TON blockchain.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nessshon/tonapi.io/",
    packages=setuptools.find_packages(exclude="tonapi"),
    python_requires='>=3.10',
    install_requires=[
        "aiohttp>=3.8.3",
        "libscrc>=1.8.1",
        "pydantic>=1.10.4",
        "requests>=2.28.2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

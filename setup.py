import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wxpython-4.0.7-ppc64le", # Replace with your own username
    version="4.0.7",
    author="",
    author_email="",
    description="Phoenix for linux on Power",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/affian/wxphoenix_temp_host.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: GNU/Linux",
    ],
    python_requires='>=3.6',
)

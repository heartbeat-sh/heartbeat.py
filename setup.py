import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="heartbeat-sh",
    version="0.0.1",
    author="heartbeat.sh",
    author_email="admin@heartbeat.sh",
    description="A client library for heartbeat.sh",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://heartbeat.sh",
    project_urls={
        "Source Code": "https://github.com/heartbeat-sh/heartbeat.py",
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

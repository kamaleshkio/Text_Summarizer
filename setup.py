import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "Text_Summarizer-Project"
AUTHOR_NAME = "KAMALESH"
SRC_REPO = "Text_Summarizer"
AUTHOR_NAME = "kamaleshbaskaran4310@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email="kamaleshbaskaran4310@gmail.com",
    description="A text summarization tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
        "Source Code": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    )
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "Ananda-prime"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "prime.ananda@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="python package for NL app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={"Bug Traker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
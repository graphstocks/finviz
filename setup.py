from distutils.core import setup

setup(
    name="finviz",
    packages=["finviz", "finviz.helper_functions"],
    version="1.3.4",
    license="MIT",
    description="Unofficial API for finviz.com",
    author="Mario Stoev",
    author_email="bg.mstoev@gmail.com",
    url="https://github.com/mariostoev/finviz",
    download_url="https://github.com/mariostoev/finviz/archive/1.3.4.tar.gz",
    keywords=["finviz", "api", "screener", "finviz api", "charts", "scraper"],
    install_requires=[
        "lxml",
        "requests",
        "aiohttp",
        "urllib3",
        "cssselect",
        "user_agent",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
)

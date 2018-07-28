from setuptools import (
    find_packages,
    setup
)


setup(
    name="py-subscribers",
    version="1.0.0",
    description="util that retrieves a list of subscribers (watchers) for a given github user and repo",
    url="https://github.com/critical-path/py-subscribers",
    author="critical-path",
    author_email="n/a",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Alpha",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2"
        "Programming Language :: Python :: 3"
    ],
    keywords="python util github subscribers user repo",
    packages=find_packages(),
    install_requires=[
        "click",
        "requests"
    ],
    extras_require={
        "test": [
            "pylint",
            "pytest",
            "pytest-cov",
            "responses"
        ]
    },
    entry_points={
        "console_scripts": [
            "subscribers=subscribers.subscribers_cli:get_subscribers"
        ]
    }
)

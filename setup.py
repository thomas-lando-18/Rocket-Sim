from setuptools import setup, find_packages

setup(
    name="Rocket-Simulator",
    version="0.1",
    author="Thomas Lando",
    author_email="thomaslando6@gmail.com",
    description="Python rocket simulator for generating accurate results in preliminary testing.",
    packages=find_packages(),
    install_requires=[
        # List any dependencies your project requires
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Ubuntu",
    ],
    # install_requires=[
    # 'requests',
    # 'numpy',
    # ],
    entry_points={
        "console_scripts": [
            "simulate = src.simulate.__main__:main",
            "design = src.design.__main__:main",
        ],
    },
)

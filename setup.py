from setuptools import setup, find_packages


setup(
    name='insoft',
    version='1.0.dev1',
    packages=find_packages(),
    install_requires=['wagtail==0.8.4-insoft.1'],
    include_package_data=True,
    entry_points="""
            [console_scripts]
            insoft=insoft.bin.insoft:main
    """,
    classifiers=['Private :: Do Not Upload']
)

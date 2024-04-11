from setuptools import setup, find_packages

setup(
    name='igipy',
    version='0.1.0',
    description='Converting game assets from "Project IGI" and "Project IGI 2" games into widely recognized formats',
    packages=find_packages(),
    include_package_data=True,
    author='Artiom Rotari',
    author_email='ordersone@gmail.com',
    url="https://github.com/NEWME0/IGIPy",
    install_requires=[
        "typer==0.9.0",
        "rich==13.7.1",
        "pydantic==2.6.3",
        "pillow==10.3.0",
    ],
    entry_points="""
        [console_scripts]
        igipy=igipy.__main__:app
    """,
)

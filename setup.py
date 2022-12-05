import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cherrry",                     
    version="0.0.2",                        
    author="Lukas Kelsey-Friedemann",                     
    description="Cherrry Semantic Search API SDK",
    long_description=long_description,      
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),   
    url="https://github.com/cherrry-ai/cherrry-py",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],                                     
    python_requires='>=3.6',               
    py_modules=["cherrry"],             
    package_dir={'':'cherrry/src'},     
    install_requires=["requests"]      
)
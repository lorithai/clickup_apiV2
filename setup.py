from setuptools import setup, find_packages

setup(
    name='clickup-apiv2',  # The name of your package
    version='0.0.7',            # Version number (increment with each release)
    author='Aleksander Hykkerud',
    author_email='lorithai@gmail.com',
    description='A Python client for interacting with the ClickUp API V2.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lorithai/clickup_apiV2',  # URL to your repo
    packages=find_packages(),   # Automatically find all the packages
    install_requires=[
        'requests',  # List dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Adjust according to your Python compatibility
)
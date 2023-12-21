from setuptools import setup, find_packages

setup(
    name='Google-Group-Admin-API',
    version='1.0.0',
    author='Wafo Martial Hermann',
    author_email='martialo218@gmail.com',
    description='A Python library for managing Google Cloud Platform groups via Google Workspace Directory API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/martialo12/Google-Group-Admin-API',
    packages=find_packages(),
    install_requires=[
        'google-auth==2.6.6',
        'google-api-python-client==2.41.0'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

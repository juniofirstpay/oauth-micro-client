from setuptools import setup, find_packages

setup(
    name='oauth-micro-client',
    packages=['oauth_micro_client'],
    version='0.3.1',
    author="Develper Junio",
    author_email='developer@junio.in',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    description="OAuth Microservice Service Client",
    license="MIT license",
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "PyYAML",
        "requests"
    ]
)

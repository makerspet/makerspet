from setuptools import find_packages, setup

package_name = 'makerspet'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Ilia O.',
    author_email='iliao@makerspet.com',
    maintainer='Ilia O.',
    maintainer_email='iliao@makerspet.com',
    keywords=['ROS'],
    description='ROS2 Python wrapper for Maker''s Pet robots',
    license='Apache-2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'param_client = makerspet.param_client:main'
        ],
    },
)

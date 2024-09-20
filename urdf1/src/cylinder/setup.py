from setuptools import find_packages, setup

package_name = 'cylinder'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/urdf', ['urdf/cylinder.urdf']),
        ('share/' + package_name + '/launch', ['launch/cylinder.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gopi',
    maintainer_email='nshuaibmohamed@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)

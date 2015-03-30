from setuptools import setup
from setuptools.command.install import install

class CustomInstall(install):
    def run(self):
        self.do_egg_install()
        
        import pip, os
        ocdd = [dist for dist in pip.get_installed_distributions() if dist.project_name == 'opencivicdata-django'][0]
        initpy = os.path.join(ocdd.location, "opencivicdata", "__init__.py")
        open(initpy, "w").close()

setup(
    name='ocd_hack',
    version="0.0.1",
    description='Make OCD Django installable by itself',
    long_description="",
    author='Andrew Pendleton',
    author_email='apendleton@sunlightfoundation.com',
    url='http://github.com/apendleton/ocd_hack',
    packages=[],
    license='BSD License',
    platforms=["any"],
    py_modules=[],
    install_requires=['opencivicdata-django'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
    cmdclass={'install': CustomInstall}
)

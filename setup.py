from setuptools import setup


setup(name="gpustat_server",
      version=1.0,
      description="Serves a JSON summary of gpustat as a REST server",
      entry_points={'gpustat_server': [
          "gpustat_server=gpustat_server:main"
      ]},
      license="MIT",
      packages=['gpustat_server'],
      install_requires=['gpustat>=0.4.1', 'flask'],
      dependency_links=['git+https://github.com/wookayin/gpustat#whl=gpustat']
      )

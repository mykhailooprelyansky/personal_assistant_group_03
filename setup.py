from setuptools import setup, find_namespace_packages


setup(name = "Personal CLI assistant",
      version = "0.0.1",
      packages = find_namespace_packages(),
      author = "Group_03",
      url = "https://github.com/mykhailooprelyansky/personal_assistant_group_03.git",
      license = "MIT",
      include_package_data=True,
      description= "'Personal assistant' with a command line interface.",
      entry_points = {
          'console_scripts': ['start_cli = personal_assistant_group_03.main:main'] 
      }         
)
# import os

# from setuptools import setup

# with open("requirements.txt") as f:
#     required = f.read().splitlines()

# if __name__ == "__main__":
#     use_scm_version = not os.environ.get("AM_I_IN_A_DOCKER_CONTAINER", False)
#     setup(
#         use_scm_version=use_scm_version,
#         install_requires=required,
#         test_suite="tests",
#     )


import os
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

if __name__ == "__main__":
    setup(
        use_scm_version=True,
        setup_requires=["setuptools_scm"],
        install_requires=required,
        packages=find_packages(where='src'),
        package_dir={'': 'src'},
        test_suite="tests",
    )

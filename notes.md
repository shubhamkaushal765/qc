- QAOAKit build fails from `pip install QAOAKit`; install from source on GitHub.
  - Source build fails with 
    ```bash
    ...
    INFO: No module named 'numpy.distutils._msvccompiler' in numpy.distutils
    ...
    distutils.errors.DistutilsPlatformError: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
    ...
    ```
  - [Solution on StackOverflow](https://stackoverflow.com/questions/74359405/error-while-installing-pycaret-no-module-named-numpy-distutils-msvccompiler)
- Set `requirements.txt`

    ```bash
    pip install pipreqs
    pipreqs --ignore "_env_qc, QAOAKit, __pycache__" .
    ```
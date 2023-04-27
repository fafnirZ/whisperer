C:\Users\Jacky\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe -m pip install pycrypto


$pathToSourceRoot = "C:\Users\Jacky\Documents\whisperer"
$env:PYTHONPATH = "$($pathToSourceRoot);"


pip uninstall pycrypto
pip install pycryptodome
pip install cryptidy
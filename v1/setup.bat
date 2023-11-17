@ECHO OFF

TITLE Stryd Exporter v1 Setup
echo Welcome to setup.
pause

echo Installing dependencies...
pip install -r ../requirements.txt

echo Done!
echo run 'python october.py' or 'python november.py'
pause
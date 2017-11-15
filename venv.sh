#!/bin/sh

pip=venv/bin/pip
activate=venv/bin/activate

virtualenv --no-site-packages venv

sudo chmod u+x ${activate}
./${activate}

${pip} install sphinx
${pip} install sphinx_rtd_theme

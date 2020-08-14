cd $(dirname $0)
export ROOT=$PWD
export PYTHONPATH=${ROOT}/lib
source virtualenvwrapper.sh
mktmpenv
cd ${ROOT}
pip install -r ${ROOT}/.freeze.pip
pytest

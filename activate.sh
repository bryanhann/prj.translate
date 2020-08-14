cd $(dirname $0)
export ROOT=$PWD
venv_id_file=${ROOT}/.tmp_venv_id_file
[[ -f ${venv_id_file} ]] || echo $RANDOM > ${venv_id_file}
venv_id=$(cat $venv_id_file)
echo $venv_id
mkvirtualenv $venv_id
workon $venv_id
pip install --upgrade pip
pip install -r ${ROOT}/.freeze.pip

export PYTHONPATH=${ROOT}/lib
echo "type 'pytest' to test."

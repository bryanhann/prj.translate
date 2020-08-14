cd $(dirname $0)
export PYTHONPATH=${PWD}/lib
#export ROOT=$PWD
#export venv_id=$(md5 -r -s $PWD | cut -c1-6)
#[[ -d $WORKON_HOME/$venv_id ]] || {
#    echo press enter to installing venv
#    read
#    mkvirtualenv $venv_id
#    echo press enter to upgrade
#    read
#    pip install --upgrade pip
#    pip install -r ${ROOT}/.freeze.pip
#}
#workon $venv_id
echo "type 'pytest' to test."

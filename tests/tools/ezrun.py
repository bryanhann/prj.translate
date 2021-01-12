import subprocess

EZRUN_TEMPLATE="""\
--stdout--
%s
--stderr--
%s
--returncode--
%s"""

def ezrun(cmd_list):
    process=subprocess.run( cmd_list, capture_output=True )
    out=process.stdout.decode('utf-8', 'ignore')
    err=process.stderr.decode('utf-8', 'ignore')
    code=str(process.returncode)
    return EZRUN_TEMPLATE % (out, err, code)


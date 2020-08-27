import subprocess

EZRUN_TEMPLATE="""\
------stdout--------
%s
------stderr--------
%s"""

def ezrun(cmd):
    cmd=cmd.split()
    process=subprocess.run( cmd, capture_output=True )
    out=process.stdout.decode('utf-8', 'ignore')
    err=process.stderr.decode('utf-8', 'ignore')
    return EZRUN_TEMPLATE % (out, err)


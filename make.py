#!/usr/bin/env python3

import os
import sys
import subprocess

build = sys.argv[ 1 ]
output = sys.argv[ 2 ]

subprocess.check_call( [ 'make', '-C', build ], env={ 'MACOSX_DEPLOYMENT_TARGET' : '10.9' } )
subprocess.check_call( [ 'rsync', '-u', os.path.join( build, 'src', 'libluajit.so' ), output ] )

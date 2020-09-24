#!/usr/bin/env python3

import os
import shutil
import subprocess
import sys

build = sys.argv[ 1 ]
output = sys.argv[ 2 ]

# Export variables for macOS build.
os.environ[ 'MACOSX_DEPLOYMENT_TARGET' ] = '10.9'

# Make libluajit.
subprocess.check_call( [ 'make', '-C', build ] )
input = os.path.join( build, 'src', 'libluajit.so' )

# Check if the build product is newer than our output file.
update = True
if os.path.exists( output ):
    intime = os.stat( input ).st_mtime
    outtime = os.stat( output ).st_mtime
    update = intime > outtime

# Update output file.
if update:

    # Copy file over.
    cp_file = output + ".install"
    os.makedirs( os.path.dirname( output ), exist_ok = True )
    shutil.copy2( input, cp_file )
    try:
        os.remove( output )
    except FileNotFoundError:
        pass
    os.rename( cp_file, output )

    # Update install name on macOS.
    if shutil.which( "install_name_tool" ):
        command = [ "install_name_tool", "-id", "@rpath/libluajit.dylib", output ]
        subprocess.check_call( command )

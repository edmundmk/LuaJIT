project( 'luajit', 'c' )

if host_machine.system() == 'darwin'
    output = 'libluajit.dylib'
else
    output = 'libluajit.so'
endif

make = find_program( 'make.py' )
root = meson.current_source_dir()

luajit_lib = custom_target( 'luajit', command : [ make, root, '@OUTPUT@' ], output : output, build_always : true, install : true, install_dir : get_option( 'libdir' ) )
luajit_lic = files( 'COPYRIGHT' )
luajit_dep = declare_dependency( include_directories : include_directories( 'src' ), link_with : luajit_lib )
install_headers( 'src/lua.h', 'src/luajit.h' )

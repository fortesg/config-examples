# config-examples

Example configuration files for FortranCallGraph and FortranTestGenerator 

### [plain](plain)
Plain samples from https://github.com/fortesg/fortrancallgraph and https://github.com/fortesg/fortrantestgenerator

### [icon](icon)
Christian's personal ICON configuration, usally tested with ICON's latest master

### [icon_pp](icon_pp)
Christian's personal ICON configuration for analysing preprocessed files

Compile ICON with `export FFLAGS=-save-temps -g -O0` and don't remove `*.f90` files in build directory.

Handle with care!
When you rerun the compiler/preprocesser after source modification, later analyses will use modified preprocessed files and not the backup files of the original source files.

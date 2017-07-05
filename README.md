# FRU-Build
C and Python tools to build FRU images for AMC and FMC boards

## Usage

On the repository root directory run

```
$ make
```

This command will generate 2 binaries: `amc-fru` and `fmc-fru`. You can run them independently with the following commands:

```
$ ./amc-fru output_dir serial_number
$ ./fmc-fru output_dir serial_number
```

Both executables will build a binary FRU image based on the information present in the headers in *user/* folder, *user_amc_fru.h* and *user_fmc_fru.h* respectively for each board type.

## Python script

In order to generate several similar FRU images at once just varying the serial number, for a production batch for example, one can use the **fru-deploy.py** in *script/* folder.

For AMC/AFC boards:
```
$ cd scripts/
$ python fru-deploy.py --board amc --start 1300101001 --end 1300101020 --dir output_dir
```

For FMC boards:
```
$ cd scripts/
$ python fru-deploy.py --board fmc --start 1400101001 --end 1400101020 --dir output_dir
```

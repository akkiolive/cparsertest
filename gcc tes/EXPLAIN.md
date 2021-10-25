# C Programming Source Error Check
2021/10/23

## Environment
```
Microsoft Windows 10 Home
10.0.19043 N/A Build 19043
Intel(R) Core(TM) i5-4690 CPU @ 3.50GHz
```

## Tools
- [ctags](https://github.com/universal-ctags/ctags-win32) (for windows)
- [cflow](https://www.gnu.org/software/cflow/) ([v1.6](https://ftp.gnu.org/gnu/cflow/))
  - [MSYS2](https://www.msys2.org/)

## Errors to check
|Error|Description|tool|
|-|-|-|-|
|Undefined variable|Refered `extern int v;` but no definition of `int v`|ctags|
|Undefined function|Called `extern void func();` but no definition of `void func()`|cflow|
|Duplicate variable|Two or more of same variable names are defined|ctags|
|Duplicate function|Two or more of same function names are defined|ctags|
|Different type variable|Defined `int v;` but referenced `extern float v;`|ctags|
|Different type function|Defined `int func();` but referenced `extern float func();`|ctag|
|Non-used variable|Non used variable in any files|ctags|
|Non-used function|Non used function in any files|cflow|


## Tools installation
### ctags
1. Visit [releases](https://github.com/universal-ctags/ctags-win32/releases) of [universal-ctags/ctags-win32](https://github.com/universal-ctags/ctags-win32)
1. Download "ctags-2021-10-20_p5.9.20211017.0-4-gdf3e2f58-x64.zip"
1. Extract the zip
2. Find "ctags.exe" and place it to as "C:\ctags\ctags.exe"
3. PATH to "C:\ctags"


### cflow
#### 1. MSYS2
1. Install [MSYS2](https://www.msys2.org/)
1. Start MSYS2 shell (purple window)
2. Type below command to update msys2 packages
   `pacman -Syuu`
3. Type below command to install base environments (all)
   `pacman -S base-devel mingw-w64-x86_64-toolchain`
1. Type below command to install gcc
   `pacman -S gcc`

#### 2. cflow
1. Visit [GNU cflow](https://www.gnu.org/software/cflow/)
   >Downloading cflow
Stable releases of GNU cflow are available for download from FTP archives on [gnu.org](https://ftp.gnu.org/gnu/cflow/) and from various mirrors worldwide. Please choose the location closer to you.
1. Downloading cflow -> gnu.org -> cflow-1.6.tar.gz
2. Extract the tar.gz by 7-zip
3. Start MSYS2 shell (purple window)
4. `cd cflow-1.6`
5. `./configure`
6. `make`
7. `cd src`
8. `./cflow --version`
9. Succeeded if below displayed:
```
$ ./cflow --version
cflow (GNU cflow) 1.6
Copyright (C) 2005-2019 Sergey Poznyakoff
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Sergey Poznyakoff.
```
## Tools basic usage
### ctags
```C
#define MMM 123

int foo;
extern long nuke;

double func(int, char*);
extern void funcB(double);

int main(){
    int lar = 1;
    foo = lar;
    func(foo, "bar");

    return 0;
}
```
Execute below command:
```bash
ctags --language-force=C --kinds-C=* --fields=* -x file.c
```
Here `-x` option means the output is on `stdout`:
```
$ ./ctags --language-force=C --kinds-C=* --fields=* -x file.c
MMM              macro         1 file.c           #define MMM 123
__anonfd762eb6010d parameter     6 file.c           double func(int, char*);
__anonfd762eb6020d parameter     6 file.c           double func(int, char*);
__anonfd762eb6030d parameter     7 file.c           extern void funcB(double);
foo              variable      3 file.c           int foo;
func             prototype     6 file.c           double func(int, char*);
funcB            prototype     7 file.c           extern void funcB(double);
lar              local        10 file.c           int lar = 1;
main             function      9 file.c           int main(){
nuke             externvar     4 file.c           extern long nuke;
```
If `-x` omitted the `ctags` file is generated:
```bash
ctags --language-force=C --kinds-C=* --fields=* file.c
```
The output in `ctags` file are below:
```
!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/;"	extras:pseudo
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/;"	extras:pseudo
!_TAG_OUTPUT_EXCMD	mixed	/number, pattern, mixed, or combineV2/;"	extras:pseudo
!_TAG_OUTPUT_FILESEP	slash	/slash or backslash/;"	extras:pseudo
!_TAG_OUTPUT_MODE	u-ctags	/u-ctags or e-ctags/;"	extras:pseudo
!_TAG_PATTERN_LENGTH_LIMIT	96	/0 for no limit/;"	extras:pseudo
!_TAG_PROC_CWD	**********************	//;"	extras:pseudo
!_TAG_PROGRAM_AUTHOR	Universal Ctags Team	//;"	extras:pseudo
!_TAG_PROGRAM_NAME	Universal Ctags	/Derived from Exuberant Ctags/;"	extras:pseudo
!_TAG_PROGRAM_URL	https://ctags.io/	/official site/;"	extras:pseudo
!_TAG_PROGRAM_VERSION	5.9.0	/df3e2f58/;"	extras:pseudo
MMM	file.c	/^#define MMM /;"	kind:macro	line:1	language:C	file:	roles:def	extras:fileScope	end:1
__anonfd762eb6010d	file.c	/^double func(int, char*);$/;"	kind:parameter	line:6	language:C	scope:prototype:func	typeref:typename:int	file:	roles:def	extras:fileScope,anonymous	nth:0
__anonfd762eb6020d	file.c	/^double func(int, char*);$/;"	kind:parameter	line:6	language:C	scope:prototype:func	typeref:typename:char *	file:	roles:def	extras:fileScope,anonymous	nth:1
__anonfd762eb6030d	file.c	/^extern void funcB(double);$/;"	kind:parameter	line:7	language:C	scope:prototype:funcB	typeref:typename:double	file:	roles:def	extras:fileScope,anonymous	nth:0
foo	file.c	/^int foo;$/;"	kind:variable	line:3	language:C	typeref:typename:int	roles:def	end:3
func	file.c	/^double func(int, char*);$/;"	kind:prototype	line:6	language:C	typeref:typename:double	file:	signature:(int,char *)	roles:def	extras:fileScope	end:6
funcB	file.c	/^extern void funcB(double);$/;"	kind:prototype	line:7	language:C	typeref:typename:void	file:	signature:(double)	roles:def	extras:fileScope	end:7
lar	file.c	/^    int lar = 1;$/;"	kind:local	line:10	language:C	scope:function:main	typeref:typename:int	file:	roles:def	extras:fileScope	end:10
main	file.c	/^int main(){$/;"	kind:function	line:9	language:C	typeref:typename:int	signature:()	roles:def	end:15
nuke	file.c	/^extern long nuke;$/;"	kind:externvar	line:4	language:C	typeref:typename:long	roles:def	end:4
```


### cflow
*file1.c*
```C
void func(int *);
extern void func_MAIN();

int main(){
    int *a;
    *a = 0;
    func(a);
    func_MAIN();
    return 0;
}

void func(int *out){
    if(*out++ < 10)
        func(out);
}
```
*file2.c*
```C
void func_MAIN(){
    funcA();
    funcB();
}

void funcA1(){}
void funcA2(){}
void funcA3(){}
void funcA4(){}

void funcA(){
    funcA1();
    funcA2();
    funcA3();
    funcA4();
}


void funcB(){
    
}
```
Execute below command on MSYS2 shell
```
./cflow file1.c file2.c
```
The output will be on `stdout` as below:
```
$ ./cflow file1.c file2.c
main() <int main () at file1.c:4>:
    func() <void func (int *out) at file1.c:12> (R):
        func() <void func (int *out) at file1.c:12> (recursive: see 2)
    func_MAIN() <void func_MAIN () at file2.c:1>:
        funcA() <void funcA () at file2.c:11>:
            funcA1() <void funcA1 () at file2.c:6>
            funcA2() <void funcA2 () at file2.c:7>
            funcA3() <void funcA3 () at file2.c:8>
            funcA4() <void funcA4 () at file2.c:9>
        funcB() <void funcB () at file2.c:19>
```


## C Source Error Analyze
## Errors to check
|#|Error|Description|tool|
|-|-|-|-|-|
|1|Undefined variable|Refered `extern int v;` but no definition of `int v`|ctags|ctag|
|2|Undefined function|Called `extern void func();` but no definition of `void |func()`|cflow|
|3|Duplicate variable|Two or more of same variable names are defined|ctags|
|4|Duplicate function|Two or more of same function names are defined|ctags|
|5|Different type variable|Defined `int v;` but referenced `extern float v;`|ctags|
|6|Different type function|Defined `int func();` but referenced `extern float |func();`|ctags|
|7|Non-used variable|Non used variable in any files|ctags|
|8|Non-used function|Non used function in any files|cflow|

### 1. Undefined variable
>Refered `extern int v;` but no definition of `int v`

Example case:
_file1.c_
```C
extern int v;

int main(){
    v = 3;
}
```
_file2.c_
```c
int w;
```
Here, execute `ctags` command as below
```
ctags --language-force=C --kinds-C=* --fields=* *.c
```
then the output `ctags` file is as below
```
!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/;"	extras:pseudo
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/;"	extras:pseudo
!_TAG_OUTPUT_EXCMD	mixed	/number, pattern, mixed, or combineV2/;"	extras:pseudo
!_TAG_OUTPUT_FILESEP	slash	/slash or backslash/;"	extras:pseudo
!_TAG_OUTPUT_MODE	u-ctags	/u-ctags or e-ctags/;"	extras:pseudo
!_TAG_PATTERN_LENGTH_LIMIT	96	/0 for no limit/;"	extras:pseudo
!_TAG_PROC_CWD	**********************	//;"	extras:pseudo
!_TAG_PROGRAM_AUTHOR	Universal Ctags Team	//;"	extras:pseudo
!_TAG_PROGRAM_NAME	Universal Ctags	/Derived from Exuberant Ctags/;"	extras:pseudo
!_TAG_PROGRAM_URL	https://ctags.io/	/official site/;"	extras:pseudo
!_TAG_PROGRAM_VERSION	5.9.0	/df3e2f58/;"	extras:pseudo
main	file1.c	/^int main(){$/;"	kind:function	line:3	language:C	typeref:typename:int	signature:()	roles:def	end:5
v	file1.c	/^extern int v;$/;"	kind:externvar	line:1	language:C	typeref:typename:int	roles:def	end:1
w	file2.c	/^int w;/;"	kind:variable	line:1	language:C	typeref:typename:int	roles:def	end:1
```
Each fileds separated with `\t` are:
- _The **externed** global variable `v`_

`v	file1.c	/^extern int v;$/;"	kind:externvar	line:1	language:C	typeref:typename:int	roles:def	end:1`
|index|content|decription|
|-|-|-|
|0|`v`|Name of variable|
|1|`/^extern int v;$/;"`|Source line enclosed with `/^` and `$/;`<br>,but if the `kind` is `macro`, then `$` will not be printed.|
|2|`kind:externvar`|`kind` will be `variable`, `externvar`, `local`,  `function`, or `macro`|
|3|`line:1`|Line start number in the source file|
|4|`language:C`||
|5|`typeref:typename:int`|Type of variable|
|6|`roles:def`||
|7|`end:1`|Line end number in the source file|

- _The **defined** global variable `w`_

`w	file2.c	/^int w;/;"	kind:variable	line:1	language:C	typeref:typename:int	roles:def	end:1`

To detect this, make a script like below: (python)
```python
def ExecuteCtags(func):
    import subprocess
    def wrapper(*args, **kwargs):
        out = subprocess.run(["./ctags --language-force=C --kinds-C=* --fields=* *.c"], shell=True, capture_output=True)
        func(*args, **kwargs)
    return wrapper

@ExecuteCtags
def FindUndefinedVariables(filename="tags"):
    # read ctags
    with open(filename, "r", encoding="ascii") as f:
        lines = f.read().split("\n")

    variables_externed = {}
    variables_defined = {}

    # read each lines
    for line in lines:
        # skip vacant line, or comments line
        if not line or line.startswith("!"):
            continue
        symbol = line.split("\t")[0]
        # find defined global variable
        if "\tkind:vairable" in line:
            variables_defined[symbol] = None
        elif "\tkind:externvar" in line:
            variables_externed[symbol] = None

    # find error
    Undefined_variables = []
    for variable in variables_externed:
        if variable not in variables_defined:
            print("Undefined variable:", variable)
            Undefined_variables.append(variable)
    return Undefined_variables

if __name__ == "__main__":
    FindUndefinedVariables()
```
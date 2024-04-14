@echo off
call "C:\Program Files (x86)\Intel\oneAPI\compiler\latest\env\vars.bat" intel64 vs2019

set JOB_ID=Job-1

@REM Nothing to touch here after

set case_root=%CD%

if /I "%~1"=="all" goto all
if /I "%~1"=="pre" goto pre
if /I "%~1"=="cae-runscript" goto cae-runscript
if /I "%~1"=="keep-odb-cae-jnl" goto keep-odb-cae-jnl
if /I "%~1"=="extract" goto extract
if /I "%~1"=="plot" goto plot
if /I "%~1"=="clean" goto clean
if /I "%~1"=="" goto all
goto error

:all
    call make.bat clean
    call make.bat pre
    call make.bat cae-runscript
    call make.bat keep-odb-cae-jnl
    call make.bat extract
    call make.bat plot
    goto :eof

:pre
    if not exist %case_root%\abq_run\ (
        mkdir %case_root%\abq_run
    )
    goto :eof

:cae-runscript
    pushd %case_root%\abq_run
    call abaqus cae noGUI=../CompShock.py
    popd
    goto :eof

:keep-odb-cae-jnl
    for %%A in (%case_root%\abq_run\*) do (
        if not "%%~xA"==".odb" if not "%%~xA"==".cae" if not "%%~xA"==".jnl" if not "%%~xA"==".png" (
            del /Q "%%A"
        )
    )
    goto :eof

:extract
    pushd %case_root%\abq_run
    call abaqus python ..\..\..\Python\AbaqusExtract.py
    popd
    goto :eof

:plot
    pushd %case_root%\abq_run
    python3 ..\..\..\Python\replaceString.py %JOB_ID% %JOB_ID%_ %JOB_ID%-
    python3 ..\..\..\Python\PlotCurves.py
    popd
    goto :eof

:clean
    if exist %case_root%\abq_run\ (
        echo Cleaning: %case_root%\abq_run
        @REM rd /S /Q %case_root%\abq_run\
        for %%A in (%case_root%\abq_run\*) do (
            if not "%%~xA"==".png" (
                del /Q "%%A"
            )
        )
    )
    goto :eof

:subclean
    call make.bat clean
    goto :eof

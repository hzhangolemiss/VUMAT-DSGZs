@echo off
call "C:\Program Files (x86)\Intel\oneAPI\compiler\latest\env\vars.bat" intel64 vs2019

set ENTITY=CubicElement-Radial

@REM set ABQ_TYPE=D
set ABQ_TYPE=DTd

set VUMAT_MODEL=%ENTITY%_VUMAT
set VUMAT_JOB_SNRwBiNUM=%ENTITY%_VUMAT_SNRwBiNUM

set NCPUS=1
set NDOMAINS=%NCPUS%

@REM Nothing to touch here after

set case_root=%CD%

if /I "%~1"=="all" goto all
if /I "%~1"=="pre" goto pre
if /I "%~1"=="vumat-snrwbinum" goto vumat-snrwbinum
if /I "%~1"=="keep-odb" goto keep-odb
if /I "%~1"=="extract" goto extract
if /I "%~1"=="plot" goto plot
if /I "%~1"=="clean" goto clean
if /I "%~1"=="" goto all
goto error

:all
    call make.bat clean
    call make.bat pre
    call make.bat vumat-snrwbinum
    call make.bat keep-odb
    call make.bat extract
    call make.bat plot
    goto :eof

:pre
    if not exist %case_root%\abq_run_%ABQ_TYPE%\ (
        mkdir %case_root%\abq_run_%ABQ_TYPE%
    )
    goto :eof

:vumat-snrwbinum
    pushd %case_root%\abq_run_%ABQ_TYPE%
    call abaqus job=%VUMAT_JOB_SNRwBiNUM% cpus=%NCPUS% mp_mode=threads parallel=domain domains=%NDOMAINS% dynamic_load_balancing=on input=..\%VUMAT_MODEL%_%ABQ_TYPE%.inp user=..\..\..\VUMAT\VUMAT-gDSGZ-SNRwBiNUM.f double=both interactive ask_delete=OFF
    popd
    goto :eof

:keep-odb
    for %%A in (%case_root%\abq_run_%ABQ_TYPE%\*) do (
        if not "%%~xA"==".odb" if not "%%~xA"==".png" (
            del /Q "%%A"
        )
    )
    goto :eof

:extract
    pushd %case_root%\abq_run_%ABQ_TYPE%
    call abaqus python ..\..\..\Python\AbaqusExtract.py
    popd
    goto :eof

:plot
    pushd %case_root%\abq_run_%ABQ_TYPE%
    python3 ..\..\..\Python\replaceString.py %VUMAT_JOB_SNRwBiNUM% %VUMAT_JOB_SNRwBiNUM%_ VUMAT-SNRwBiNUM-
    python3 ..\..\..\Python\PlotCurves.py
    popd
    goto :eof

:clean
    if exist %case_root%\abq_run_%ABQ_TYPE%\ (
        echo Cleaning: %case_root%\abq_run_%ABQ_TYPE%
        @REM rd /S /Q %case_root%\abq_run_%ABQ_TYPE%\
        for %%A in (%case_root%\abq_run_%ABQ_TYPE%\*) do (
            if not "%%~xA"==".png" (
                del /Q "%%A"
            )
        )
    )
    goto :eof

:subclean
    call make.bat clean
    goto :eof

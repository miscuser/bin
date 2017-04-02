@echo off
echo Searching for latest file...

FOR /F "delims=|" %%I IN ('DIR "J:\videos\TV Shows\2 Broke Girls\Season 06\*.*" /B /O:D') DO SET NewestFile=%%I

echo Found: %NewestFile%

echo Checking historical file...

@echo off
find "%NewestFile%" "C:\Dropbox\logs\2 Broke Girls\2 Broke Girls.txt" && (
    echo %NewestFile% was already processed...
    pause
) || (
    echo %NewestFile% was NOT found.
    
    echo Logging latest file...
    echo %NewestFile% >> "C:\Dropbox\logs\2 Broke Girls\2 Broke Girls.txt"
    
    echo Copying file...
    copy "J:\videos\TV Shows\2 Broke Girls\Season 06\%NewestFile%" c:\dl
    
    echo Extracting audio from video...
    C:\cygwin64\home\main\bin\win\2BG\vid2mp3.bat
    
    echo Updating audio metadata...
    2BrokeGirls.py -d c:\dl\

   	echo Moving audio files to iTunes folder...
    move c:\dl\2*Broke*mp3 "J:\Music\Automatically Add to iTunes\"

   	echo Cleaning temp folder...
    del c:\dl\2*Broke*.*
    
    pause
)

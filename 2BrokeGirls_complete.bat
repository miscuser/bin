@echo off
echo Searching for latest file...

FOR /F "delims=|" %%I IN ('DIR "J:\videos\TV Shows\2 Broke Girls\Season 06\*.*" /B /O:D') DO SET NewestFile=%%I

echo Found: %NewestFile%

echo Checking historical file...

@echo off
find "%NewestFile%" "C:\Users\main\Google Drive\logs\2 Broke Girls\2 Broke Girls.txt" && (
    echo %NewestFile% was already processed...
    pause
) || (
    echo %NewestFile% was not found.
    
    echo Logging latest file...
    echo %NewestFile% >> "C:\Users\main\Google Drive\logs\2 Broke Girls\2 Broke Girls.txt"
    
    echo Copying file...
    copy "J:\videos\TV Shows\2 Broke Girls\Season 06\%NewestFile%" c:\dl
    
    echo Extracting audio from video...
    for %%a in ("c:\dl\2*Broke*.mkv") do avconv -i "%%a" -loglevel panic -threads auto -vn -qscale:a 9 "c:\dl\%%~na.mp3"
    
    echo Updating audio metadata...
    c:\python27\python.exe C:\cygwin64\home\main\bin\2BrokeGirls -d c:\\dl\\

   	echo Moving audio files to iTunes folder...
    move c:\dl\2*Broke*mp3 "J:\music\Automatically Add to iTunes\"

   	echo Cleaning temp folder...
    del c:\dl\2*Broke*.*
    
    pause
)

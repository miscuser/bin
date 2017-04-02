:: https://trac.ffmpeg.org/wiki/Encode/MP3
:: lame option    Average kbit/s    Bitrate range kbit/s    ffmpeg/avconv option
::       -V 0        245                  220-260                -q:a 0
::       -V 1        225                  190-250                -q:a 1
::       -V 2        190                  170-210                -q:a 2
::       -V 3        175                  150-195                -q:a 3
::       -V 4        165                  140-185                -q:a 4
::       -V 5        130                  120-150                -q:a 5
::       -V 6        115                  100-130                -q:a 6
::       -V 7        100                   80-120                -q:a 7
::       -V 8        85                    70-105                -q:a 8
::       -V 9        65                     45-85                -q:a 9

set folder="c:\dl"

for %%a in ("%folder%\*.mp4") do avconv -i "%%a" -loglevel panic -threads auto -vn -qscale:a 2 "c:\dl\%%~na.mp3"
for %%a in ("%folder%\*.avi") do avconv -i "%%a" -loglevel panic -threads auto -vn -qscale:a 2 "c:\dl\%%~na.mp3"
for %%a in ("%folder%\*.mkv") do avconv -i "%%a" -loglevel panic -threads auto -vn -qscale:a 2 "c:\dl\%%~na.mp3"
for %%a in ("%folder%\*.flac") do avconv -i "%%a" -loglevel panic -threads auto -vn -qscale:a 2 "c:\dl\%%~na.mp3"
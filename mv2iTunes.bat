@echo off

echo Moving audio files to iTunes folder...

:loop
      :: Default to dl directory.
      if ["%~1"]==[""] (
        move c:\dl\*mp3 "J:\Music\Automatically Add to iTunes\"
        goto end
      )
      :: Use directory from command line.
      if not exist %~s1 (
        echo not exist
      ) else (
        echo exist
        if exist %~s1\NUL (
          move %1\*.mp3 "J:\Music\Automatically Add to iTunes\"
        ) else (
          echo is a file
        )
      )
      ::-------
      shift
      goto loop
:end

pause

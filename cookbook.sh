# Various Bash recipes for all occasions.

### Rename files using wildcard and regular expressions.
# Replace Season with blanks.
for f in *.mp4; do mv "$f" "`echo $f | sed s/Season\ //`"; done

# Replace Episode with x0.
for f in *.mp4; do mv "$f" "`echo $f | sed s/\ Episode\ /x0/`"; done



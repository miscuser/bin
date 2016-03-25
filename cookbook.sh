# Various Bash recipes for all occasions.

### Rename files using wildcard and regular expressions.
# Replace Season with blanks.
for f in *.mp4; do mv "$f" "`echo $f | sed s/Season\ //`"; done

# Replace Episode with x0.
for f in *.mp4; do mv "$f" "`echo $f | sed s/\ Episode\ /x0/`"; done

# Create multiple directories at once.
# This will create blah\testing and blah\dummy -- do not put a space after the commas 
mkdir -p blah/{testing,dummy}
# Multiple levels can be created at once.
mkdir -p projects/{src,doc/{api,system},tools,db}



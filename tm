#!/bin/bash

# abort if we're already inside a tmux session
if ! { [ "$TMUX" == "" ] ;} then 
    exit 0
fi
# startup a "default" session if non currently exists
# tmux has-session -t _default || tmux new-session -s _default -d

# present menu for user to choose which workspace to open
PS3="Choose your session: "
options=($(tmux list-sessions -F "#S") "new session" "cancel")
echo "Available sessions"
echo "------------------"
echo " "
select opt in "${options[@]}"
do
    case $opt in
        "new session")
            read -p "Enter new session name: " SESSION_NAME
            tmux new -s "$SESSION_NAME"
            break
            ;;
        "cancel")
            break;;
        *)
            tmux attach-session -t $opt
            break
            ;;
    esac
done


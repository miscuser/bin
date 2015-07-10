#!/bin/bash

# Abort if we're already inside a tmux session.
if ! { [ "$TMUX" == "" ] ;} then 
    exit 0
fi

# Start a default session if none currently exists.
# tmux has-session -t _default || tmux new-session -s _default -d

# Present menu for user to choose a workspace.
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


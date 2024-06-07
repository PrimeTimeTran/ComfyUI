export PATH="C:\ProgramData\anaconda3\condabin:$PATH"
export PATH="C:\ProgramData\anaconda3\Scripts:$PATH"
export PATH="C:\ProgramData\anaconda3:$PATH"

export LPATH=$LPATH:/usr/lib/nvidia-current:/opt/bin:/opt/lib64:/opt/lib
export LIBRARY_PATH=$LIBRARY_PATH:/usr/lib/nvidia-current:/opt/lib64:/opt/lib
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia-current:/opt/lib64:/opt/lib
export PATH=$PATH:/opt/bin:/opt/lib64:/opt/lib

alias bp="code ~/.bashrc"
alias l="ls -al"
alias gs="git status"
alias gcm="git commit -m"

eval "$(command conda 'shell.bash' 'hook' 2> /dev/null)"
echo "Times ticking"



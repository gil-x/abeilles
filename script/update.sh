#!/bin/bash

# CONFIG VAR
gitID=""

env="$1"
user="$(whoami)"
root="/home/${user}"

logFile="${root}/logs/update.log"

pyEnv="${root}/virtualenv/${env}/3.8/bin/activate"
pyRoot="${root}/${env}"

peEntry="${pyRoot}/tmp"

# FUNCTIONS GLOBAL
err() {
    echo "FATAL ERROR: ${1}"
    exit 1
}

quit() {
    log -1 "Program Termination"
    exit 0
}

log() {
    local _buff=""

    if [ "$1" -eq 1 ]; then _buff="ERROR"
    else _buff="INFO "; fi

    _buff="[${env}] $(date '+%H%M%S-%d%m%y') ${_buff}: ${2}"

    echo "$_buff"
    echo "$_buff" >> "$logFile"
}

# FUNCTIONS GIT
gitNeedPull() {
    export GIT_DIR="$pyRoot/.git"

    if ! git fetch 2>&1; then
        log 1 "Repository '${pyRoot}' can't fetch"
        log 1 "${_buff}"
        return 1
    fi

    if git checkout | grep "git pull" 2>&1; then
        return 0
    fi

    log 0 "Repository '${pyRoot}' nothing to do"
    return 1
}

gitPull() {
    local _branch
    export GIT_DIR="$pyRoot/.git"

    gitID="$(git rev-parse HEAD)"
    _branch="remotes/origin/$(git branch --show-current)"

    if git reset --hard "${_branch}" 2>&1; then
        log -1 "Repository '${pyRoot}' updated"
        git clean -fd
        return 0
    fi

    log 1 "Fail to update '${pyRoot}' repository"
    log 1 "${_buff}"
    return 1
}

gitItemIsUpdated() {
    local _item
    #export GIT_DIR="$pyRoot/.git"

    _item="$1"
    if [[ -z $_item ]]; then
        log 1 "Function 'gitItemIsUpdated' require a parameter"
        return 1
    fi

    if git diff --name-only HEAD "$gitID" | grep "$_item" 2>&1; then
        log -1 "Latest commit update this file '${_item}'"
        return 0
    fi

    return 1
}

# FUNCTION SYS
passengerStop() {
    if touch "${peEntry}/stop.txt"; then
        log -1 "WebApp '${env}' stop request sended to Passenger"
        return 0
    fi

    log 1 "WebApp '${env}' stop request failed"
    return 1
}

passengerRestart() {
    if touch "${peEntry}/restart.txt"; then
        log -1 "WebApp '${env}' restart request sended to Passenger"
        return 0
    fi

    log 1 "WebApp '${env}' restart request failed"
    return 1
}

# MAIN
# Declaration
log 0 "# UPDATE --> For: '${env}'"

# Check env
[[ -z $env ]] && err "WebApp name required"

# Chargement de l'environement py
# shellcheck source=/dev/null
. "$pyEnv"
cd "$pyRoot" || err "Can't go inside '${pyRoot}'"

# Check si besoin de pull
if ! gitNeedPull; then
    quit
fi

# On pull
gitPull || err "GitPull error"

# Check si requirements change
if gitItemIsUpdated "requirements"; then
    pip install --no-input -r requirements.txt
fi

# Mise a jour
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Redemarage du service
passengerRestart || err "WebApp update failled"

quit
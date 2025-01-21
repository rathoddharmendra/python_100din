# new_learnen

cat <<EOF >> ~/.bash_profile
export TWILIO_PHONE_NUMBER=+14066041514
export ANOTHER_VARIABLE=value
export PATH=\$PATH:/new/path
EOF

~/.bash_profile >> persisten storage of api keys across sessions
source ~/.bash_profile > to load in the current session
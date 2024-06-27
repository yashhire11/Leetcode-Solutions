# Read from the file file.txt and output all valid phone numbers to stdout.

regex1="^[0-9]\{3\}\-[0-9]\{3\}\-[0-9]\{4\}$"
regex2="^([0-9]\{3\}) [0-9]\{3\}\-[0-9]\{4\}$"

# grep - e "$regex1" -e "$regex2" file.txt

# awk "/^[0-9]{3}\-[0-9]{3}-[0-9]{4}$|^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$/ {print}" file.txt

sed -n -E "/^[0-9]{3}\-[0-9]{3}-[0-9]{4}$|^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$/p" file.txt

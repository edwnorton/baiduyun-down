#!/bin/bash
cd ~/mywork/Wechat/baiduyun/
a="s"
path="/book/"
for i in $(cat downurl_lists.txt)
do
url=$(echo ${i}|awk -F"," '{print $1}')
password=$(echo ${i}|awk -F"," '{print $2}')
echo -e $url >> b.log
/usr/bin/expect <<EOF
set time 5
spawn ./baiduyun.py ${a} ${url} ${path}
expect {
"enterpasswd:" {send "${password}\r"}
}
expect eof
EOF
done

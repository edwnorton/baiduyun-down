#!/bin/bash
Bashpath="/home/tq/mywork/Wechat/baiduyun/ireadweekdown"
downurl_lists="/home/tq/mywork/Wechat/baiduyun/ireadweekdown/downurl_lists.txt"
downpath="/home/tq/mywork/Wechat/baiduyun/ireadweekdown/book"
cd ${Bashpath}
a="s"
d="d"
path="/book/ireadweek/"
for i in $(cat ${downurl_lists})
do
    if [ `echo $i|egrep pan.baidu` ];then
    echo -e $i >> b.log
    /home/tq/mywork/Wechat/baiduyun/ireadweekdown/baiduyun.py ${a} ${i} ${path}
    #/home/tq/mywork/Wechat/baiduyun/ireadweekdown/baiduyun.py ${d} ${i} ${downpath}
    sleep 1
    fi
done

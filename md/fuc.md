# fuc.md

## frequently used commands

sudo raspi-config

reboot

ls -lsh

ls -R | wc -l

df

du -sh

cd -

exit

docker-compose exec web bash

docker-compose up -d --build

docker-compose down

docker-compose pull code

docker restart api

docker rm

docker ps -a

docker images

docker image prune

docker logs --tail 1000 --follow api

vi requirements.txt

vi Dockerfile.api

sudo systemctl daemon-reload

sudo systemctl start ibi

sudo systemctl stop ibi

sudo systemctl restart ibi

sudo systemctl status ibi

journalctl -u ibi -f

source ibi/venv/bin/activate

rsync -avz --progress --delete

sudo dpkg -i xyz.deb 

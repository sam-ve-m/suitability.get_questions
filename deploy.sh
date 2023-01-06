fission spec init
fission env create --spec --name acc-suit-quest-get-env --image nexus.sigame.com.br/fission-account-suit-quest-get:0.1.0 --poolsize 0 --version 3 --imagepullsecret "nexus-v3" --spec
fission fn create --spec --name acc-suit-quest-get-fn --env acc-suit-quest-get-env --code fission.py --targetcpu 80 --executortype newdeploy --maxscale 3 --requestsperpod 10000 --spec
fission route create --spec --name acc-suit-quest-get-rt --method GET --url /suitability/questions --function acc-suit-quest-get-fn
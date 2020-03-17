#$1-dicionario
#$2-nomearquivo
#$3-hosts



echo "rodar com todos arquivos no mesmo diretorio"

while read line; do
        echo "maquina $line"
        echo "transfer files to $line">>log.txt
        scp ./updatefile.py root@$line:/var/>>log.txt
        scp $1 root@$line:/var/>>log.txt
        echo "run command" >> log.txt
        screen -dm ssh root@$line "python /var/updatefile.py /var/$1 $2">>log.txt
done < "$3"

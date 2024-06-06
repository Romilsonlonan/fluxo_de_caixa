#!/bin/bash

python3 -m pip install -r bundle.txt

if [ $? -eq 0 ]; then
    echo "Instalação concluída com sucesso!"
    # Adicionando o comando para iniciar o aplicativo 
    python3 app.py 
else
    echo "Houve um problema na instalação das dependências."
fi







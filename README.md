
# GProcessos
Gestor de Processos de Arquivo | Python 3.6 + Django 2.2


## Tutorial: Deploy no Apache2 | Debian

#### Preparando o sistema

`sudo apt update && apt dist-upgrade`

#### Instalando os requerimentos

`sudo apt install apache2`

`sudo apt install python3-pip python-dev build-essential`

`sudo apt install libapache2-mod-wsgi-py3`

#### Instalando virtualenv

`sudo python3 -m pip install virtualenv`

#### Pasta raiz onde tudo vai acontecer

`sudo cd /var/www/`

#### Criando o enviroment

`sudo python3 -m virtualenv env` 

#### Ativando o env

`source env/bin/activate`

#### Instalando os modules necessários

`pip3 install django`

### Criando um projeto
#### Dentro da pasta /var/www/env/ crie uma pasta “src”

`sudo mkdir env/src && cd src`

Baixando o projeto direto do Github

`sudo django-admin.py startproject --template=https://github.com/MartinsMessias/GProcessos/archive/master.zip --name=Procfile GProcessos`

#### A partir daqui é django então você sabe. Vamos pro apache2

### Configurando o apache

Por default, o arquivo de configuração do apache fica localizado em
**/etc/apache2/sites-available/000-default.conf**

Com um editor no console de sua preferência, apague tudo o que estiver dentro.
Eu curto o nano.

Vamos configurar:

`nano /etc/apache2/sites-available/000-default.conf`

    <VirtualHost *:80>  
	    ServerName localhost  
	    ServerAdmin webmaster@localhost  
      
	    # Substituir pelo endereço da sua pasta "static"
	    Alias /static "/home/trhat/PycharmProjects/GProcessos/static"  
	    <Directory "/home/trhat/PycharmProjects/GProcessos/static">  
		    Require all granted  
	    </Directory>  
	      
	    # Substituir pelo endereço da sua pasta "media"
	    Alias /userfiles "/home/trhat/PycharmProjects/GProcessos/userfiles"  
	    <Directory "/home/trhat/PycharmProjects/GProcessos/userfiles">  
		    Require all granted  
	    </Directory>  
	      
	    # Substituir pelo endereço da pasta do seu "wsgi.py"
	    <Directory /home/trhat/PycharmProjects/GProcessos/GProcessos>  
		    <Files wsgi.py>  
			    Require all granted  
		    </Files>  
	    </Directory>  
	      
	      # Substituir pelo endereço da suas devidas pastas
	      # Pasta do projeto:Pasta do Python
	    WSGIDaemonProcess GProcessos python-path=/var/www/env/src/GProcessos:/var/www/env/lib/python3.7/site-packages  
	    WSGIProcessGroup GProcessos  
	    # Pasta onde esta o wsgi.py
	    WSGIScriptAlias / /var/www/env/src/GProcessos/GProcessos/wsgi.py  
	    WSGIPassAuthorization On  
	      
	      
	    ErrorLog ${APACHE_LOG_DIR}/error.log  
	    CustomLog ${APACHE_LOG_DIR}/access.log combined  
    </VirtualHost>


#### Salve o arquivo e dê um: service apache2 restart
#### Tente acessar o ip no navegador e deve estar correndo tudo bem.
#### Agora você já tem sua aplicação rodando.

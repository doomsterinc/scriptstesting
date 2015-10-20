#!/usr/bin/python
# -*- coding:iso-8859-1 -*-

import os
import time

back_dir = '/root/bkpdb/'
log_dir = '/var/log/backups_sgdb.log'

def dumpsgdb (user,host,passwd,*databases):
	#databases = ['mysql'] #lista dos bancos de dados que estarão no backup
	mes = back_dir + time.strftime(%b)
	if not os.path.exists(mes):
		os.mkdir(mes)
	for db in databases:
		name_dkp = mes + '/' + host + ‘_’ + db + ‘-‘+ time.strftime(‘%d-%m-%Y_%H:%M:%S’) + ‘.sql.gz’
		dump_db = "/usr/bin/mysqldump –quick -u %s -h %s -p%s %s | gzip > %s" % (user,host,passwd,db,name_bkp)
	if os.system(dump_db) != 0:
		msg_log = "echo Erro no backup %s >> %s" %(name_dkp, log_dir)
		os.system(msg_log)
		break
	else:
		msg_log = "echo Backup %s realizado com sucesso >> %s" % (name_bkp,log_dir)
		os.system(msg_log)

dumpsgdb(‘usuario’,’nome-do-host-do-servidor.com.br’,’senha-do-usuario’,’db1′,’db2′,’db3′,’db4′)
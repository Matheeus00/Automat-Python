import datetime
import os
import shutil
import logzero
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

today = datetime.datetime.now()
today_str = today.strftime('%d%m%Y')

path = '//home//matheus'
dst = '//home//matheus//Área de Trabalho'

def mover(path, dst):
    for lista in path:
        diretorio = os.listdir(path)
        for file in diretorio:
            if today_str in file:
                pass
            else:
                shutil.copy(path + file, dst)


def cria_log():
    data_arq = today.strftime('%a%d%m%y')
    logzero.logfile('//home//matheus//Área de Trabalho//logs' + f'{data_arq}.txt')
    logzero.logger.info('Os arquivos foram de fato movidos')


def envia_email():
    message = 'Hey TI, \nI copy the files to the destiny and created the log file.'

    msg = MIMEMultipart()
    msg['From'] = 'fromemail@email.com'
    msg['To'] = 'toemail@email.com'
    msg['Subject'] = '[LOG] - Arquivos de Nota'
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP_SSL('172.217.192.108', 465)
        server.login(msg['From'], 'senhadoemail')
        server.sendmail(msg['From'], msg['To'], msg.as_string())
    except smtplib.SMTPException:
        print('Houve um erro ao conectar com o servidor SMTP')
    server.quit()


mover(path, dst)
cria_log()
envia_email()

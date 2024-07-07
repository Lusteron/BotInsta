import webbrowser
import pyautogui
from time import sleep

# Abrir o Instagram em uma nova aba do navegador
webbrowser.open_new_tab('https://www.instagram.com')

# Aguardar o carregamento da página
sleep(5)
pyautogui.alert(text='Iniciando o programa BotInsta!', title='BotInsta', button='Ok')
login = pyautogui.prompt(text='Telefone, nome de usuário ou email', title='BotInsta')
senha = pyautogui.password(text='Senha', title='Bot insta', mask='*')
pagina = pyautogui.prompt(text='Informe a página que deseja verificar', title='BotInsta')

# Clicar no campo de login e inserir o usuário e senha
pyautogui.click(1252, 652, duration=2)
sleep(1)
pyautogui.press('tab')
sleep(1)
pyautogui.write(login)
pyautogui.press('tab')
sleep(1)
pyautogui.write(senha)
sleep(1)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')

# Aguardar o carregamento da página após o login
sleep(5)

# Realizar a busca por 'nike'
pyautogui.click(119,287, duration=2)
sleep(2)
pyautogui.write(pagina)
sleep(2)
pyautogui.press('tab')
sleep(2)
pyautogui.press('tab')
pyautogui.press('enter')
sleep(2)

# Clicar na primeira postagem após a busca
pyautogui.click(774, 772, duration=2)
sleep(5)

while True:
    try:
        pyautogui.locateCenterOnScreen('coracao.png')
        pyautogui.click(1873,124, duration=2)
        sleep(2)
        pyautogui.click(154,1003, duration=2)
        sleep(2)
        sair = pyautogui.locateCenterOnScreen('sair.png')
        pyautogui.click(sair, duration=2)
        pyautogui.alert(text='A última publicação ja foi curtida!', title='BotInsta')
        pyautogui.alert(text='Próxima análise será feita em 24 horas!', title='BotInsta')
        pyautogui.alert(text='Programa encerrado!', title='BotInsta')
        sleep(86400)
    except:
        coracao_vazio = pyautogui.locateCenterOnScreen('coracaovazio.png')
        sleep(2)
        pyautogui.click(coracao_vazio, duration=2)
        sleep(2)
        pyautogui.click(1223,989, duration=2)
        sleep(2)
        pyautogui.write('top')
        sleep(2)
        pyautogui.press('enter')
        sleep(2)
        pyautogui.click(1873,124, duration=2)
        sleep(2)
        pyautogui.click(154,1003, duration=2)
        sleep(2)
        sair = pyautogui.locateCenterOnScreen('sair.png')
        pyautogui.click(sair, duration=2)
        pyautogui.alert(text='A última publicação acabou de ser curtida!', title='BotInsta')
        pyautogui.alert(text='Próxima análise será feita em 24 horas!', title='BotInsta')
        pyautogui.alert(text='Programa encerrado!', title='BotInsta')
        sleep(86400)
        
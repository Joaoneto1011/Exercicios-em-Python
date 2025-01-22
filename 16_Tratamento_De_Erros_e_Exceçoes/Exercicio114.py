#crie um codigo em python que teste se o site Kabum esta acessivel pelo computador usado.


import urllib
import urllib.error
import urllib.request


def verificar_site(url):
    """
    Testa se o site esta acessivel.
    :parametro url: URL do site a ser verificado
    """
    try:
        urllib.request.urlopen(url, timeout= 5)

    except urllib.error.URLError as e:
        print(f'O site {url} nao esta acessivel no momento. ')
        print(f'Motivo: {e.reason}') #mostra o motivo do erro
    else:
        print(f'Consegui acessar o site {url} com sucesso!')


url = 'https://www.kabum.com.br/?awc=17729_1737384352_630d720311b407d3f0236366621dbc7d&utm_source=AWIN&utm_medium=AFILIADOS&utm_campaign=fevereiro24&utm_content=gx1-br-awin-kabum-sd-vfbm&utm_term=141629'

verificar_site(url)
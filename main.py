import os

from pytubefix import *

while True:

    while True:
        yt = YouTube(input('Digite ou cole o link aqui: '))
        print(yt.title)  # imprime o título do vídeo
        print((yt.thumbnail_url))  # url da thumbnail

        print('É esse o vídeo solicitado? Digite 1 para Sim e 2 para Não: ')
        opcao = int(input())

        if(opcao == 1):
            break
        else:
            print()
            print('Vamos tentar novamente')

    print('Digite 1 para baixar o vídeo ou 2 para baixar o áudio (MP3): ')
    videoOuAudio = int(input())

    # Obter o caminho da área de trabalho
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    if videoOuAudio == 1:
        stream = yt.streams.get_highest_resolution()  # Melhor resolução
        stream.download(output_path=desktop_path)
        print('Download do vídeo concluído.')
    elif videoOuAudio == 2:
        audio = yt.streams.get_audio_only()
        audio.download(output_path=desktop_path)
        print('Download do áudio concluído.')
    else:
        print('Opção inválida, tente novamente.')

    os.system('cls' if os.name == 'nt' else 'clear')

    print('Baixar outro vídeo? Se sim, digite 1')
    repetir = int(input())

    if repetir !=1:
        print('Programa finalizado')
        break

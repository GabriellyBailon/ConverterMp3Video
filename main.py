import os
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip

from pytubefix import *

def baixarAudio(youtube):
    audio = youtube.streams.filter(only_audio=True).first()
    downloaded_file = audio.download(output_path=desktop_path)

    # Converter para MP3
    base, ext = os.path.splitext(downloaded_file)
    mp3_file = base + '.mp3'
    
    # Usando MoviePy para conversão
    audio_clip = AudioFileClip(downloaded_file)
    audio_clip.write_audiofile(mp3_file)
    audio_clip.close()

    os.remove(downloaded_file)

    return audio_clip

def baixarVideoNaoHD(yt, desktop_path):
    stream = yt.streams.get_highest_resolution()  # Melhor resolução
    stream.download(output_path=desktop_path)
    print('Download do vídeo concluído.')

def baixarVideoQualidadeAlta(yt, desktop_path):
     # Selecionar o stream de vídeo com a maior resolução
    video_stream = yt.streams.filter(adaptive=True, file_extension="mp4", only_video=True).order_by("resolution").desc()[2]
    
    # Selecionar o stream de áudio de melhor qualidade
    audio_stream = yt.streams.filter(adaptive=True, file_extension="mp4", only_audio=True).order_by("abr").desc().first()

    # Baixar vídeo
    video_file = video_stream.download(desktop_path)
    print(f"Vídeo baixado: {video_file}")

    # Baixar áudio
    audio_file = audio_stream.download(desktop_path)
    print(f"Áudio baixado: {audio_file}")

    # Combinar vídeo e áudio
    video_clip = VideoFileClip(video_file)
    audio_clip = AudioFileClip(audio_file)

    # Salvar o vídeo final com áudio
    final_file = os.path.join(desktop_path, yt.title.replace(" ", "_") + ".mp4")
    video_clip.with_audio(audio_clip).write_videofile(final_file, codec="libx264", audio_codec="aac")

    # Fechar os clipes
    video_clip.close()
    audio_clip.close()

    # Remover arquivos temporários (opcional)
    os.remove(video_file)
    os.remove(audio_file)

    print(f"Vídeo combinado e salvo como: {final_file}")

while True:

    while True:
        url = input('Digite ou cole o link aqui: ')
        yt = YouTube(url)
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
        print('[1] Qualidade média [2] Melhor qualidade (mais demorado): ')
        opcaoQualidadeVideo = int(input())

        if opcaoQualidadeVideo == 1:
            baixarVideoNaoHD(yt, desktop_path)
        elif opcaoQualidadeVideo == 2:
            baixarVideoQualidadeAlta(yt, desktop_path)
        else:
            print('Opção inválida, tente novamente.')

    elif videoOuAudio == 2:
        _ = baixarAudio(youtube= yt)
    else:
        print('Opção inválida, tente novamente.')

    os.system('cls' if os.name == 'nt' else 'clear')

    print('Download concluído com sucesso!')
    print('Local do arquivo: ', desktop_path)
    print('Baixar outro vídeo? Se sim, digite 1')
    repetir = int(input())

    if repetir !=1:
        print('Programa finalizado')
        break

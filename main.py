import platform

def identificar_so():
    sistema = platform.system()
    release = platform.release()
    
    # ids = [distro["ID"]]

    if 'Windows' in sistema:
        print(f'Sistema Operacional: {sistema}')
        print(f'Release: {release}')
    elif 'Linux' in sistema:
        distro = platform.freedesktop_os_release()
        print(distro['NAME'], distro['VERSION'])
    else:
        print(f'Sistema Operacional não reconhecido: {sistema}')

identificar_so()
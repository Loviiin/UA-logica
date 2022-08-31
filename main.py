def le_numeros():
    global x
    global y
    global z
    x = float(input("coloque o primeiro numero aqui:"))
    y = float(input("coloque o segundo numero aqui:"))
    z = float(input("coloque o terceiro numero aqui:"))
    print("os números digitados são:")
    print(x, y, z)


def calcula_soma():
    global soma
    soma = (x + y + z)
    print("a soma dos resultados é:")
    print(soma)


def calcula_media():
    global media
    media = (soma / 3)
    print("a media dos números é")
    print(media)

def main():
    le_numeros()
    calcula_soma()
    calcula_media()
main()

from processador_de_imagem_ptbr.utilidades import io, plot
from processador_de_imagem_ptbr.processador import combinacao, transformacao

# Lendo e retornando os plots das imagens:

# Lendo as imagens
imagem1 = io.ler_imagem(
    'C:/Users/PICHAU/Documents/Gabriel/Git/pacote-processador-de-imagem-ptbr/exemplos_aplicados_pimbr/drink.jpeg')

imagem2 = io.ler_imagem(
    'C:/Users/PICHAU/Documents/Gabriel/Git/pacote-processador-de-imagem-ptbr/exemplos_aplicados_pimbr/fire.jpeg')
    

# Plotando:
plot.plot_imagem(imagem1)
plot.plot_imagem(imagem2)


# Retornando a diferenca entre as imagens e plotando a diferenca
imagem_resultante = combinacao.achar_diferenca(imagem1, imagem2)
plot.plot_resultado(imagem1, imagem2, imagem_resultante)


# Retorna o match entre as duas imagens
histograma_resultante = combinacao.transferir_histograma(imagem1, imagem2)
plot.plot_resultado(imagem1, imagem2, histograma_resultante)


# Embassando a imagem
tranformacao = transformacao.redimensionar_imagem(histograma_resultante, 0.1)
plot.plot_resultado(histograma_resultante, tranformacao)

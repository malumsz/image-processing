<div align="center">

# Processamento Básico de Imagens 📷
Aplicativo em ***python*** para um sistema de manipulação e processamento de imagens na disciplina de *Computação Gráfica*.

[![Image Processing](https://img.shields.io/badge/Image_Processing-APP-purple.svg?logo=photon&logoColor=f5f5f5&style=for-the-badge)](PDF.pdf)

</div>

---

## Requisitos ⚙️

- ***Python***;
- biblioteca `Pillow`;
- biblioteca do `pyqt`.

## Uso 🛠

1. Utilize o arquivo `app/app.py` para abertura do menu do aplicativo.

## Construção 📄

### Processamento de Cores: Separação de Canais R, G e B
- Ao clicar no botão *"Separar RGB"*, a imagem carregada é processada para separar os canais de cores vermelho (R), verde (G) e azul (B).
- Utiliza-se o método `getpixel()` para obter os valores de intensidade de cada canal para cada pixel da imagem.
- A imagem é dividida em três imagens distintas, uma para cada canal de cor.
- A imagem de cada canal é então exibida separadamente.

### Conversão de Colorido RGB para Tons de Cinza
- Ao clicar no botão *"Grayscale"*, a imagem carregada é convertida para tons de cinza.
- Utiliza-se o método `convert()` da biblioteca *Pillow* para converter a imagem para tons de cinza.
- A imagem em tons de cinza é então exibida.

### Conversão de Tons de Cinza para Preto e Branco (Limiarização/Binarização Manual)
- Ao clicar no botão *"Binário"*, a imagem em tons de cinza é binarizada manualmente com base em um limiar pré-definido.
- Utiliza-se o método `getpixel()` para obter os valores de intensidade de cada pixel da imagem em tons de cinza.
- Cada pixel é então convertido para preto ou branco dependendo se sua intensidade é maior ou igual ao limiar.
- A imagem binarizada é então exibida.

### Filtros da Média
- Ao clicar no botão *"Média"*, é aplicado um filtro da média na imagem carregada.
- O filtro da média é aplicado através de uma máscara 3x3, onde cada pixel é substituído pela média dos valores dos pixels vizinhos.
- A nova imagem filtrada é então exibida.

### Filtro da Mediana
- Ao clicar no botão *"Mediana"*, é aplicado um filtro da mediana na imagem carregada.
- O filtro da mediana é aplicado através de uma máscara 3x3, onde cada pixel é substituído pelo valor mediano dos pixels vizinhos.
- A nova imagem filtrada é então exibida.

### Girar a Imagem 90 Graus
- Ao clicar no botão *"Girar em 90º"*, a imagem é rotacionada em 90 graus no sentido horário.
- Utiliza-se o método `transpose()` da biblioteca *Pillow* para realizar a rotação.
- A nova imagem rotacionada é então exibida.

### Inverter a Imagem (Horizontal/Vertical)
- Ao clicar no botão *"Inverter imagem horizontalmente"* ou *"Inverter imagem verticalmente"*, a imagem é invertida horizontal ou verticalmente, respectivamente.
- Utiliza-se o método `transpose()` da biblioteca *Pillow* para realizar a inversão horizontal ou vertical.
- A nova imagem invertida é então exibida.

#

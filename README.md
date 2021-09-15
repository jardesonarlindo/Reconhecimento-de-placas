Passo 1: Instalar Raspbian no Raspberry Pi
Passo 2: Inserir na USB a WebCam
Passo 3: Abrir terminal e digitar os seguintes comandos
sudo apt-get update
sudo apt-get upgrade
sudo apt-get update && sudo apt-get install -y openalpr openalpr-daemon openalpr-utils libopenalpr-dev
sudo apt-get update
sudo apt-get -y install fbi
Passo 4: Clonar o projeto do github em /home/pi
Passo 5: Criar uma pasta em /home/pi chamada “webcan”
Passo 6: 
Clonar o seguinte repositório: GitHub - tesseract-ocr/tessdata: Trained models with support for legacy and LSTM OCR engine
Copiar para a pasta: /usr/share/openalpr/runtime_data/ocr/tessdata

Passo 7: Executar o seguinte comando - 
sudo cp -a /home/pi/tessdata-main/* /usr/share/openalpr/runtime_data/ocr/tessdata
Passo 8: No terminal ir até o diretório /home/pi
Passo 9: Executar o comando python Cod.py
Passo 10: Digite a versão da placa desejada (No vídeo apresentação foi utilizada placas dos USA, no caso digitar “us”)
Passo 11: Apontar a câmera para a placa desejada, o programa ficará em loop tirando fotos e exibindo os resultados.



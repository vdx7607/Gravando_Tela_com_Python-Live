# importações
import pyautogui
import cv2
import numpy as np

# Resolução da tela a ser gravada
resolution = (1920, 1080)

# Especificação do codec de vídeo para 4bytes
codec = cv2.VideoWriter_fourcc(*"XVID")

# Nome de saída/destino
filename = "Recording.avi"

# frames rate.
fps = 60.0


# Criando gravação
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Criar Janela Live em Branco
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Redimensionar Janela Live
cv2.resizeWindow("Live", 480, 270)

while True:
	# Fazer captura de tela
	img = pyautogui.screenshot()

	# Converter captura de tela para numpy array
	frame = np.array(img)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# gravar no frame
	out.write(frame)
	
	# Adcional: Mostrar tela Live de gravação
	cv2.imshow('Live', frame)
	
	# Comando para parar gravação
	if cv2.waitKey(1) == ord('q'):
		break

# Fechar gravador de vídeo
out.release()

# Fechar todas instancias
cv2.destroyAllWindows()

import cv2

''' Um vídeo é representado como uma sequência de quadros,cada quadro possui pixels e canais 
de cor, enquanto o fps indica quantos quadros são exibidos por segundo.'''

cap = cv2.VideoCapture("video.mp4")

# Verifica se o vídeo foi aberto corretamente
if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

quadros = []

while True:
    ret, quadro = cap.read()

    # o vídeo chegou ao fim
    if not ret:
        break

    quadros.append(quadro)

cap.release()

meio = len(quadros) // 2

cv2.imwrite("frame_meio.jpg", quadros[meio])

print("Total de quadros:", len(quadros))
print("Quadro do meio salvo em: frame_meio.jpg")
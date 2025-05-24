
import cv2

def capturar_com_camera():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Não foi possível acessar a câmera.")
        return

    print("Pressione 's' para salvar uma imagem ou 'q' para sair.")
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        cv2.imshow("Captura de Câmera", frame)
        k = cv2.waitKey(1)
        if k == ord('s' or 'S'):
            cv2.imwrite("captura.jpg", frame)
            print("Imagem capturada e salva como 'captura.jpg'")
        elif k == ord('q' or 'Q'):
            break

    cam.release()
    cv2.destroyAllWindows()

capturar_com_camera()

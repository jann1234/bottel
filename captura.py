import pyautogui
# Capturar pantalla.
screenshot = pyautogui.screenshot(region=(50, 50, 400, 300))
# Guardar imagen.
screenshot.save("screenshot.png")
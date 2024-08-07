import PySimpleGUI as sg

def create_window():
    # Definir el diseño de la ventana
    layout = [
        [sg.Text("Welcome to the Selenium Automation Tool")],
        [sg.Button("Run Selenium Script", size=(20, 2))]
    ]

    return sg.Window("Selenium Script", layout, element_justification='center', finalize=True)
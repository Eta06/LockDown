import PySimpleGUI as sg


layout = [[
    sg.Text("Merhaba")
]]

window = sg.Window(title="Deneme uygulaması", layout=layout, keep_on_top=True, resizable=False,finalize=True)
window.Maximize()
while True:
    values, event = window.read()
    print(values)
    print(event)
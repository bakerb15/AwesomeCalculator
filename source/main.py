from calculator_mvc import CalculatorView, CalculatorController, CalculatorModel
import PySimpleGUI as sg

def main():
    model = CalculatorModel()
    view = CalculatorView()
    controller = CalculatorController()
    sg.theme(view.theme)
    window = sg.Window('Awesome Calculator', view.layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        if controller.process(window, model) is False: # the user clicked the cancel button
            break
    window.close()


if __name__== "__main__":
    main()
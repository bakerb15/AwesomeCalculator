from calculator_mvc import CalculatorView, CalculatorController, CalculatorModel
import PySimpleGUI as sg
import math

def two_pi(model):
    model.calculation += str(2*math.pi)

def main():
    
    model = CalculatorModel()
    view = CalculatorView()
    controller = CalculatorController()

    #add a custom button with a stored procedure
    tp = '2pi'
    view.custom_row.append(sg.Button(tp))
    controller.stored_precedures[tp] = two_pi

    sg.theme(view.theme)
    window = sg.Window('Awesome Calculator', view.layout)
    while True:
        if controller.process(window, model) is False: # the user clicked the cancel button
            break
    window.close()


if __name__== "__main__":
    main()
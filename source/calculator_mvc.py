import PySimpleGUI as sg


class CalculatorView(object):

    def __init__(self, *args, **kwargs):
        self.theme = 'DarkTanBlue'
        self.layout = \
            [[sg.InputText(key='_CALCINPUT_')],
                [sg.Button(str(x), key=str(x)) for x in range(7, 10)],
                [sg.Button(str(x), key=str(x)) for x in range(4, 7)],
                [sg.Button(str(x), key=str(x)) for x in range(1, 4)],
                [sg.Button('0'), sg.Button('+'), sg.Button('-')],
                [sg.Button('*'), sg.Button('/'), sg.Button('.')],
                [sg.Button('('), sg.Button(')'), sg.Button('Clear')],
                [sg.Button('='), sg.Button('Cancel')]]


class CalculatorModel(object):

    def __init__(self, *args, **kwargs):
        self.calculation = ""
        self.history = []

    def add_to_history(self, formula, result):
        self.history.append((formula, result))


class CalculatorController(object):

    def __init__(self, *args, **kwargs):
        pass

    def process(self, window, model):
        event, values = window.read()
        if event in (None, 'Cancel'):	# if user closes window or clicks cancel
            return False
        calc_input =  window['_CALCINPUT_']
        model.calculation = values['_CALCINPUT_']
        if event == '=':
            try:
                result = eval(model.calculation)
                model.add_to_history(model.calculation, result)
                model.calculation = result
            except:
                model.calculation = 'ERROR :('
        elif event == 'Clear':
            model.calculation = ''
        else:
            model.calculation = values['_CALCINPUT_'] + event
        calc_input.update(value=model.calculation)
        return True
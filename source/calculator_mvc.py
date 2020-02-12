import PySimpleGUI as sg


class CalculatorView(object):
    """
        Objects of this class keep track of
        the theme and layout that are passed to
        PysimpleGui Window.
    """

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
                [],
                [sg.Button('='), sg.Button('Cancel')]]
        self.custom_row = self.layout[7] # reference to the row in the layout that can handle more buttons


class CalculatorModel(object):
    """ the user's arithmetic expression
    will be stored as a string in the calculation member 
    If a valid expression is executed the result
    will overwrite the calculations string.

    history will contain a list of tuples containing
    expression, result
    """

    def __init__(self, *args, **kwargs):
        self.calculation = "" 
        self.history = []

    def add_to_history(self, formula, result):
        self.history.append((formula, result))


class CalculatorController(object):

    def __init__(self, *args, **kwargs):
        self.stored_precedures = {} # Maps an event to a function 

    def process(self, window, model):
        """ Catches button clicks from the window.
        If the user presses the '=' this method
        will attempt to use python's eval method
        to execute the expression dispalyed in the
        calculators text box. If the calculation
        is invalid eval will throw an exception,
        which results in an error message being 
        displayed to the user.
        """
        event, values = window.read()
        if event in (None, 'Cancel'):	# closing window or clicking cancel returns False
            return False
        calc_input =  window['_CALCINPUT_']
        model.calculation = values['_CALCINPUT_']
        if event in self.stored_precedures:
            self.stored_precedures[event](model)
            calc_input.update(value=model.calculation)
        else:
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
        return True # The model and view have been updated
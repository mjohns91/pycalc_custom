import tkinter as tk
from calculator import SafeEvaluator

class CalculatorApp:
    def __init__(self, root):
        self.calc = SafeEvaluator()
        self.expression = ""
        self.input_text = tk.StringVar()
        self.result_text = tk.StringVar()

        self.build_gui(root)

    def build_gui(self, root):
        root.title("Calculator")
        root.geometry("400x400")

        result_frame = tk.Frame(root)
        result_frame.pack()

        input_frame = tk.Frame(root)
        input_frame.pack()

        button_frame = tk.Frame(root)
        button_frame.pack()

        result_field = tk.Entry(result_frame, textvariable=self.result_text, font=("arial", 20), justify='right')
        result_field.grid(row=0, column=0, columnspan=4)

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('arial', 18), bd=5, justify='right')
        input_field.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
        ]

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                btn = tk.Button(button_frame, text=char, width=6, height=2, font=('arial', 18),
                                command=lambda ch=char: self.on_button_click(ch))
                btn.grid(row=r+1, column=c)

    def on_button_click(self, char):
        if char == '=':
            result = self.calc.evaluate(self.expression)
            self.result_text.set(result)
            self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

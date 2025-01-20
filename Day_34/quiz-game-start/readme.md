bug in the line:
    self.text = self.canvas.create_text(150, 125, text='demo', font=FONT)
    # cannot use positional arguments for x and y coordinates, as it raises IndexError: tuple index out of range
        self.text = self.canvas.create_text(x=150, y=125, text='demo', font=FONT)



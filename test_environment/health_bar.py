import tkinter as tkin

class health:
    """Class for health bar creation and health tracking."""

    def __init__(self, master,
                 bg_cnf={"width": 60, "height": 26, "bg":"#654321"},
                 fg_cnf={},
                 health_max=100,
                 x=0, y=5, relx=0, rely=0, **kw):
        """Create health bar and assign default values."""
        # Create background frame
        self.bg = tkin.Frame(master, bg_cnf)

        # Assign default size
        self.default_bg_width = int(self.bg['width'])
        self.default_bg_height = int(self.bg['height'])
        self.bg.place(anchor='sw', x=x, y=y, relx=relx, rely=rely)

        # Create foreground frame
        self.bar = tkin.Frame(self.bg, fg_cnf)

        # Assign default size
        self.bar['width'] = self.default_bg_width - 10
        self.bar['height'] = self.default_bg_height - 10
        self.default_bar_width = int(self.bar['width'])
        self.default_bar_height = int(self.bar['height'])

        # Assign default values
        self.value_max: int = health_max
        self.value = 100


    def __repr__(self):
        return str(self.value)


    def __setattr__(self, name, value):
        if name == 'value':
            self.__dict__[name] = value
            self.update()
        else:
            object.__setattr__(self, name, value)


    def __add__(self, other):
        return self.value + other


    def __get__(self, instance, value):
        return self.__dict__['value']


    def __set__(self, instance, value):
        self.__dict__['value'] = value
        self.update()


    def update(self, *args):
        """Update values and foreground frame width."""
        # Get percentages
        self.value_percent = self.value / self.value_max
        _health_width = round(self.value_percent * self.default_bar_width)

        # Assign new width
        self.bar['width'] = _health_width

        if self.value <= 0:
            self.bar.place_forget()
        else:
            self.bar.place(anchor='w', x=5, rely=0.5)


# Code for running this specific file
if __name__ == '__main__':

    # Root creation
    root = tkin.Tk()
    root.title("Health bar Prototype")
    root.geometry("1600x900")
    root.minsize(1024, 576)

    # Set root properties
    root['bg'] = '#2e2e2e'

    # Create entity
    entity = tkin.Frame(root, width=80, height=100, bg='#ff6961')
    entity.place(anchor='sw', relx=0.5, rely=0.5)

    # Define arguments
    _fg_args = {"bg":"#dd3a2a"}
    _args = {'fg_cnf':_fg_args,
             'x':40, 'y':5,
             'relx':0.5, 'rely':0.5}

    # Initialize health bar
    HEALTH = health(root, **_args)

    def raise_health():
        if HEALTH.value < HEALTH.value_max:
            _updated_health = HEALTH.value + 2
            HEALTH.value = _updated_health
        else:
            pass

    def lower_health():
        if HEALTH.value > 0:
            _updated_health = HEALTH.value - 2
            HEALTH.value = _updated_health
        else:
            pass

    _lower_health = tkin.Button(root,
                                text='Lower Health',
                                command=lower_health)
    _lower_health.place(x=0, y=25)


    _raise_health = tkin.Button(root,
                                text='Raise Health',
                                command=raise_health)
    _raise_health.place(x=00, y=0)
                                                                                # INITIALIZE ROOT #
    root.mainloop()

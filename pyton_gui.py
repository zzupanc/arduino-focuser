import tkinter as tk
from tkinter import ttk
import serial


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        self.setup_widgets()

    def setup_widgets(self):
        # Create a Frame for input widgets
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(
            row=0, column=1, padx=100, pady=(40, 10), sticky="nsew", rowspan=3
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)

        # Button 1
        self.button_zoom1 = ttk.Button(self.widgets_frame, text="Focus +")
        self.button_zoom1.grid(row=6, column=0, padx=5, pady=20, sticky="nsew")

        # Button 2
        self.button_zoom2 = ttk.Button(self.widgets_frame, text="Focus -")
        self.button_zoom2.grid(row=7, column=0, padx=5, pady=20, sticky="nsew")

        # Switch
        self.switch_var = tk.BooleanVar()
        self.switch = ttk.Checkbutton(
            self.widgets_frame,
            text="Speed toggle",
            style="Switch.TCheckbutton",
            variable=self.switch_var,
        )
        self.switch.grid(row=9, column=0, padx=5, pady=10, sticky="nsew")

        # Initialize the serial connection
        self.serial_port = serial.Serial("COM3", 9600)  # Adjust the port accordingly

        # Bind events
        self.button_zoom1.bind("<ButtonPress-1>", lambda event: self.on_button_press1())
        self.button_zoom1.bind(
            "<ButtonRelease-1>", lambda event: self.on_button_release()
        )

        self.button_zoom2.bind("<ButtonPress-1>", lambda event: self.on_button_press2())
        self.button_zoom2.bind(
            "<ButtonRelease-1>", lambda event: self.on_button_release()
        )

        self.switch.bind("<ButtonPress-1>", self.switch_state)

    def on_button_press1(self):
        switch_state = self.switch_var.get()
        if switch_state:
            # If the switch is True (checked), send command based on button pressed
            print(f"Switch is ON. Button pressed! Sending command: A")
            self.send_command("A")
        else:
            # If the switch is False (unchecked), always send 'A' command
            print(f"Switch is OFF. Button pressed! Sending command: C")
            self.send_command("C")

    def on_button_press2(self):
        switch_state = self.switch_var.get()
        if switch_state:
            # If the switch is True (checked), send command based on button pressed
            print(f"Switch is ON. Button pressed! Sending command: B")
            self.send_command("B")
        else:
            # If the switch is False (unchecked), always send 'A' command
            print(f"Switch is OFF. Button pressed! Sending command: D")
            self.send_command("D")

    def on_button_release(self):
        print(f"Button released! Sending command: STOP")
        # Send the command to Arduino
        self.send_command("E")

    def send_command(self, command):
        self.serial_port.write(command.encode())

    def switch_state(self, event):
        switch_state = self.switch_var.get()
        print("Switch state:", switch_state)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Arduino Focuser - GUI")
    root.iconbitmap("icon.ico")

    # Simply set the theme
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "./dark")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(300, 300)
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

    root.mainloop()

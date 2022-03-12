class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    """ 
        Using a custom context manager:
        __enter__ runs as the start of a with statement
        __exit__ runs upon exit for the with statement
    """
    def __enter__(self):
        print('start')
        self.connected = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('end')
        self.connected = False
        return

    @classmethod
    def __str__(cls):
        return f"Device {cls.__name__}"

    def disconnect(self):
        self.connected = False
        print("Disconnected")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages}) pages remaining"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return None

        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


if __name__ == '__main__':
    # Instantiate object
    printer = Printer("Printer", "USB", 500)

    # Print some pages
    print(printer.remaining_pages)
    print(printer.print(50))
    print(printer.remaining_pages)

    # Disconnect - can't print any more
    printer.disconnect()
    print(printer.print(50))

    # Print using with statement - thanks to __enter__ and __exit__ methods
    with Printer('James', 'USB', 500) as p:
        print(p.print(50))

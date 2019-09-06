from gpiozero import LED

red = LED(17)
green = LED(17)
yellow = LED(17)


def off():
    """ Changes all leds to off
        Args:
        Returns:
        """
    print('LED OFF')
    red.off()
    yellow.off()
    green.off()

    return


def red():
    """ Changes red led to on
        Args:
        Returns:
        """
    print('LED RED')
    red.on()

    return


def yellow():
    """ Changes yellow led to on
        Args:
        Returns:
        """
    print('LED YELLOW')
    yellow.on()
    return


def green():
    """ Changes green led to on
       Args:
       Returns:
       """
    print('LED GREEN')
    green.on()

    return

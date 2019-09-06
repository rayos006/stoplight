from gpiozero import LED

led_red = LED(17)
led_green = LED(22)
led_yellow = LED(27)


def off():
    """ Changes all leds to off
        Args:
        Returns:
        """
    print('LED OFF')
    led_red.off()
    led_yellow.off()
    led_green.off()

    return


def red():
    """ Changes red led to on
        Args:
        Returns:
        """
    print('LED RED')
    led_yellow.off()
    led_green.off()
    led_red.on()

    return


def yellow():
    """ Changes yellow led to on
        Args:
        Returns:
        """
    print('LED YELLOW')
    led_green.off()
    led_red.off()
    led_yellow.on()
    return


def green():
    """ Changes green led to on
       Args:
       Returns:
       """
    print('LED GREEN')
    led_red.off()
    led_yellow.off()
    led_green.on()

    return

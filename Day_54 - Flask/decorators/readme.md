# decorator expects <new> from view function: read documentation
-> it expects func to return some kind of output - pre set

# equivalent to sugar syntax @delay_decorator on say_bye function
bye_decorator = delay_decorator(say_bye)
bye_decorator()
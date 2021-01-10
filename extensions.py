class Bot_exception(BaseException):
    pass


class Converter:
    @staticmethod
    def get_price(user_input):
        if len(user_input) !=3:
            raise Bot_exception
        base, quote, ammount = user_input
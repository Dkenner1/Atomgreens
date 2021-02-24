from unpacker import SerialMsg


if __name__ == '__main__':
    x = SerialMsg(72)
    x.interpret(68)

    print(x.msg)

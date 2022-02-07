class Encryptor():
    def __init__(self, name):
        self.encryption_types = ["ascii"]
        self.name = name

    def ascii_converter(self, message):
        ascii_list = []
        for i in message:
            ascii_num = ord(i)
            ascii_list.append(ascii_num)
        return ascii_list

    def run(self):
        user_input = input("Enter a message to encrypt🥳")
        ascii_list = self.ascii_converter(user_input)
        print(self.encrypt(ascii_list))

    def encrypt(self, ascii_list):
        modified_ascii_list = ""
        for i, num in enumerate(ascii_list):
            modified = num + 0
            modified_str = str(modified)
            modified_ascii_list += modified_str
        return modified_ascii_list
            



    def hello(self):
        print(f"Hello🥳🤩🥳🤩🥳🤩🥳🤩🥳🤩🥳🤩🥳🤩🥳🤩, {self.name}")


encryptor = Encryptor("Derek")
encryptor.run()
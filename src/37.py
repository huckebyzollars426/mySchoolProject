class MyClass:
    def __init__(self):
        self.data = []

    def add_data(self, data):
        self.data.append(data)

    def get_data(self):
        return self.data

if __name__ == "__main__":
    # Example usage
    example_data = [1, 2, 3]
    my_class = MyClass()
    my_class.add_data(example_data)
    print("Data:", my_class.get_data())

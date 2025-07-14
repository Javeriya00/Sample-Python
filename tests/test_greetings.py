from greetings import say_hello, say_goodbye

def test_say_hello():
    assert say_hello("Alice") == "Hello, Alice!"

def test_say_goodbye():
    assert say_goodbye("Bob") == "Goodbye, Bob!"

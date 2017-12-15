# code to xml
def to_xmltag(fn):
    def func(*args):
        return '<' + fn(*args) + '/>'
    return func


@to_xmltag
def input_name(name):
    return name

if __name__ == '__main__':
    print(input_name("hello"))

## OUTPUTS: <hello/>

def surround_tag(tag):
    def decorator(fn):
        def func(*args, **kwargs):
            return '<' + tag + '>' + fn(*args, **kwargs) + '</' + tag + '>'
        return func
    return decorator


@surround_tag('p')
def say_hi(name):
    return 'Hi~, ' + name;

print(say_hi('심청이'))

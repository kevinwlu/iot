# https://github.com/defunkt/pystache
import pystache
print(pystache.render('Hi {{person}}!', {'person': 'Mom'}))

class SayHello(object):
    def to(self):
        return "Pizza"

hello = SayHello()
renderer = pystache.Renderer()
print(renderer.render(hello))

parsed = pystache.parse(u"Hey {{#who}}{{.}}!{{/who}}")
print(parsed)
print(renderer.render(parsed, {'who': 'Pops'}))
print(renderer.render(parsed, {'who': 'you'}))

# This gets only ever called once, and therefore makes sure the 'registry' code is 
# also only executed one time per session
import registry

# Here we can work with the registed code
registry.register('my name')
for name in registry.registered_names():
    print(name)
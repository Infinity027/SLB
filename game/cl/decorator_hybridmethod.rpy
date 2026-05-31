
init -500 python:



    class hybridmethod(object):
        """
    hybridmethod is a decorator that allows to define both class and
    instance methods with the same name.

    Class methods should be decorated with `@hybridmethod` and instance
    methods with `@<class method name>.instancemethod`:

        class A(object):
            @hybridmethod
            def method_name(cls, *args):
                ''' class method. '''
                pass

            @method_name.instancemethod
            def method_name(self, *args):
                ''' instance method. '''
                pass
    """
        
        def __init__(self, fclass=None, finstance=None, doc=None):
            self.fclass = fclass
            self.finstance = finstance
            if doc is None and fclass is not None:
                doc = fclass.__doc__
            self.__doc__ = doc
        
        def classmethod(self, fclass):
            return type(self)(fclass, self.finstance, self.__doc__)
        
        def instancemethod(self, finstance):
            return type(self)(self.fclass, finstance, self.__doc__)
        
        def __get__(self, instance, cls):
            if instance is not None:
                if self.finstance is None:
                    raise AttributeError("can't call this method on an instance")
                return self.finstance.__get__(instance, cls)
            if self.fclass is None:
                raise AttributeError("can't call this method on a class")
            return self.fclass.__get__(cls, None)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

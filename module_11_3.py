def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]
    obj_module = obj.__module__
    other_properties = {}
    if isinstance(obj, type):
        other_properties['base_classes'] = [base.__name__ for base in obj.__bases__]
    if hasattr(obj, '__dict__'):
        other_properties['attributes'] = obj.__dict__

    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': obj_module,
            'other_properties': other_properties}

    return info


if __name__ == "__main__":
    class Sample:
        def __init__(self):
            self.attr1 = "value1"
            self.attr2 = "value2"

        def method1(self):
            pass

        def method2(self):
            pass


    sample_obj = Sample()
    result = introspection_info(sample_obj)
    print(result)

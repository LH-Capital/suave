from marshmallow import Schema


class Base(object):

    @classmethod
    def create(cls, **kwargs):
        data = {}
        for k, v in kwargs.items():
            if hasattr(cls, k):
                data[k] = v
        return cls(**data)


class BaseSchema(Schema):

    @staticmethod
    def clean(key):
        split = key.split(' ')
        if len(split) > 2:
            return '_'.join(split[1:])
        return split[-1]

    def marshal(func):
        def _marshal(self, data, *args, **kwargs):
            res = {}
            for k, v in data.items():
                if hasattr(self, k):
                    k = BaseSchema.clean(k)
                    res[k] = v
            return func(self, res, *args, **kwargs)
        return _marshal

    @marshal
    def load(self, data):
        return super(BaseSchema, self).load(data)

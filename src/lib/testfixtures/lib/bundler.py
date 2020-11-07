class FixtureBundler:
    # Fixture Bundle
    def __init__(self, *args):
        args = list(args)
        names = args.pop(-1).split()
        assert len(names)==len(args)
        for name,arg in zip(names,args):
            setattr(self, name, arg)




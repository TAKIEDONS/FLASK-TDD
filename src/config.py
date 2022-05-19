# place where Flask itself puts certain configuration values and also where extensions can put their configuration values. But this is also where you can have your own configuration.

class BaseConfig:
    TESTING = False


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    pass
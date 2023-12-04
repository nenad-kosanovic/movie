import os
class Config:
    TRACK_MODIFICATIONS = True
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
class TestingConfig(Config):
    TESTING = True
class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
class ProductionConfig(Config):
    DEBUG = False
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig
}
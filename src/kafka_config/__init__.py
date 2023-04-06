
import os


SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"
API_KEY = 'DNJ47LKX2VT3BNAN'
# API_KEY = os.getenv('DNJ47LKX2VT3BNAN',None)
# https://psrc-gn6wr.us-east-2.aws.confluent.cloud
# ENDPOINT_SCHEMA_URL  = os.getenv('https://psrc-gn6wr.us-east-2.aws.confluent.cloud',None)
ENDPOINT_SCHEMA_URL  = "https://psrc-gn6wr.us-east-2.aws.confluent.cloud"
# API_SECRET_KEY = os.getenv('sTHzWr6IcY8kYLvKTSGOEPU5A8Z0MdIZmwLfJu5oHKMfJGUzLMlnOyQURz02F1iH',None)
API_SECRET_KEY = 'sTHzWr6IcY8kYLvKTSGOEPU5A8Z0MdIZmwLfJu5oHKMfJGUzLMlnOyQURz02F1iH'
# BOOTSTRAP_SERVER = os.getenv('pkc-n00kk.us-east-1.aws.confluent.cloud:9092',None)
BOOTSTRAP_SERVER = 'pkc-n00kk.us-east-1.aws.confluent.cloud:9092'
# SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
# SCHEMA_REGISTRY_API_KEY = os.getenv('EADXGUCQLTK2X3ED',None)
SCHEMA_REGISTRY_API_KEY = 'EADXGUCQLTK2X3ED'
SCHEMA_REGISTRY_API_SECRET = 'lU2cg+IYwUEBSY2T6x+vqhTQwaK3awPaTY0U+34m+No1ksG6jtS3OQIF3wLW7r/T'
# SCHEMA_REGISTRY_API_SECRET = os.getenv('lU2cg+IYwUEBSY2T6x+vqhTQwaK3awPaTY0U+34m+No1ksG6jtS3OQIF3wLW7r/T',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()


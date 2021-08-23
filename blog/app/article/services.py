import json
import requests
from blog.settings import ARTICLE_PARSER_URL
import logging

logger = logging.getLogger(__name__)

def run_parse_site(site_name):
    ''' запрос для начала парсинга определенного ресурса '''
    r = requests.post(f"{ARTICLE_PARSER_URL}/run_parse", data=json.dumps({"spider_name": site_name, "make_import": False}))
    logger.info(f"Status code ({r.status_code}) for run parse: {site_name}")
    return r.status_code
    
def send_email(user):
    """"""
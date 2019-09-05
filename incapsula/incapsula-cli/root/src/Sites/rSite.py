import json

import Sites.rIncapRule
from Utils.executeRest import execute
from Sites.site import Site
from Utils.incapError import IncapError
import logging


def r_site(args):
    output = 'Get site status for ID = {0}'. format(args.site_id)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "tests": args.tests,
        "site_id": args.site_id
    }

    result = read(param)

    if result.get('res') != 0:
        err = IncapError(result)
        err.log()
        return err
    else:
        site = Site(result)
        site.log()
        return site


def read(params):
    resturl = '/api/prov/v1/sites/status'
    if params:
        if "site_id" in params:
            return execute(resturl, params)
        else:
            logging.warning("No site_id parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where passed in.')

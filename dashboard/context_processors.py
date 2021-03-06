from dashboard.common import db_util
from dashboard.common import utils

import logging
logger = logging.getLogger(__name__)


def last_updated(request):
    return {'last_updated': db_util.get_canvas_data_date()}


def get_git_version_info(request):
    return {'git_version': utils.get_git_version_info()}
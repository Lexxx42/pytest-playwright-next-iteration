import pytest

import config
import qase
import api


@pytest.fixture(autouse=config.qase.IS_DOC_UPDATE_NEEDED)
def update_docs(request) -> None:
    case_id_marker = request.node.get_closest_marker('case_id')
    if config.qase.TOKEN and len(case_id_marker.args) > 0:
        qase.docs.create_database(request)
    yield
    if config.qase.TOKEN and len(case_id_marker.args) > 0:
        api.qase.update_case(case_id_marker.args[0], qase.docs.read())
        qase.docs.delete_database()

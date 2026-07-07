from pycaprio.core.objects import Curation


def test_create_curation(pycaprio, test_project, test_document, test_io):
    curation = pycaprio.api.create_curation(test_project, test_document, test_io)
    assert isinstance(curation, Curation)


def test_detail_curation(pycaprio, test_project, test_document, test_io):
    pycaprio.api.create_curation(test_project, test_document, test_io)
    content = pycaprio.api.curation(test_project, test_document)
    assert content


def test_delete_curation(pycaprio, test_project, test_document, test_io):
    pycaprio.api.create_curation(test_project, test_document, test_io)
    assert pycaprio.api.delete_curation(test_project, test_document) is True

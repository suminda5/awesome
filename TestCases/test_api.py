import pytest
import requests

BASE = "http://127.0.0.1:5000/"

@pytest.mark.run(order=1)
def test_post_create():
    r = requests.post(BASE + "kvstore/myname", {"key": "myname", "value": "myvalue"})
    print(r.json())
    print(r.status_code)
    assert 201 == r.status_code
    assert r.json() == {"key": "myname", "value": "myvalue"}


@pytest.mark.run(order=2)
def test_post_record_exist():
    r = requests.post(BASE + "kvstore/myname", {"key": "myname", "value": "myvalue"})
    print(r.json())
    print(r.status_code)
    assert 409 == r.status_code


@pytest.mark.run(order=3)
def test_put_content_type():
    r = requests.put(BASE + "kvstore/myname", {"key": "myname", "value": "myvalue"})
    print(r.json())
    print(r.status_code)
    print(r.headers['Content-Type'])
    assert "application/json" == r.headers['Content-Type']


@pytest.mark.run(order=4)
def test_get_read():
    r = requests.get(BASE + "kvstore/myname")
    print(r.json())
    print(r.status_code)
    assert 200 == r.status_code


@pytest.mark.run(order=5)
def test_delete_200():
    r = requests.delete(BASE + "kvstore/myname")
    print(r.json())
    print(r.status_code)
    assert 200 == r.status_code


@pytest.mark.run(order=6)
def test_delete_404():
    r = requests.delete(BASE + "kvstore/myname")
    print(r.json())
    print(r.status_code)
    assert 404 == r.status_code

@pytest.mark.run(order=7)
def test_get_read_myname_not_exist():
    r = requests.get(BASE + "kvstore/myname")
    print(r.json())
    print(r.status_code)
    assert 404 == r.status_code
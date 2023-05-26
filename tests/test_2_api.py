from api.questions import api
from http import HTTPStatus
from utils.assertions import Assert


def test_list_users():
    responsible = api.list_users()

    assert responsible.status_code == HTTPStatus.OK
    Assert.validate_schema(responsible.json())


def test_user_not_found():
    responsible = api.single_user_not_found()

    assert responsible.status_code == HTTPStatus.NOT_FOUND
    Assert.validate_schema(responsible.json())


def test_single_user():
    responsible = api.single_user()
    responsible_body = responsible.json()

    assert responsible.status_code == HTTPStatus.OK
    Assert.validate_schema(responsible_body)

    assert responsible_body['data']['first_name'] == 'Janet'
    example = {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }
    assert example == responsible_body


def test_create():
    name = 'Cavin'
    job = 'Tester'
    responsible = api.create(name, job)

    assert responsible.status_code == HTTPStatus.CREATED
    assert responsible.json()['name'] == name
    assert responsible.json()['job'] == job
    assert api.delete_user(responsible.json()['id']).status_code == HTTPStatus.NO_CONTENT









import api_backend


def test_AllUsersInfo_get(): #All users
    results = api_backend.AllUsersInfo.get('self')
    assert type(results) == list


def test_UserInfo_get(): #Single User
    results = api_backend.UserInfo.get('self', 'Chris')
    assert type(results) == list

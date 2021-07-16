import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestUserModel:
    """
        TestUserModel : Testing user model
    """
    def test_init(self):
        user_obj = mixer.blend('auth_app.User')
        assert user_obj.id >= 1, 'should save an instance'

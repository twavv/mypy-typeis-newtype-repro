from typing import NewType

from typing_extensions import TypeIs, reveal_type


class User:
    role: str


Admin = NewType("Admin", User)


def is_admin(user: User) -> TypeIs[Admin]:
    return user.role == "admin"


def f(user: User) -> None:
    if is_admin(user):
        reveal_type(user)  # if-branch: expected Admin
    else:
        reveal_type(user)  # else-branch: expected User

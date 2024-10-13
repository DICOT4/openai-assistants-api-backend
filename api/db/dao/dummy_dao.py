from typing import List, Optional

from api.db.models.dummy_model import Dummy


class DummyDAO:
    """Class for accessing dummy table."""

    async def create_dummy_model(self, name: str) -> None:
        """
        Add single dummy to session.

        :param name: name of a dummy.
        """
        await Dummy.insert_one(Dummy(name=name))

    async def get_all_dummies(self, limit: int, offset: int) -> List[Dummy]:
        """
        Get all dummy models with limit/offset pagination.

        :param limit: limit of dummies.
        :param offset: offset of dummies.
        :return: stream of dummies.
        """
        return await Dummy.find_all(skip=offset, limit=limit).to_list()

    async def filter(self, name: Optional[str] = None) -> List[Dummy]:
        """
        Get specific dummy model.

        :param name: name of dummy instance.
        :return: dummy models.
        """
        if name is None:
            return []
        return await Dummy.find(Dummy.name == name).to_list()

    async def delete_dummy_model_by_name(
        self,
        name: str,
    ) -> Optional[Dummy]:
        """
        Delete a dummy model by name.

        :param name: name of dummy instance.
        :return: option of a dummy model.
        """
        res = await Dummy.find_one(Dummy.name == name)
        if res is None:
            return res
        await res.delete()
        return res

from classes.BaseClass import BaseClass
from Model.Task import Task as TaskModel


class Task(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False) -> TaskModel:
        return TaskModel() if new_model else TaskModel

    def _prepare_query_filter(self, query, filter_params):
        if filter_params:
            filter_params = {}

        if filter_params.get('onlyActive'):
            query = query.where(self.get_model().date_complited == None)

        if filter_params.get('onlyComplete') and not filter_params.get('onlyActive'):
            query = query.where(self.get_model().date_complited != None)

        return query

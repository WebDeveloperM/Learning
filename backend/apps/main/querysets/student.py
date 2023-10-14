from apps.main.querysets.base_queryset import BaseQuerySet


class StudentQuerySet(BaseQuerySet):

    def get_answer_statistics(self):
        query = self.filter(control__set_science="")
        return query

class TableSelector:
    def __init__(self, items, criteria):
        """
        Class that acts as a filter for Table's Items

        :param items: List of Items objects that will be filtered.
        :param criteria: A List used as filter as an AND of ORs (see CNF). Examples:
            [{date: today}, [{tag: 1},{tag: 2}]] // (date === today && (tags === 1 || tags === 2))
            [[{assigneeId: 'GO'}, {assigneeId: 'AM'}]] // (assigneeId === 'GO' || assigneeId === 'AM')
            [{name: 'Guillem'}, {surname: 'Orpinell'}] // (name === 'Guillem' && surname === 'Orpinell')
            {name: 'Guillem', surname: 'Orpinell'} // (name === 'Guillem' && surname === 'Orpinell')

        """
        self.items = items

        if isinstance(criteria, list):
            self.clauses = criteria
        else:
            self.clauses = [criteria]

    def execute(self):
        """
        Method to filter items on a table based on field name and value.

        :return: List of Items containing only filtered items or and empty List.

        """
        return [item for item in self.items if self._matches(item, self.clauses)]

    def _matches(self, item, clauses):
        """
        Method that applies AND & OR filters to an item.

        :return: List of Items containing only filtered items or and empty List.

        """
        for clause in clauses:
            if isinstance(clause, dict) and not self._matches_and_clause(item, clause):
                return False
            if isinstance(clause, list) and not self._matches_or_clauses(item, clause):
                return False
        return True

    @staticmethod
    def _matches_and_clause(item, clause):
        for header, value in clause.items():
            if not item.matches_value(header, value):
                return False
        return True

    @staticmethod
    def _matches_or_clauses(item, clauses):
        for clause in clauses:
            if not isinstance(clause, dict):
                raise ValueError('OR clauses need to be dictionaries')
            for header, value in clause.items():
                if item.matches_value(header, value):
                    return True
        return False

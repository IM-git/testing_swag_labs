class ComparisonTools:
    """These tools are used to compare values."""

    @staticmethod
    def compare_sequences_numbers_by_sort_order(list_values: list) -> bool:
        pre_index = 0
        for index in range(1, len(list_values)):
            pre_value = float(list_values[pre_index].lstrip('$'))
            value = float(list_values[index].lstrip('$'))
            pre_index = index
            if pre_value >= value:
                pass
            else:
                return False
        return True

    @staticmethod
    def compare_sequences_names_sort_order(list_values: list) -> bool:
        pre_index = 0
        for index in range(1, len(list_values)):
            pre_value = list_values[pre_index].split()
            value = list_values[index].split()
            pre_index = index
            boolean_value = ComparisonTools.comparing(pre_value, value)
            if boolean_value is True:
                pass
            else:
                return False
        return True

    @staticmethod
    def comparing(first_value: str, second_value: str) -> bool:
        for index in range(len(first_value)):
            if first_value[index] > second_value[index]:
                return True
            elif first_value[index] == second_value[index]:
                continue
            else:
                return False
        return True

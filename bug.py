def function_with_uncommon_error(data):
    if not data:
        return []
    result = []
    for item in data:
        try:
            processed_item = process_item(item)
            result.append(processed_item)
        except Exception as e:
            # This is the problematic part 
            print(f"Error processing item: {item}, Error: {e}")
            # Instead of printing error and continuing, raise the exception
            # raise e
    return result


def process_item(item):
    # Simulates some processing that might raise an exception
    if item == 'error':
        raise ValueError("Cannot process 'error' item")
    return item * 2

data = ['a', 'b', 'error', 'c']
print(function_with_uncommon_error(data))
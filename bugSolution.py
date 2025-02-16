def function_with_uncommon_error(data):
    if not data:
        return []
    result = []
    for item in data:
        try:
            processed_item = process_item(item)
            result.append(processed_item)
        except ValueError as e:
            # Handle specific exception type, for example by adding a default value.
            print(f"Error processing item: {item}, Error: {e}")
            result.append(None) # Or another suitable default value
        except Exception as e: # Catch other unexpected errors
            # Log or handle more serious issues
            print(f"An unexpected error occurred processing item: {item}. Error: {e}")
            raise  # Re-raise to ensure the issue is addressed
    return result

def process_item(item):
    # Simulates some processing that might raise an exception
    if item == 'error':
        raise ValueError("Cannot process 'error' item")
    return item * 2

data = ['a', 'b', 'error', 'c']
print(function_with_uncommon_error(data))
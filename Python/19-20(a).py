initial_dict = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
    'key4': 'value4',
    'key5': 'value5',
    'key6': 'value6',
    'key7': 'value7',
    'key8': 'value8',
    'key9': 'value9',
    'key10': 'value10'
}

print("| Key  | Value |")
print("|------|-------|")

for key, value in initial_dict.items():
    print(f"| {key:<5}| {value:<6}|")

print(f"\nTotal number of records: {len(initial_dict)}")

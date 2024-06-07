# This script removes version specifications from your existing requirements.txt

with open('requirements.txt', 'r') as f:
    lines = f.readlines()

with open('requirements.in', 'w') as f:
    for line in lines:
        # Skip comments and blank lines
        if line.startswith('#') or not line.strip():
            continue
        # Remove version specifications
        package = line.split('==')[0].split('>=')[0].split('<')[0].strip()
        f.write(package + '\n')

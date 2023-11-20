def next_version(current_version):
    version_numbers = int("".join(current_version))
    new_version = str(version_numbers + 1)
    return f"{'.'.join(new_version)}"


version = input().split(".")
print(next_version(version))
from gen_hotkeys import *
from tests import test_cases

def main():
    race, grid, prefix, name = test_cases.case2().values()
    print(f"Testing: {test_cases.case2()}")
    print("\n\n")

    hotkey_profile = GridHotkeys(
        race, name, custom_grid=grid, grid_key_prefix=prefix, verbose=True)
    hotkey_profile.gen_hotkey_file()


if __name__ == "__main__":
    main()